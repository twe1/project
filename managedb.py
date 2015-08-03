import sqlite3

class database():

	def __init__(self):
		self.s=sqlite3.connect('report.db')
		self.c=self.s.cursor()

	def createTable(self):
		self.c.execute('''CREATE TABLE tb(id INTEGER PRIMARY KEY AUTOINCREMENT,
		 empid STRING, dept STRING, code STRING)''')

obj=database()
obj.createTable()