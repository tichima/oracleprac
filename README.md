"# oracleprac" 

Author: T Chima

Functionalities:
	- Update/Modify DB records for hospital management system
	- Port DB information to XML
	- Pull patient information using DB queries
	
Requirements:
	- Python 2.7
	- Oracle SQL Developer (http://www.oracle.com/technetwork/developer-tools/sql-developer/downloads/index.html)

Clone repo:	
		
		$ git clone https://github.com/tichima/oracleprac.git
		$ git checkout -b tilden master
				
To run:
		
		$ python oracleprac.py
	
++++++++++++++++++++++++++++++++++++++++++++++++
Challenges faced:
	- Navigating the Oracle DB Console
	- Took a while to find how to enable access rules since I was working from scratch
	- Verbose documentation
	- use SSH (Secure Shell) to connect to cloud instance created using PuTTY
	- PuTTY SSH Key in unsupported default UNIX format since I was on a Windows machine
		
Resources:
	- http://www.oracle.com/webfolder/technetwork/tutorials/obe/cloud/dbaas/obe_dbaas_QS/oracle_database_cloud_service_dbaas_quick_start.html
	- http://www.oracle.com/webfolder/technetwork/tutorials/obe/cloud/apaas/python/python-oracle-accs/python-oracle-accs.html
	- https://www.youtube.com/watch?v=w3WVqn3WySs
	-
	
++++++++++++++++++++++++++ DATABASE OUTLINE ++++++++++++++++++++++

UoD: Hospital

TABLES: PATIENTS - ID, NAME, DOB
		PRESCRIPTIONS - ID, PATIENT1D, DATE, DCTR
	
!lisa.jones.OCular@4FeLLOW	
