CREATE TABLE users (
    id INTEGER,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE schools (
    id INTEGER,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    address TEXT NOT NULL,
    year TEXT NOT NULL,
    PRIMARY KEY(id),
);

CREATE TABLE airlines (
    id INTEGER,
    name TEXT NOT NULL,
    concourse TEXT NOT NULL CHECK(concourse IN ('A', 'B', 'C', 'D', 'E', 'F', 'T')),
    PRIMARY KEY(id)
);

CREATE TABLE flights (
    id INTEGER,
    flight_number INTEGER NOT NULL,
    airline_id INTEGER,
    departure_airport_code TEXT NOT NULL,
    arrival_airport_code TEXT NOT NULL,
    departure_date_time DATETIME NOT NULL,
    arrival_date_time DATETIME NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(airline_id) REFERENCES airlines(id)
);
