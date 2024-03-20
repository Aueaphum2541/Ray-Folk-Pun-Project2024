#include <Arduino.h> // Standard Arduino library
#include <SparkFun_BMI270_Arduino_Library.h> // SparkFun BMI270 library
#include "FS.h"
#include "SD.h"
#include "SPI.h"
#include "Wire.h"
#include <esp_log.h> // ESP32 logging library

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

bool detect_sd() {
  if (!SD.begin(cs)) {
    return false;
  } else {
    return true;
  }
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
}

void loop() {

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

  delay(1000/20); // 50Hz
}
