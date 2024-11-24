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
    PRIMARY KEY(id)
);

CREATE TABLE companies (
    id INTEGER,
    name TEXT NOT NULL,
    industry TEXT NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE user_user_connection (
    id INTEGER,
    user_id_1 INTEGER,
    user_id_2 INTEGER,
    PRIMARY KEY(id),
    FOREIGN KEY(user_id_1) REFERENCES users(id),
    FOREIGN KEY(user_id_2) REFERENCES users(id)
);

CREATE TABLE user_school_connection (
    id INTEGER,
    user_id INTEGER,
    school_id INTEGER,
    start_date NUMERIC NOT NULL,
    end_date NUMERIC,
    degree TEXT NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(school_id) REFERENCES schools(id)
);

CREATE TABLE user_company_connection (
    id INTEGER,
    user_id INTEGER,
    company_id INTEGER,
    start_date NUMERIC NOT NULL,
    end_date NUMERIC,
    title TEXT NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(company_id) REFERENCES companies(id)
);
