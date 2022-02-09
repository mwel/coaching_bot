"""connect to the coachingBot_DB and check, if the user table already exists. If not, create it."""

# imports 
import sqlite3
from logEnabler import logger


from handler_functions.database_connector.create_db import create_db


def insert_update (user_id, time_stamp, first_name, last_name, gender, photo, birthdate, email, telephone, longitude, latitude, bio, state, mail_sent, appointment, event):
    
    # create db if non-existent
    # TODO: nice-to-have: use if clause to check table existence and only on fail try to create
    create_db()
    
    # connect to db
    connection = sqlite3.connect("coachingBotDB.db")

    # cursor
    cursor = connection.cursor()

    # sql command to INSERT a new record into the db
    insert_command = 'INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    insert_args = (
        user_id,
        time_stamp,
        first_name,
        last_name,
        gender,
        photo,
        birthdate,
        email,
        telephone,
        longitude,
        latitude,
        bio,
        state,
        mail_sent,
        appointment,
        event
        )

    # sql command to UPDATE an existing record
    update_command = """UPDATE users SET
        first_name = ?,
        last_name = ?,
        gender = ?,
        photo = ?,
        birthdate = ?,
        email = ?,
        telephone = ?,
        longitude = ?,
        latitude = ?,
        bio = ?,
        state = ?
        mail_sent = ?
        appointment = ?
        event = ?
        WHERE user_id = ?
        """
    update_args = (
        first_name,
        last_name,
        gender,
        photo,
        birthdate,
        email,
        telephone,
        longitude,
        latitude,
        bio,
        state,
        mail_sent,
        appointment,
        event,
        user_id
        )


    #if record exists, UPDATE it. Else, INSERT.
    # sql command to check, if user exists
    user_check = f'SELECT EXISTS (SELECT 1 FROM users WHERE user_id={user_id})' # will return a sqlite3.Cursor object

    cursor.execute(user_check)

    if cursor.fetchone():
        logger.info("+++++ FOUND record +++++")
        cursor.execute(update_command, update_args)
        logger.info (f'+++++ UPDATED RECORD {user_id}: {first_name} {last_name} +++++')

    else:
        logger.info("+++++ NOT FOUND record +++++")
        cursor.execute(insert_command, insert_args)
        logger.info (f'+++++ INSERTED RECORD {user_id}: {first_name} {last_name} +++++')


    #commit changes to db
    connection.commit()
    
    # close connection
    connection.close()
    