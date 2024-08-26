CREATE TABLE transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_id integer,
    symbol TEXT,
    shares INTEGER,
    rate FLOAT,
    total FLOAT,
    method TEXT,
    date_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE INDEX userid ON transactions (user_id)
