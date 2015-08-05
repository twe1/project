import serial
s=serial.Serial('/dev/ttyUSB1', 9600, timeout=1)
fData=s.read(100)
s.write(fData)