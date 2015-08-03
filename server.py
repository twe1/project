import socket
import serial
import sqlite3

class database():

	def __init__(self):
		self.s=sqlite3.connect('report.db')
		self.c=self.s.cursor()

	def insertData(self,eid,dpt,code):
		self.c.execute('''INSERT INTO tb(empid,dept,code) VALUES(?,?,?)''',(eid,dpt,code))
		self.s.commit()

	def close():
		self.s.close()	

class employee():
	def __init__(self):

		self.db=database()

		#self.xbee = serial.Serial('/dev/ttyUSB0', 9600, timeout = 1)

		self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.s.bind(('0.0.0.0', 8000))
		self.s.listen(1)
		self.sock,self.var2 = self.s.accept()
		
	def main(self):
		packet = self.recvdata()
		sms = self.extractdata(packet)
		self.senddata(sms)

	def recvdata(self):
		while True:
			packet = self.sock.recv(100)
			
			if len(packet)>0:
				print "Received Data: ", packet
				return packet

	def senddata(self,sms):
		print sms
		
	def extractdata(self,packet):
		data = packet.split(';')

		self.db.insertData(data[0],data[1],data[2])

		sms = 'EmpID: ' +data[0]+'\nDpt ID: ' +data[1]+'\nCode: '+data[2]
		return sms

emp=employee()
while True:
	emp.main()

		

		

	
		
		
		