import serial
import time
import json 

arduino1 = serial.Serial(port='COM13', baudrate=9600, timeout=1)

def writeSerial(Text):
    Text = json.dumps(Text)
    arduino1.write(Text.encode(encoding='UTF-8'))
    print("send: "+ Text)

def readSerial():
    Text = arduino1.readline()
    Text = Text.decode()
    try:
        Text = json.loads(Text)
        return Text
    except:
        return False

def doSomething(i):
    Text = {"Geschwindigkeit": [1000, i*12, i], "Richtung":[1,1,-1]}
    return Text
        

if __name__ == "__main__":
    i = 0
    while True:
        if arduino1.isOpen():
            Text = doSomething(i)
            writeSerial(Text)                
            print("get:  " + str(readSerial()))
            time.sleep(1)
        else:
            print("Nicht verbunden")
        i += 1