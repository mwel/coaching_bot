""" Deltes one or all records of a specific user """


# imports
import sqlite3
from handler_functions.database_connector.select_db import user_search

# delete all data of a specific user
def delete_record(user_id):
    
    if user_search(user_id):
        try:
            # connect to db
            connection = sqlite3.connect("coachingBotDB.db")

            # cursor
            cursor = connection.cursor()

            # DELETE record for specific user_id
            cursor.execute(f'''DELETE FROM users WHERE user_id = {user_id};''')
            print(f'----- DELETED record for user_id: {user_id}. -----')  

            #commit changes to db			
            connection.commit()
        
            # close connection
            connection.close()
        
        except:
            print(f'----- ERROR while trying to delete record for user_id: {user_id}. -----')  




# delete one value of a specific user
def delete_value(user_id, column):
    
    if user_search(user_id):
        try:
            # connect to db
            connection = sqlite3.connect("coachingBotDB.db")

            # cursor
            cursor = connection.cursor()

            selection = f"""DELETE {column}
                FROM users
                WHERE user_id = {user_id}
                """

            # DELETE record for specific user_id
            cursor.execute(selection)

            print(f'----- DELETED {column} for user_id: {user_id}. -----')  

            #commit changes to db			
            connection.commit()
        
            # close connection
            connection.close()
        
        except:
            print(f'----- ERROR while trying to delete record for user_id: {user_id}. -----')  

