#include <ArduinoJson.h>

DynamicJsonDocument doc(512);

void setup(){
  Serial.begin(9600);
}
  
void loop() {
  //Empfangen
  if (Serial.available()) {
  deserializeJson(doc, Serial);
  //Mach was damit
  doc = doSomething(doc);
  //Senden
  serializeJson(doc, Serial);
  Serial.println();
  }
  // doc = doSomething(doc);
} 

DynamicJsonDocument doSomething (JsonDocument& Values){
  //Anpassen nach Zweck
  Values["Geschwindigkeit"][1] = 900;
  Values["Richtung"][0] = -1;
  Values["Tiefe"][2] = 30;
  return Values;
}
