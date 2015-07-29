import socket
import serial

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('0.0.0.0', 8000))
s.listen(1)
print "Waiting for Client.."
var1,var2=s.accept()
print "Connected to Client & waiting for data."
packet=var1.recv(100)
print "Received Data: ", packet
s.close()







