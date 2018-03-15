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
	menu = '''
Please select an option:
|| 1 - add patient   || 2 - find patient   || 3 - list all patients 
|| 4 - export patient information to XML   || 0 - exit
Option: '''
	
	option = 1
	
	try:
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
				
	finally:
		print "\nExiting TChima Clinic...Goodbye!"
		con.commit()
		con.close()

def addPatient(cur):
	name = raw_input("Enter Name: First Last\n")
	name = name.strip().title()
	
	while (len(name.split()) < 2):
		print "Must enter first and last name"
		name = raw_input("Enter Name: First Last\n")
		name = name.strip().title()
	
	statement = "insert into patient (fname, lname) values ('"+name.split()[0]+"', '"+name.split()[1]+"')"
	cur.execute(statement)
	print "Patient added"

def findPatient(cur):
	name = raw_input("Enter Name: First or Last\n")
	name = name.strip().title()
	
	if (len(name.split()) < 2):
		statement = "select * from patient where fname='"+name+"' or lname='"+name+"'"
	
	else:
		statement = "select * from patient where fname='"+name.split()[0]+"' and lname='"+name.split()[1]+"'"
	
	#print statement
	cur.execute(statement)
	
	count = 0
	for result in cur:
		print result
		count = count+1
	
	if count is 0:
		print "No patients found"
	
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



