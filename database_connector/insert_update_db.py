# connect to the coachingBot_DB and check, if the user table already exists. If not, create it.
import sqlite3


def insert_update (user_id, first_name, last_name, gender, photo, birthdate, email, phone, longitude, latitude, bio):
    # connect to db
    connection = sqlite3.connect("coachingBotDB.db")
    print("+++++ Connected to coachingBotDB. +++++")

    # cursor
    cursor = connection.cursor()
    print("+++++ Cursor created. +++++")

    
    # sql command to INSERT a new record into the db
    # c.execute("INSERT INTO test VALUES (?, 'bar')", (testfield,))
    # insert_command = 'INSERT INTO users VALUES (user_id, first_name, last_name, gender, photo, birthdate, email, phone, longitude, latitude, bio)'
    insert_command = 'INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
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
        bio = ? 
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
            user_id)


    #if record exists, UPDATE it. Else, INSERT.
    # sql command to check, if user exists
    user_check = f'SELECT EXISTS (SELECT 1 FROM users WHERE user_id={user_id})'

    cursor.execute(user_check)

    if cursor.fetchone():
        print("+++++ Record Found! +++++")
        cursor.execute(update_command, update_args)
        print (f'UPDATED record {user_id}: {first_name} {last_name}')

    else:
        print("+++++ No record found +++++")
        cursor.execute(insert_command, insert_args)
        print (f'INSERTED record {user_id}: {first_name} {last_name}')


    #commit changes to db			
    connection.commit()
    print('+++++ COMMITTED changes to DB. +++++')  

    # close connection
    connection.close()
    print ('+++++ CLOSED connection to DB. +++++')

