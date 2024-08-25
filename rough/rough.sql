CREATE TABLE transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_name TEXT,
    FOREIGN KEY (user_name) REFERENCES users(username)
);
