import serial
s=serial.Serial('/dev/ttyUSB1', 9600, timeout=1)

while True:
	fData=s.read(100)
	if len(fData)>0:
		s.write(fData)
		print 'sending: ',fData
