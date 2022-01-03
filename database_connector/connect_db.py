# connect to the coachingBot_DB and 
import sqlite3
  
# connecting to the database
connection = sqlite3.connect("coachingBotDB.db")
  
# cursor
cursor = connection.cursor()
# print with no errors
print("Successfully connected to coachingBotDB")

# SQL command to create a table in the database
sql_command = """CREATE TABLE emp ( 
staff_number INTEGER PRIMARY KEY, 
fname VARCHAR(20), 
lname VARCHAR(30), 
gender CHAR(1), 
joining DATE);"""
  
# execute the statement
cursor.execute(sql_command)

# close the connection
connection.close()

