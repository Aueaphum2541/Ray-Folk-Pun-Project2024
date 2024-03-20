//ESP32 Dev Module
#include "FS.h"
#include "SD.h"
#include "SPI.h"
#include "Wire.h"

// Pin definition for SPI
const int sck = 14;
const int miso = 39;
const int mosi = 12;
const int cs = 11;

bool detect_sd(){
  if(!SD.begin(cs)){
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
}

void loop() {
  // Detect SD Card
  if (detect_sd()) {
    Serial.println("- Micro SD : Mounted card");

    // Open root directory
    File root = SD.open("/");
    // Print all files in the root directory
    while (true) {
      File entry = root.openNextFile();
      if (!entry) {
        // No more files
        break;
      }
      Serial.print("- File: ");
      Serial.println(entry.name());
      entry.close();
    }
    root.close();
  } else {
    Serial.println("- Micro SD : Unmounted card");
  }
  
  delay(1000);
}