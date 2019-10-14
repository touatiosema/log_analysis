# Logs Analysis
This a program written in python3, It checks the database created by the newsdata.sql in the PostgreSQL database manager to extract usefull information, this database contains information about articles and their authors, and a table of containing a log file information of a web server. The program extracts the following informations:
1. Most popular three articles of all time. 
2. Most popular authors of all time. 
3. Days when error requests are bigger than 1%.

### Prerequisites

You need the following prerequisites:

1. python3:
On debian, you can install it by:
```
sudo apt-get install python3
```
2. psycopg2
On debian, you can install it by:
```
sudo apt-get install python3-psycopg2
```
3. postgresql:
On debian, you can install it by:
```
sudo apt-get install postgresql
```
### Installing

If you have the dependencies, this program doesn't require any installation process.

## Running the tests

In the same folder as log_analysis.py, execute the following.

```
python3 log_analysis.py
```

## Authors

* **TOUATI OSEMA** - *Initial work* - [touatiosema](https://github.com/touatiosema)
