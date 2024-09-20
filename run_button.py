import serial
import serial.tools.list_ports
import os, random

def checkPorts():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        print(p)
        if "Arduino" in p.description:
            return p.device
        
def chooseRandomFile():
    name = random.choice(os.listdir("./pdfs")) #change dir name to whatever
    print (name)
    return name
 
def readserial(comport, baudrate):

    ser = serial.Serial(comport, baudrate, timeout=0.1)         # 1/timeout is the frequency at which the port is read

    while True:
        data = ser.readline().decode().strip()
        if data:
            print(data)
            name = "./pdfs/"+chooseRandomFile()
            print(name)
            os.system("lpr -P 'HP DeskJet 4200 series [6D09F8]' ./COMPLICIT-14.43.00.pdf")



if __name__ == '__main__':
    port = checkPorts()
    print("port",port)
    readserial(port, 9600)