# connect to the coachingBot_DB and check, if the user table already exists. If not, create it.
import sqlite3

def create_db ():
    # connect to db
    connection = sqlite3.connect("coachingBotDB.db")

    # cursor
    cursor = connection.cursor()

    # put table checker sql statement into a variable
    # checker = '''SELECT count(name)
    #     FROM sqlite_master
    #     WHERE type='table' AND name='users'
    # '''
    # cursor.execute(checker)

    # put table creation sql statement into a variable
    table_users = '''CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        gender TEXT,
        photo BLOB,
        birthdate INT,
        email TEXT UNIQUE,
        telephone TEXT UNIQUE,
        longitude INT,
        latitude INT,
        bio TEXT,
        state INT
    );'''

    #if count is 1, table already exists - else, create it
    if cursor.fetchone()[0]==1:
        print('+++++ ALREADY EXISTS: table "users" +++++')
    else:
        cursor.execute(table_users)
        print('+++++ CREATED table: "users" +++++')

    #commit changes to db
    connection.commit()

    # close connection
    connection.close()


if __name__ == '__main__':
    create_db()
