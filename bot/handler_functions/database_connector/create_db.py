"""connect to the coachingBot_DB and check, if the user table already exists. If not, create it."""

# imports
import sqlite3
from logEnabler import logger


db = 'coachingBotDB.db'

# build a new db, if none exists yet
def create_db ():
    # connect to db
    connection = sqlite3.connect(db)
    # cursor
    cursor = connection.cursor()

    # put table checker sql statement into a variable
    checker = '''SELECT count(name)
        FROM sqlite_master
        WHERE type='table' AND name='users'
    '''

    # put table creation sql statement into a variable
    table_users = '''CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        time_stamp TEXT,
        first_name TEXT,
        last_name TEXT,
        gender TEXT,
        photo BLOB,
        birthdate INTEGER,
        email TEXT UNIQUE,
        telephone TEXT UNIQUE,
        longitude INTEGER,
        latitude INTEGER,
        bio TEXT,
        state INTEGER,
        mail_sent BOOLEAN,
        appointment TEXT,
        event_id TEXT
    );'''

    cursor.execute(checker)

    #if count is 1, table already exists - else, create it
    if cursor.fetchone()[0]==1:
        logger.info('+++++ TABLE EXISTS: "users" +++++')
    else:
        cursor.execute(table_users)
        logger.info('+++++ TABLE CREATED: "users" +++++')

    #commit changes to db
    connection.commit()
    # close connection
    connection.close()


if __name__ == '__main__':
    create_db()
