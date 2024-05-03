#include <Arduino.h> // Standard Arduino library
#include <Wire.h> // Library for I2C communication
#include <SparkFun_BMI270_Arduino_Library.h> // SparkFun BMI270 library
#include <SD.h> // SD card library
#include <SPI.h> // SPI library for SD card
#include <esp_log.h> // ESP32 logging library

#define TAG "main" // Define a tag for logging purposes

BMI270 m5IMU; // Creating an instance of the BMI270 sensor
uint8_t i2cAddress = BMI2_I2C_SEC_ADDR; // 0x69

void setup() {
  Serial.begin(115200); // Initialize serial communication
  pinMode(46, OUTPUT); // Set pin 46 as output
  digitalWrite(46, HIGH); // Set pin 46 to HIGH
  Wire.begin(8, 10, 400000); // Initialize I2C communication with SDA pin 8 and SCL pin 10 at 400kHz
  uint8_t ans;
  do {
    delay(1000); // Delay for 1 second
    ans = m5IMU.beginI2C(i2cAddress); // Initialize BMI270 sensor with I2C address
    Serial.println(ans); // Print initialization result
  } while(ans != BMI2_OK); // Repeat until initialization is successful
  ESP_LOGW(TAG, "Booted"); // Log a warning message
}

void loop() {
  m5IMU.getSensorData(); // Get sensor data from BMI270
  Serial.printf("%lu, %.2f,%.2f,%.2f\n", millis(), m5IMU.data.accelX, m5IMU.data.accelY, m5IMU.data.accelZ); // Print timestamp and accelerometer data
  delay(10); // Delay for 10 milliseconds
}
