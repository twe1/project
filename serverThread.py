import threading
import serial

s=serial.Serial('/dev/ttyUSB0', 9600, timeout=0.1)

def write():
	while True:
		data=raw_input()
		s.write(data)

def read():
	while True:
		data=s.read(100)
		if len(data)>0:
			print data

w=threading.Thread(target=write)
r=threading.Thread(target=read)
w.start()
r.start()

