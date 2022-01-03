# connect to the coachingBot_DB and 
import sqlite3
import database_connector
  
# connecting to the database
connection = sqlite3.connect("coachingBotDB.db")
  
# cursor
cursor = connection.cursor()
# print with no errors
print("Successfully connected to coachingBotDB")

# if none exists, create table in database
table_users = str(database_connector.CREATE_user_table.sql)
  
# execute the statement
cursor.execute(table_users)

# close the connection
connection.close()

