CREATE TABLE passengers (
    id INTEGER
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    PRIMARY KEY(id)
);


CREATE TABLE check_in (
    id INTEGER
    passenger_id INTEGER,
    flight_id INTEGER,
    age INTEGER NOT NULL,
    PRIMARY KEY(id)
);
