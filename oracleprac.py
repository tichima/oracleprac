#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Oracleprac.py: Practice project using OracleDB.
	Emulates hospital management system
"""


def main(): # where the code starts running from
	connectDB()
	
def connectDB(): # establish connection to Oracle cloud DB
	import cx_Oracle
	#con = cx_Oracle.connect('system/XUCVAdwd1_@129.157.176.137:1521/orcl')
	
	ip = '129.157.176.137'
	port = 1521
	SID = 'ORCL'
	dsn = cx_Oracle.makedsn(ip, port, SID)
	con = cx_Oracle.connect('system', 'XUCVAdwd1_', dsn)
	cur = con.cursor()
	
	
	print 'Welcome to TChima Clinic.'
	menu = '''Please select an option:
|| 1 - add patient || 2 - find patient || 3 - list all patients 
|| 4 - export patient information to XML 
|| 0 - exit
'''
	
	option = 1
	
	while(option):
		option = input(menu)
	
		if option is 1:
			addPatient(cur)
			
		if option is 2:
			findPatient(cur)
			
		if option is 3:
			listAllPatient(cur)
			
		if option is 4:
			exportPatient(cur)
	
	print "Exiting TChima Clinic...Goodbye!"
	
	con.close()

def addPatient(cur):
	# statement = 'select * from patient order by id'
	# cur.execute(statement)
	# id = 0
	# for result in cur:
		# id = id+1
		
	# id = id+1
	# name = raw_input("Enter Name: First Last")
	
	# while (len(name.split()) < 2):
		# print "Must enter first and last name"
		# name = raw_input("Enter Name: First Last")
	
	# statement = 'insert into patient (id, fname, lname) values ('+str(id)+', '+name.split()[0]+', '+name.split()[1]+')'
	# print statement
	# cur.execute(statement)
	pass

def findPatient(cur):
	pass

def listAllPatient(cur):
	cur.execute('select * from patient order by id')
	for result in cur:
		print result
	
	
def exportPatient(cur):
	pass

def debug(cur):
	print con.version


if __name__ == "__main__": # calls the function main()
    main()



