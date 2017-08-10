# Project 3, Logs Analysis Project

This project had us develop queries in PostgreSQL. The queries were designed with increasing levels of complexity. The first query was a simple count with in one table to determine the most popular articles of all time. The second query required using join commands to match
the primary keys from 3 different tables and a concatenate function to determine the most popular article authors of all time. The 3rd query requierd using a query inside of another query and some calculations that would be easier to handle in Python then within the query itself to 
determine on which days did more than !% of requests on the server lead to errors.


To start, make sure that you set the initial configuration of the queries.py file to point to your database, with the correct username and password, otherwise a connection error will occur. 

Then, run: 

```sh
pip -r | requirements.txt
python queries.py
```

This uses Python 2.7.13, located in the `.python-version`.
