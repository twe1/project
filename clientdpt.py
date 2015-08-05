import serial
import time
s=serial.Serial('/dev/ttyUSB1', 9600, timeout=1)

while True:
	fData=s.read(100)
	time.sleep(1)
	print fData, '.', 
	if len(fData)>0:
		s.write(fData)
		print 'sending: ',fData
