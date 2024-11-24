CREATE TABLE ingredients (
    id INTEGER,
    name TEXT NOT NULL UNIQUE,
    rate NUMERIC NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE donuts (
    id INTEGER,
    name TEXT NOT NULL UNIQUE,
    rate NUMERIC NOT NULL,
    PRIMARY KEY(id)
);
