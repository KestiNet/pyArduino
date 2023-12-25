import time
import serial
arduinoData=serial.Serial('com6',9600)#specify com port and baud rate
time.sleep(1)

dataPacket=arduinoData.readline()#reads data from arduino
print(dataPacket)