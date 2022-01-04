import sqlite3
  
def getAllData(user_id):
    # connect to db
    connection = sqlite3.connect("coachingBotDB.db")
    print("+++++ Connected to coachingBotDB. +++++")

    # cursor
    cursor = connection.cursor()
    print("+++++ Cursor created. +++++")
    
    selection = f"""SELECT * 
        FROM coachingBotDB.users
        WHERE user_id = {user_id} 
        """

    # execute command to fetch all data from table users
    cursor.execute(selection)
    
    # store all data from selection in table_data
    table_data = cursor.fetchall()
    
    # print table
    for i in table_data:
        print(i)

    return table_data


def getFirstName(user_id):
    # connect to db
    connection = sqlite3.connect("coachingBotDB.db")
    print("+++++ Connected to coachingBotDB. +++++")

    # cursor
    cursor = connection.cursor()
    print("+++++ Cursor created. +++++")
    
    selection = f"""SELECT first_name 
        FROM coachingBotDB.users
        WHERE user_id = {user_id} 
        """

    # execute command to fetch all data from table users
    cursor.execute(selection)
    
    # store all data from selection in table_data
    table_data = cursor.fetchall()
    
    # print table
    for i in table_data:
        print(i)

    return table_data
    