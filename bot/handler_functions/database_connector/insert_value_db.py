# connect to the coachingBot_DB and check, if the user table already exists. If not, create it.
import sqlite3


def insert_update (user_id, column, value):
    # connect to db
    connection = sqlite3.connect("coachingBotDB.db")
    print("+++++ Connected to coachingBotDB. +++++")

    # cursor
    cursor = connection.cursor()
    print("+++++ Cursor created. +++++")

    # sql command to check, if user exists
    user_check = f'SELECT EXISTS (SELECT 1 FROM users WHERE user_id={user_id})'
    cursor.execute(user_check)

    if not cursor.fetchone():
        print("+++++ No record found +++++")
        cursor.execute('INSERT INTO users VALUES (?)', (user_id,))
        print (f'CREATED record {user_id}')

    # sql command to UPDATE an existing record
    update_command = f"UPDATE users SET {column} = ? WHERE user_id = ?"
    update_args = (value, user_id)

    cursor.execute(update_command, update_args)
    print (f'UPDATED record {user_id}: {column} >> {value}')

    #commit changes to db			
    connection.commit()
    print('+++++ COMMITTED changes to DB. +++++')  

    # close connection
    connection.close()
    print ('+++++ CLOSED connection to DB. +++++')

