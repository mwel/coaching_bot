# connect to the coachingBot_DB and check, if the user table already exists. If not, create it.
import sqlite3
  
# connecting to the database
connection = sqlite3.connect("coachingBotDB.db")
print("+++++ Connected to coachingBotDB. +++++")

# cursor
cursor = connection.cursor()
print("+++++ Curser created. +++++")

# put table checker sql statement into a variable
checker = '''SELECT count(name) 
    FROM sqlite_master 
    WHERE type='table' AND name='user_table' 
'''
cursor.execute(checker)

# put table creation sql statement into a variable
table_users = '''CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    gender TEXT,
    photo BLOB,
    birthdate INT,
    email TEXT UNIQUE,
    phone TEXT UNIQUE,
    longitude INT,
    latitude INT,
    bio TEXT NOT NULL
);'''

#if count is 1, table already exists - else, create it and tell me you did!
if cursor.fetchone()[0]==1: 
	print('+++++ Table already exists. +++++')
else:
    cursor.execute(table_users)
    print('+++++ Table "table_users" created. +++++')  

#commit changes to db			
connection.commit()
print('+++++ Changes comitted to DB. +++++')  

# close connection
connection.close()
print ('+++++ Connection to DB closed. +++++')

