HOW TO PROPERLY USE THIS SOFTWARE.
NEEDS PYTHON INSTALLED TO WORK: python.org/downloads/
AFTER INSTALATION, ADD PYTHON TO GLOBAL VARIABLES ON COMPUTER.
ATTENTION: TO RUN THIS PROGRAM, YOU HAVE TO USE PYTHON2

When the program is done, the data will be save into the database(mydb.db).

BEFORE USE:
User must enter the following into a CMD prompt:

python -m pip install datetime
python -m pip install Tkinter
pip install sqlite3

Allow for the installation to complete, then the program is ready to run.

Simply type: python d2p2.py

AFTER THE PROGRAM IS DONE, THE DATA WILL BE SAVED INTO THE DATABASE(mydb).
YOU CAN CHECK THE DATA BY OPEN THE DATABASE(using following command):

sqlite3 mydb
select * from User;

OR, IF YOU WANT TO EXPORT THE DATA INTO .CSV FILE:

sqlite3 mydb
.header on
.mode csv
.output data.csv
select * from User;
.quit

THEN, YOU CAN GET THE DATA LOG FILE OF THE PROGRAM.