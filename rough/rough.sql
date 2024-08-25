CREATE TABLE transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_name INTEGER,
    FOREIGN KEY (user_name) REFERENCES users()

);
