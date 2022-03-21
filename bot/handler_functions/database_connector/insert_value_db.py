""" connect to the coachingBot_DB and check, if the user table already exists. If not, create it."""

# imports 
import sqlite3
from logEnabler import logger


from handler_functions.database_connector.create_db import create_db


def insert_update (user_id, column, value):

    # create db if non-existent
    # TODO: nice-to-have: use if clause to check table existence and only on fail try to create
    create_db()

    # connect to db
    connection = sqlite3.connect("coachingBotDB.db")
    # cursor
    cursor = connection.cursor()

    try:
        cursor.execute('INSERT INTO users (user_id) VALUES (?)', (user_id,))
        logger.info (f'+++++ CREATED record {user_id}: {cursor.lastrowid} +++++')
    except sqlite3.IntegrityError:
        logger.info("+++++ FOUND record... UPDATING... +++++")

    # sql command to UPDATE an existing record
    update_command = f"UPDATE users SET {column} = ? WHERE user_id = ?"
    update_args = (value, user_id)

    cursor.execute(update_command, update_args)
    logger.info (f'+++++ UPDATED record {user_id}: {column} >> {value} +++++')

    # commit changes to db
    connection.commit()
    # close connection
    connection.close()
