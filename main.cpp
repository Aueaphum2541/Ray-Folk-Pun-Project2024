#include <Arduino.h>
#include <Wire.h>
#include <SparkFun_BMI270_Arduino_Library.h>
//#include <Arduino_BMI270_BMM150.h>
#include <esp_log.h>

#define TAG "main"

BMI270 m5IMU;
uint8_t i2cAddress = BMI2_I2C_SEC_ADDR; // 0x69

void setup() {
  Serial.begin(115200);
  pinMode(46, OUTPUT);
  digitalWrite(46, HIGH);
  Wire.begin(8, 10, 400000);
  uint8_t ans;
  do {
    delay(1000);
    ans = m5IMU.beginI2C(i2cAddress);
    Serial.println(ans);
  } while(ans != BMI2_OK);
  ESP_LOGW(TAG, "Booted");
}

void loop() {
  m5IMU.getSensorData();
  Serial.printf("%.2f,%.2f,%.2f\n", m5IMU.data.accelX, m5IMU.data.accelY, m5IMU.data.accelZ);
  delay(10);
}
