import serial
s=serial.Serial('/dev/ttyUSB0', 9600, timeout=0.1)
print 'Server connected'

def clientdata():
	data=raw_input('Client: ')
	s.write(data)
	while True:
		server=s.read(100)
		if len(server)>0:
			print 'Server: ', server
			break
	clientdata()		

clientdata()

