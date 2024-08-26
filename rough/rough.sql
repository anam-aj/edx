CREATE TABLE transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_id integer,
    symbol TEXT,
    shares INTEGER,
    rate FLOAT,
    total FLOAT,
    method TEXT,
    date_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
