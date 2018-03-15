#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Oracleprac.py: Practice project using OracleDB.
	Emulates hospital management system
"""

def main(): # where the code starts running from
	print "hello world!"
	connectDB()
	
def connectDB(): # establish connection to Oracle cloud DB
	import cx_Oracle
	con = cx_Oracle.connect('system/XUCVAdwd1_@129.157.176.137/orcl')
	print con.version
	cur = con.cursor()
	cur.execute('select * from patient order by id')
	for result in cur:
		print result
	con.close()

def createStatement():
	pass # empty statement



if __name__ == "__main__": # calls the function main()
    main()



