-- CREATION of user records and UPDATE queries to add more data to existing records

-- initial INSERT command for when a user data set is created
INSERT INTO users(user_id, first_name, last_name)
VALUES ('user_id%', 'first_name%', 'last_name%')


-- insetion of gender
UPDATE users
SET gender = 'gender%'
WHERE user_id = 'user_id%';


-- insetion of email
UPDATE users
SET photo = 'photo%'
WHERE user_id = 'user_id%';


-- insetion of birthdate
UPDATE users
SET birthdate = 'birthdate%'
WHERE user_id = 'user_id%';


-- insetion of email
UPDATE users
SET email = 'email%'
WHERE user_id = 'user_id%';


-- insetion of phone
UPDATE users
SET phone = 'phone%'
WHERE user_id = 'user_id%';


-- insetion of longitude, latitude (location)
UPDATE users
SET longitude = 'longitude%', latitude = 'latitude%'
WHERE user_id = 'user_id%';


-- insetion of bio
UPDATE users
SET bio = 'bio%'
WHERE user_id = 'user_id%';

