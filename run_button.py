import serial
import serial.tools.list_ports
import os

def checkPorts():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        print(p)
        if "Arduino" in p.description:
            return p.device
def readserial(comport, baudrate):

    ser = serial.Serial(comport, baudrate, timeout=0.1)         # 1/timeout is the frequency at which the port is read

    while True:
        data = ser.readline().decode().strip()
        if data:
            print(data)
            os.system("lpr -P Canon_MG3600_series COMPLICIT-14.43.00.pdf; echo 'printin'")



if __name__ == '__main__':
    port = checkPorts()
    print("port",port)
    readserial(port, 9600)