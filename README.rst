Databased to REST API
=====================

.. image:: https://pypip.in/v/db2rest/badge.png
    :target: https://crate.io/packages/db2rest/
    :alt: Latest PyPI version

.. image:: https://pypip.in/d/db2rest/badge.png
    :target: https://crate.io/packages/db2rest/
    :alt: Number of PyPI downloads

db2rest provides a HTTP REST API for relational databases. You might
find it most useful for tasks where you want access the database by
using the HTTP protocol.

Installation
^^^^^^^^^^^^

Egg-files for this project are hosted on PyPi. You should be able to use
pip to automatically install this project.

::

    pip install db2rest

Configuration
^^^^^^^^^^^^^

::

    edit YOUR_PACKAGE_PATH:db2rest/confing.example

In order to connect to the database modify the string connection and the
configure LDAP to provied to the API a way to authorize the users.

::

    [db]
    string_connection: mysql://USER:@127.0.0.1:PORT/dbname

    [webserver]
    host: 127.0.0.1
    port: 5000

    [logger]
    level: DEBUG

    [ldap]
    string_connection: ldap://LDAPSERVER
    query:              MYQUERY

Rename it:

::

    YOUR_PACKAGE_PATH:db2rest/config.cfg

Example
^^^^^^^

Type the following command:

::

    db2rest-run

or,

::

    db2rest-run YOUR_CONFIG_FILE 

If everthing went fine you should be able to see the following two
lines:

::

    INFO:werkzeug: * Running on http://127.0.0.1:5000/
    INFO:werkzeug: * Restarting with reloader

To query your database from command line using curl
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set you password in this way the password isn't in the history's shell:

::

    read -s -p "Enter Password: " mypassword
    Enter Password:********

--------------

To get all tables present in the databases:

::

    curl --user usernmae:$mypassword -i -H "Accept: application/json" -X GET  http://localhost:5000/  

--------------

To get all row from a table in the database:

::

    curl --user usernmae:$mypassword -i -H "Accept: application/json" -X GET  http://localhost:5000/mytablename 

--------------

To update a field of a row:

::

    curl --user usernmae:$mypassword -i -H "Accept: application/json" -X PUT  -d "myfield=myvalue "http://localhost:5000/mytablename/myid 

--------------

NOTES
^^^^^

This software is also on GITHub because of Travis-Ci provides a continuos service integration:  https://github.com/nikpalumbo/db2rest.git
