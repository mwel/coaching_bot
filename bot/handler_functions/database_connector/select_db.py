""" SQL SELECT operations that will check, if a user exists or return a set of db records."""


# imports
import sqlite3
from logEnabler import logger


# check, if a record exists in the db and return a boolean
def user_search(user_id): # I'm sure there is a better solution for this, but this is mine.
    # connect to db
    connection = sqlite3.connect("coachingBotDB.db")
    # cursor
    cursor = connection.cursor()

    # sql command to check, if user exists
    user_check = f"""SELECT CASE WHEN EXISTS (
        SELECT *
        FROM users
        WHERE user_id = {user_id}
        )
        THEN CAST(1 AS BIT)
        ELSE CAST(0 AS BIT) END
        """

    cursor.execute(user_check)

    # get result from db, parse it as string, trim it and pase it as boolean
    result = bool(int((str(cursor.fetchone())).lstrip('(').rstrip(',)')))

    logger.info(f'+++++ RECORD REQUESTED for user_id: {user_id} +++++')
    if result == True:
        logger.info(f'+++++ RECORD FOUND +++++')
    else:
        logger.info(f'+++++ NO RECORD FOUND +++++')

    return result


# get all data available for one single user
def get_all_data(user_id):
    # connect to db
    connection = sqlite3.connect("coachingBotDB.db")
    # cursor
    cursor = connection.cursor()

    # SELECT all info from user with respective user_id
    selection = f"""SELECT *
        FROM users
        WHERE user_id = {user_id}
        """

    # fetch all data from table users
    logger.info(f'+++++ RECORD FOUND FOR: {user_id} +++++')
    cursor.execute(selection)

    # store all data from selection in table_data
    table_data = cursor.fetchall()


    # print table
    logger.info(f'+++++ RECORD REQUESTED for user_id: {user_id} +++++')
    for i in table_data:
        print(i)

    return table_data


# get all data available for one single user
def get_customers():
    # connect to db
    connection = sqlite3.connect("coachingBotDB.db")
    # cursor
    cursor = connection.cursor()

    # SELECT all info from user with respective user_id
    selection = f"""SELECT *
        FROM users
        """

    # fetch all data from table users
    cursor.execute(selection)

    # store all data from selection in table_data
    table_data = cursor.fetchall()

    # print table
    for i in table_data:
        print(i)

    return table_data


# get a specific value of a user
def get_value(user_id, column):
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
    table_value = (str(cursor.fetchone())).lstrip("('").rstrip("',)")

    # print value
    logger.info(f'+++++ RECORD REQUESTED for user_id: {user_id} +++++')
    logger.info(f'+++++ DB RESPONSE: {table_value} +++++')

    return table_value
