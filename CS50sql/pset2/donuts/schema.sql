CREATE TABLE ingredients (
    id INTEGER,
    name TEXT NOT NULL UNIQUE,
    rate NUMERIC NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE donuts (
    id INTEGER,
    name TEXT NOT NULL UNIQUE,
    gluten_free TEXT NOT NULL CHECK(gluten_free IN ('yes', 'no'))
    rate NUMERIC NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE customers (
    id INTEGER,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    PRIMARY KEY(id)
);


