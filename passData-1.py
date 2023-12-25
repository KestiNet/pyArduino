import time
import serial
arduinoData=serial.Serial('com6',9600)#specify com port and baud rate
time.sleep(1)

while True:
    while(arduinoData.inWaiting()== 0):
        pass
    dataPacket=arduinoData.readline()#reads data from arduino
    dataPacket=str(dataPacket,'utf-8')#Converts the bytes to utf-8
    dataPacket=dataPacket.strip('\r\n')#strips the \r and \n from the print
    splitPacket = dataPacket.split(",")#splits the dataPacket from the comma
    x = float(splitPacket[0])#Convert X, Y, Z from string to floats
    y = float(splitPacket[1])
    z = float(splitPacket[2])

    print("X=", x,"Y=",y,"Z=",z)

    