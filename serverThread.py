import threading
import time
s=serial.Serial('/dev/ttyUSB1', 9600, timeout=1)

def write():
	data=raw_input("Server: ")
	s.write(data)

def read():
	while True:
	data=s.read(100)
	if len(data)>0:
		print "Client :" data

w=threading.Thread(target=write)
r=threading.Thread(target=read)
write.start()
read.start()
