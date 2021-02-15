import serial
import time
import json 

arduino1 = serial.Serial(port='COM6', baudrate=9600, timeout=1)


def writeSerial():
    Text = {"Geschwindigkeit": [1000, 10, 30], "Richtung":[1,1,-1]}
    Text = json.dumps(Text)
    arduino1.write(Text.encode(encoding='UTF-8'))
    print("send: "+ Text)

def readSerial():
    Text = arduino1.readline()
    Text = Text.decode()
    Text = json.loads(Text.decode())
    return Text

def doSomething():
    pass
        

if __name__ == "__main__":
    while True:
        if arduino1.isOpen():
            try:
                doSomething()
                writeSerial()
                time.sleep(0.5)
                print("get:  " + readSerial())
                time.sleep(0.5)
            except:
                print("Fehler")
                Abbruch = input("Abbruch?")
                if Abbruch == "JA":
                    break
        else:
            print("Nicht verbunden")