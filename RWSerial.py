
import serial
import time
import json 

arduino1 = serial.Serial(port='COM4', baudrate=9600, timeout=1 )
first_round = True

def writeSerial():
    Text = {"Geschwindigkeit": [1000, 10, 30], "Richtung":[1,1,-1]}
    Text = json.dumps(Text)
    arduino1.write(Text.encode())
    print("send")

def readSerial():
    # global first_round
    # if first_round:
    #     for i in range(5):
    #         print(arduino1.readline())
    #         first_round = False
    Text = arduino1.readline()
    Text = json.loads(Text.decode(encoding='UTF-8'))
    return Text


if __name__ == "__main__":
    while True:
        if arduino1.isOpen():
            try:
                writeSerial()
                print(readSerial())
            except:
                print("Fehler")
                Abbruch = input("Abbruch?")
                if Abbruch == "JA":
                    break
        else:
            print("Nicht verbunden")
