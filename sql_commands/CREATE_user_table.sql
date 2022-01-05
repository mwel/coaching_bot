CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    gender TEXT,
    photo BLOB,
    birthdate INT,
    email TEXT UNIQUE,
    phone TEXT UNIQUE,
    longitude INT,
    latitude INT,
    bio TEXT NOT NULL
);