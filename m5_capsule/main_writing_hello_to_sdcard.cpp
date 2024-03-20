#include "FS.h"
#include "SD.h"
#include "SPI.h"
#include "Wire.h"

// Pin definition for SPI
const int sck = 14;
const int miso = 39;
const int mosi = 12;
const int cs = 11;

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
}

void loop() {
  // Detect SD Card
  if (detect_sd()) {
    Serial.println("- Micro SD : Mounted card");

    // Open data.txt file in append mode
    File dataFile = SD.open("/data.txt", FILE_APPEND);
    if (dataFile) {
      // Write "hello" to the file
      dataFile.println("hello");
      dataFile.close();
      Serial.println("Added data to data.txt");
    } else {
      Serial.println("Error opening data.txt for appending");
    }
  } else {
    Serial.println("- Micro SD : Unmounted card");
  }

  delay(1000);
}
