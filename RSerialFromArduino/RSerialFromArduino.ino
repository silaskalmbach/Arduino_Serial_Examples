#include <ArduinoJson.h>

DynamicJsonDocument doc(512);

void setup(){
  Serial.begin(9600);
}

void loop() {
writeSerial();
}

void writeSerial(){
  for (uint8_t i = 0; i < 5; i++) {
    doc["Sonar"][i] = i;
  }
serializeJson(doc, Serial);
Serial.println();
}
