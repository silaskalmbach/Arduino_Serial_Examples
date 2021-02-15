
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
    # global first_round
    # if first_round:
    #     for i in range(5):
    #         print(arduino1.readline())
    #         first_round = False
    Text = arduino1.readline()
    Text = Text.decode()
    # Text = json.loads(Text.decode())
    return Text
    # if Text[0] == "{":
    #     Text = json.loads(Text.decode(encoding='UTF-8'))
    #     return Text
    # else:
    #     print("fail")
    #     readSerial()
        


if __name__ == "__main__":
    while True:
        if arduino1.isOpen():
            try:
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
