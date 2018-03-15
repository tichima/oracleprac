"# oracleprac T Chima"

Intended Functionalities:
- Add patient records for hospital management system (added)
- Pull all/Find unique patient record(s) (added)
- Port patient information to XML (TBD)

Requirements: (1) Python 2.7 (2) cx_Oracle module which can be downloaded using.	
	
	$ python -m pip install cx_Oracle --upgrade
 
  Note: cx_Oracle needs Oracle Instant Client to be installed. Get it here: https://oracle.github.io/odpi/doc/installation.html#id1.
        Ensure the Oracle Instant Client matches the installed 64 or 32 bit version of Python2.7

Clone repo:	
		
	$ git clone https://github.com/tichima/oracleprac.git
				
Easy way to use GitHub: http://bit.ly/2FTHYN4

To run:
		
	$ python oracleprac.py
	
+++++++++++++++++++++++ CHALLENGES FACED +++++++++++++++++++++++++

- The (Secure Shell) SSH Key was in unsupported format since I was on a Windows machine, had to use PuTTY
- Took a while to find how to enable access rules 
		
Resources:

- http://www.oracle.com/webfolder/technetwork/tutorials/obe/cloud/dbaas/obe_dbaas_QS/oracle_database_cloud_service_dbaas_quick_start.html
- http://www.oracle.com/webfolder/technetwork/tutorials/obe/cloud/apaas/python/python-oracle-accs/python-oracle-accs.html
- https://www.youtube.com/watch?v=w3WVqn3WySs
	
++++++++++++++++++++++++++ CURRENT DB OUTLINE ++++++++++++++++++++++

UoD: Hospital

PATIENT table - Columns: ID(PK), FNAME, LNAME, DOB

++++++++++++++++++++++++++ FUTURE WORK ++++++++++++++++++++++

- Add DOCTOR table - Columns: ID(PK), FNAME, LNAME
- Add PRESCRIPTIONS table - Columns: ID(PK), PATIENTID(FK), DATE, DCTRID(FK)






!lisa.jones.OCular@4FeLLOW	
