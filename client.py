import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('localhost', 8000))
print "Connected to server."
packet=[]
for i in range(0,3):
	packet.append(raw_input('Data: '))
packet=packet[0]+';'+packet[1]+';'+packet[2]
s.sendall(packet)
print "Data is sent to server."
s.close()
