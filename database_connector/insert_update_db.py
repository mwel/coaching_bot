# connect to the coachingBot_DB and check, if the user table already exists. If not, create it.
import sqlite3
from telegram import Update
from telegram.ext import CallbackContext


def insert_update (update: Update, user_id, first_name, last_name, gender, photo, birthdate, email, phone, longitude, latitude, bio):
    # connect to db
    connection = sqlite3.connect("coachingBotDB.db")
    print("+++++ Connected to coachingBotDB. +++++")

    # cursor
    cursor = connection.cursor()
    print("+++++ Cursor created. +++++")

    # sql command to check, if user exists
    user_check = f"""EXISTS (SELECT 1 FROM coachingBotDB.users WHERE user_id = {user_id}"""
    
    # sql command to INSERT a new record into the db
    insert_command = f"""INSERT INTO coachingBotDB.users (user_id, first_name, last_name, gender, photo, birthdate, email, phone, longitude, latitude, bio) 
            VALUES(
            {user_id},
            {first_name},
            {last_name},
            {gender},
            {photo},
            {birthdate},
            {email},
            {phone},
            {longitude},
            {latitude},
            {bio},
            )"""

    # sql command to UPDATE an existing record
    update_command = f"""UPDATE coachingBotDB.users SET 
        first_name = {first_name},
        last_name = {last_name},
        gender = {gender},
        photo = {photo},
        birthdate = {birthdate}, 
        email = {email},
        phone = {phone},
        longitude = {longitude}, 
        latitude = {latitude},
        bio = {bio} 
        WHERE user_id = {user_id}
        """


    #if record exists, UPDATE it. Else, INSERT.
    if cursor.execute(user_check):
        cursor.execute(update_command)
        print (f'UPDATED record {user_id}: {first_name} {last_name}')
    else:
        cursor.execute(insert_command)
        print (f'INSERTED record {user_id}: {first_name} {last_name}')


    #commit changes to db			
    connection.commit()
    print('+++++ COMMITTED changes to DB. +++++')  

    # close connection
    connection.close()
    print ('+++++ CLOSED connection to DB. +++++')

