Databased to REST API
=====================

db2rest provides a HTTP REST API for relational databases. You might find
it most useful for tasks where you want access the database by using the HTTP
protocol.


#### Installation
Egg-files for this project are hosted on PyPi. You should be able to use pip to automatically install this project.	
	
	pip install db2rest
	
	
#### Configuration
	
	edit db2rest/confing.cfg
	
In order to connect to the database modify the string connection and the configure LDAP to provied to the API a way to authorize the users.   
	
	[db]
	string_connection: mysql://USER:@127.0.0.1:PORT/dbname

	[webserver]
	host: 127.0.0.1
	port: 5000

	[logger]
	level: DEBUG

	[ldap]
	string_connection: ldap://LDAPSERVER
	query:				MYQUERY
	
#### Example

Type the following command:

	db2rest-run

If everthing went fine you should be able to see the following two lines:

	INFO:werkzeug: * Running on http://127.0.0.1:5000/
	INFO:werkzeug: * Restarting with reloader

	

#### To query your database from command line using curl
Set you password in this way the password isn't in the history's shell:
	
	read -s -p "Enter Password: " mypassword
	Enter Password:********
	
***

To get all tables present in the databases:
	
			
	curl --user usernmae:$mypassword -i -H "Accept: application/json" -X GET  http://localhost:5000/  
	
	
***

To get all row from a table in the database:
	
	curl --user usernmae:$mypassword -i -H "Accept: application/json" -X GET  http://localhost:5000/mytablename 
	
	
***

To update a field of a row:
		
	curl --user usernmae:$mypassword -i -H "Accept: application/json" -X PUT  -d "myfield=myvalue "http://localhost:5000/mytablename/myid 
	
***	
		
	
	
