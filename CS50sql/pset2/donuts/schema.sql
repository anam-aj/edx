CREATE TABLE ingredients (
    id INTEGER,
    name TEXT NOT NULL UNIQUE,
    last_name TEXT NOT NULL,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    PRIMARY KEY(id)
);
