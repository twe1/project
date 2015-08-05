import socket
import serial
import sqlite3

class database():

	def __init__(self):
		self.s = sqlite3.connect('filename.db')
		self.c = self.s.cursor()

	def inputData(self,eid,dpt,code):								#fn to input data(eid,dpt,code) to table
		self.c.execute('''INSERT INTO tb(empid,dept,code) VALUES(?,?,?)''',(eid,dpt,code))	#tb is the name of the table created
		self.s.commit()

	def close():
		self.s.close()	

class serverduty():									#class contains fns to receive,extract & send data from client  
	def __init__(self):

		self.db = database()							#creating object for outside class database() 
		
		
		self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.s.bind(('0.0.0.0', 8000))
		self.s.listen(1)
		self.a,self.b = self.s.accept()


	def main(self):									#main() calls all fns in this class 
		cData = self.clientData()
		fData = self.extractClientData(cData)
		self.dataToSend(fData)


	def clientData(self):								#fn to receive data from client
		while True:
			cData = self.a.recv(100)
			if len(cData)>0:
				print "Received Client Data: ", cData
				return cData

	def extractClientData(self,cData):						#fn to extract the data received from client
		data = cData.split(';')								

		self.db.inputData(data[0],data[1],data[2])				#calls object db in fn init(), where it will call outside class fn inputData()

		fData = 'EmpID: ' +data[0]+'\nDpt ID: ' +data[1]+'\nCode: '+data[2]
		return fData

	def dataToSend(self,fData):							#fn to send the data received from client to gsm modem
		print fData


s=serverduty()
while True:
	s.main()

