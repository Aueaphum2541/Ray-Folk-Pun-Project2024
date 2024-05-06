#include <Arduino.h> // Standard Arduino library
#include <SparkFun_BMI270_Arduino_Library.h> // SparkFun BMI270 library
#include "FS.h"
#include "SD.h"
#include "SPI.h"
#include "Wire.h"
#include <esp_log.h> // ESP32 logging library
#include <WiFi.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>
#include <iostream>
#include <chrono>
#include <ctime>
#include <string>
#include <cstring> // For std::strlen

#define TAG "main" // Define a tag for logging purposes

BMI270 m5IMU; // Creating an instance of the BMI270 sensor
uint8_t i2cAddress = BMI2_I2C_SEC_ADDR; // 0x69

// Pin definition for SPI
const int sck = 14;
const int miso = 39;
const int mosi = 12;
const int cs = 11;

// Buffer for data
char data[100];
JsonDocument json_doc;

// const char* ssid = "Longhuang 2fl";
// const char* password = "08045535532";
const char* ssid = "folkkkkk";
const char* password = "autkakmakmak";

// const char* mqtt_server = "broker.hivemq.com";
const char* mqtt_server = "broker.emqx.io";
const int mqtt_port = 1883; // Default MQTT port
// const char* mqtt_username = "your_mqtt_username"; // If your MQTT server requires authentication
// const char* mqtt_password = "your_mqtt_password"; // If your MQTT server requires authentication
const char* mqtt_topic = "thammasat/chakapat/sensor";

u_int32_t prev_time = millis();

WiFiClient espClient;
PubSubClient client(espClient);

bool detect_sd() {
  if (!SD.begin(cs)) {
    return false;
  } else {
    return true;
  }
}

void setup_wifi() {
  delay(10);
  // Connect to Wi-Fi network with SSID and password
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void setup() {
  // Begin Serial
  Serial.begin(115200);

  // Begin SD
  SPI.begin(sck, miso, mosi, cs);

  // Start IMU
  pinMode(46, OUTPUT); // Set pin 46 as output
  digitalWrite(46, HIGH); // Set pin 46 to HIGH
  Wire.begin(8, 10, 400000); // Initialize I2C communication with SDA pin 8 and SCL pin 10 at 400kHz
  m5IMU.beginI2C(i2cAddress);

  setup_wifi();
  client.setServer(mqtt_server, mqtt_port);
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    if (client.connect("chakapatESP")) {
      Serial.println("connected");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      delay(5000);
    }
  }
}

void loop() {
  // if (millis() - prev_time >= 485) {  // Update every around 1000ms
  if (millis() - prev_time >= 985) {  // Update every around 1000ms
    m5IMU.getSensorData(); // Get sensor data from BMI270
 
    // Format the string with the desired values
    snprintf(data, sizeof(data), "%lu, %.2f, %.2f, %.2f, %.2f, %.2f, %.2f", millis(), m5IMU.data.accelX, m5IMU.data.accelY, m5IMU.data.accelZ, m5IMU.data.gyroX, m5IMU.data.gyroY, m5IMU.data.gyroZ);

    // Detect SD Card
    if (detect_sd()) {
        Serial.println("- Micro SD : Mounted card");
        
        // Open data.txt file in append mode
        File dataFile = SD.open("/data.txt", FILE_APPEND);
        if (dataFile) {
          // Write data to the file
          dataFile.println(data);
          dataFile.close();
          Serial.println("Added data to data.txt");
        } else {
          Serial.println("Error opening data.txt for appending");
        }
      } else {
        Serial.println("- Micro SD : Unmounted card");
      }

      if (!client.connected()) {
          reconnect();
        }

      // Publish a message to the MQTT topic
      char json_str[256];
      json_doc.clear();

      // Get the current time from the ESP32's real-time clock (RTC)
      time_t now = time(nullptr);
      struct tm *timeinfo;
      timeinfo = localtime(&now);

      // Format and add datetime to json_doc
      char datetime_buffer[20]; // Adjust size as needed
      strftime(datetime_buffer, sizeof(datetime_buffer), "%Y-%m-%d %H:%M:%S", timeinfo);
      json_doc["datetime"] = std::string(datetime_buffer);

      json_doc["time"] = millis();
      json_doc["accelX"] = String(m5IMU.data.accelX, 6);
      json_doc["accelY"] = String(m5IMU.data.accelY, 6);
      json_doc["accelZ"] = String(m5IMU.data.accelZ, 6);
      json_doc["gyroX"] = String(m5IMU.data.gyroX, 6);
      json_doc["gyroY"] = String(m5IMU.data.gyroY, 6);
      json_doc["gyroZ"] = String(m5IMU.data.gyroZ, 6);
      serializeJson(json_doc, json_str);
      client.publish(mqtt_topic, json_str, 2);
      Serial.println("Message sent: " + String(json_str));
      prev_time = millis();
      
      client.loop();
  }
}
