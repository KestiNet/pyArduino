import time
import serial
from vpython import *

arduinoData = serial.Serial('com6',9600)

time.sleep(1)
tube = cylinder(color=color.blue,radius=1, length=5,axis=vector(0,1,0))
label = label(text='5 volts', box =False, pos=vector(0,.2,0))

while True:
    while arduinoData.in_waiting==0:
        pass
    dataPacket=arduinoData.readline()
    dataPacket=str(dataPacket,'utf-8')#Converts the bytes to utf-8
    dataPacket=float(dataPacket.strip('\r\n'))#Converts the string to int
    potVal = dataPacket
    vol=(5./1023.)*potVal
    if vol ==0:
        vol = .001
    tube.length=vol
    vol = round(vol,1) #rounds the value to 2 decimals
    label.text=str(vol)
