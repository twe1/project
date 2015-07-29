import socket
import serial

def recvdata():
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.bind(('0.0.0.0', 8000))
	s.listen(1)
	print "Waiting for Client.."
	var1,var2=s.accept()
	print "Connected to Client & waiting for data."
	packet=var1.recv(100)
	print "Received Data: ", packet
	s.close()
	return packet

def senddata():
	s=serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
	data=extractdata()
	print data
	recvdata()

def extractdata():
	data=recvdata()
	data=data.split(';')
	sms='EmpID: ' +data[0]+'\nDpt ID: ' +data[1]+'\nCode: '+data[2]
	return sms

senddata()








