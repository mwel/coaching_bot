# connect to the coachingBot_DB and check, if the user table already exists. If not, create it.
import sqlite3


def insert_update (user_id, first_name, last_name, gender, photo, birthdate, email, phone, longitude, latitude, bio, state):
    # connect to db
    connection = sqlite3.connect("coachingBotDB.db")

    # cursor
    cursor = connection.cursor()

    # sql command to INSERT a new record into the db
    insert_command = 'INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    insert_args = (
        user_id,
        first_name,
        last_name,
        gender,
        photo,
        birthdate,
        email,
        phone,
        longitude,
        latitude,
        bio,
        state,
        )

    # sql command to UPDATE an existing record
    update_command = """UPDATE users SET
        first_name = ?,
        last_name = ?,
        gender = ?,
        photo = ?,
        birthdate = ?,
        email = ?,
        phone = ?,
        longitude = ?,
        latitude = ?,
        bio = ?,
        state = ?
        WHERE user_id = ?
        """
    update_args = (
            first_name,
            last_name,
            gender,
            photo,
            birthdate,
            email,
            phone,
            longitude,
            latitude,
            bio,
            state,
            user_id
            )


    #if record exists, UPDATE it. Else, INSERT.
    # sql command to check, if user exists
    user_check = f'SELECT EXISTS (SELECT 1 FROM users WHERE user_id={user_id})' # will return a sqlite3.Cursor object

    cursor.execute(user_check)

    if cursor.fetchone():
        print("+++++ FOUND record +++++")
        cursor.execute(update_command, update_args)
        print (f'+++++ UPDATED RECORD {user_id}: {first_name} {last_name} +++++')

    else:
        print("+++++ NOT FOUND record +++++")
        cursor.execute(insert_command, insert_args)
        print (f'+++++ INSERTED RECORD {user_id}: {first_name} {last_name} +++++')


    #commit changes to db
    connection.commit()
    
    # close connection
    connection.close()
    