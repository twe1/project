import serial
s=serial.Serial('/dev/ttyUSB1',9600,timeout=0.1)
print 'Client connected'

def serverdata():
	while True:
		client=s.read(100)
		if len(client)>0:
			print 'Client: ', client
			break
	data=raw_input('Server:')
	s.write(data)
	serverdata()

serverdata()	