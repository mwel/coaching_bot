import sqlite3

def delete_record(user_id):
    # connect to db
    connection = sqlite3.connect("coachingBotDB.db")

    # cursor
    cursor = connection.cursor()
    
    # DELETE record for specific user_id
    cursor.execute(f'''DELETE FROM users WHERE user_id = {user_id};''')
    print(f'+++++ DELETED record for user_id: {user_id}. +++++')  

    #commit changes to db			
    connection.commit()

    # close connection
    connection.close()
