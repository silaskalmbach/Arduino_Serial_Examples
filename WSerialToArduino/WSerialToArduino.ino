#include <ArduinoJson.h>

DynamicJsonDocument doc2(512);

void setup(){
  Serial.begin(9600);
}

void loop() {
readSerial();

}

void readSerial(){
  if (Serial.available() > 0) {
  deserializeJson(doc2, Serial);
  int G1 = doc2["Geschwindigkeit"][0];  
  int G2 = doc2["Geschwindigkeit"][1];   
  int G3 = doc2["Geschwindigkeit"][2];                                       // Speichervariable für die Stellwerte des 1. Kanals/Scheibe 
  Serial.print(G1);
  Serial.println();}
}
