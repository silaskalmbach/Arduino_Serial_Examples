import serial
import time
import json 

arduino1 = serial.Serial(port='COM4', baudrate=9600, timeout=1)


def writeSerial():
    Text = {"Geschwindigkeit": [20, 10, 30], "Richtung":[1,1,-1]}
    Text = json.dumps(Text)                         # Umwandlung Dictionary zu Json-String
    arduino1.write(Text.encode())                           # Senden des encodeten Json-String (Umwandlung in Byte)
    print("send")



if __name__ == "__main__":
    while True:
        if arduino1.isOpen():
            writeSerial()
            print("open")
            try:
                Text = arduino1.readline()
                Text = str(Text, 'utf-8')
                print(Text)
            except:
                print("nichts Empfangen")
            time.sleep(2)
        else:
            print("Nicht verbunden")