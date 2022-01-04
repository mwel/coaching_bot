import sqlite3

def delete_record(user_id):
    # connect to db
    connection = sqlite3.connect("coachingBotDB.db")
    print("+++++ Connected to coachingBotDB. +++++")

    # cursor
    cursor = connection.cursor()
    print("+++++ Cursor created. +++++")
    
    # DELETE record for specific user_id
    cursor.execute(f'''DELETE FROM coachingBotDB.users WHERE user_id = {user_id};''')
    print(f'+++++ DELETED record for user_id: {user_id}. +++++')  

    #commit changes to db			
    connection.commit()
    print('+++++ COMMITTED changes to DB. +++++')  

    # close connection
    connection.close()
    print ('+++++ CLOSED connection to DB. +++++')