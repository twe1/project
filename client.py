import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('localhost', 8000))
print "Connected to server."
packet=[]
for i in range(0,3):
	packet.append(raw_input('Data: '))
s.sendall(str(packet))
print "Data is sent to server."
s.close()
