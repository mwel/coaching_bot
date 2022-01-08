import sqlite3
  
def getAllData(user_id):
    # connect to db
    connection = sqlite3.connect("coachingBotDB.db")

    # cursor
    cursor = connection.cursor()
    
    # SELECT all info from user with respective user_id
    selection = f"""SELECT * 
        FROM users
        WHERE user_id = {user_id} 
        """
    
    user_count = cursor.execute(selection)

    # execute command to fetch all data from table users
    print(f'+++++ Coaching Bot Users: ({user_count}) +++++')
    # execute command to fetch all data from table users
    cursor.execute(selection)
    
    # store all data from selection in table_data
    table_data = cursor.fetchall()
    
    # print table
    for i in table_data:
        print(i)

    return table_data



def getValue(user_id, column):
    # connect to db
    connection = sqlite3.connect("coachingBotDB.db")

    # cursor
    cursor = connection.cursor()
    
    selection = f"""SELECT {column} 
        FROM users
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
    