import serial
import time
import json 

arduino1 = serial.Serial(port='COM4', baudrate=9600, timeout=1)
print(arduino1.readline()) # Erstes mal printen, da hier oft nicht vollständig

def readSerial():
    Text = arduino1.readline()
    Text = str(Text, 'utf-8')
    Text = json.loads(Text) 
    return Text

if __name__ == "__main__":
    while True:
        if arduino1.isOpen():
            Text = readSerial()
            print(Text)
            Sonar1 = Text["Sonar"][0]
            Sonar2 = Text["Sonar"][-1]
            print(Sonar1)
            print(Sonar2)
        else:
            print("Nicht verbunden")