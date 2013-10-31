Databased to REST API
=====================

db2rest provides a HTTP REST API for relational databases. You might find
it most useful for tasks where you want access the database by using the HTTP
protocol.


#### To install
	
check it out from the repository
	
	cd project_dir
	python setup.py install

#### To contribute

check it out from the repository
	
	cd project_dir
	python setup.py develop

#### To configure
	
	cd project_dir	
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
	
#### To run
	
	cd project_dir_name
	python db2rest/app.py


#### To get info from command line
Set you password in this way avoiding to keep in the history shell:
	
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
	
	
	
	
	
	
	
	
	
	
	
		
	
	
