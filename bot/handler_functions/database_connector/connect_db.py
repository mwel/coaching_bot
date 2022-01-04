# connect to the coachingBot_DB and check, if the user table already exists. If not, create it.
import sqlite3

def connect_db ():
    # connect to db
    connection = sqlite3.connect("coachingBotDB.db")
    print("+++++ Connected to coachingBotDB. +++++")

    # cursor
    cursor = connection.cursor()
    print("+++++ Cursor created. +++++")

    # put table checker sql statement into a variable
    checker = '''SELECT count(name) 
        FROM sqlite_master 
        WHERE type='table' AND name='users' 
    '''
    cursor.execute(checker)

    # put table creation sql statement into a variable
    table_users = '''CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        gender TEXT,
        photo BLOB,
        birthdate INT,
        email TEXT UNIQUE,
        phone TEXT UNIQUE,
        longitude INT,
        latitude INT,
        bio TEXT,
        state INT
    );'''

    #if count is 1, table already exists - else, create it and tell me you did!
    if cursor.fetchone()[0]==1: 
        print('+++++ Table "users" already exists. +++++')
    else:
        cursor.execute(table_users)
        print('+++++ Table "users" created. +++++')

    #commit changes to db			
    connection.commit()
    print('+++++ COMMITTED changes to DB. +++++')  

    # close connection
    connection.close()
    print ('+++++ CLOSED connection to DB. +++++')


if __name__ == '__main__':
    connect_db()

