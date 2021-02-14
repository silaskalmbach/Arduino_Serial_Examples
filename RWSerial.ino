#include <ArduinoJson.h>

DynamicJsonDocument doc(512);
DynamicJsonDocument doc1(512);
DynamicJsonDocument doc2(512);

void setup(){
  Serial.begin(9600);
}

void loop() {
while (!Serial) {} // wait for serial port to connect. Needed for native USB
while (Serial.available() == 0) {} // wait for serial port to send data
doc = readSerial();
writeSerial();
}

void readSerial(){
  // Daten Empfangen

  if (Serial.available() > 0) {
  deserializeJson(doc2, Serial);
  return doc2;

  // Daten Auslesen
  int G1 = doc2["Geschwindigkeit"][0];  
  int G2 = doc2["Geschwindigkeit"][1];   
  int G3 = doc2["Geschwindigkeit"][2];

  // // Daten Senden
  // serializeJson(doc2, Serial);
  // Serial.println();
}
}

void writeSerial(){
  if (Serial) {
  // Daten zum Senden
  int G1 = doc2["Geschwindigkeit"][0];  
  int G2 = doc2["Geschwindigkeit"][1];   
  int G3 = doc2["Geschwindigkeit"][2]; 

  doc1["Sonar"][0] = G1;
  doc1["Sonar"][1] = G2;
  doc1["Sonar"][2] = G3; 

  // Daten Senden
  serializeJson(doc1, Serial);
  Serial.println();
  }
}