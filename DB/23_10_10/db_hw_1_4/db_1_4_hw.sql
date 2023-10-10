CREATE TABLE users(
    email VARCHAR(50) NOT NULL UNIQUE,
    name VARCHAR(50) NOT NULL,
    age INTEGER NOT NULL,
    phoneNumber INTEGER NOT NULL,
    gender INTEGER NOT NULL,
    address VARCHAR(50) NOT NULL DEFAULT 'no address'
);

PRAGMA table_info('users')

ALTER TABLE
    users
RENAME COLUMN
    phoneNumber TO number;

DROP TABLE users;