CREATE TABLE users (
    id INT UNSIGNED AUTO_INCREMENT,
    first_name VARCHAR(64) NOT NULL,
    last_name VARCHAR(64) NOT NULL,
    username VARCHAR(64) UNIQUE NOT NULL,
    password VARCHAR(128) NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE schools (
    id INT UNSIGNED AUTO_INCREMENT,
    name VARCHAR(128) NOT NULL,
    type ENUM('Primary', 'Secondary', 'Higher Education') NOT NULL,
    address VARCHAR(256) NOT NULL,
    year YEAR NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE companies (
    id INT UNSIGNED AUTO_INCREMENT,
    name VARCHAR(128) NOT NULL,
    industry ENUM('Technology', 'Education', 'Business') NOT NULL,
    address VARCHAR(256) NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE user_user_connection (
    id INT UNSIGNED AUTO_INCREMENT,
    user_id_1 INT UNSIGNED,
    user_id_2 INT UNSIGNED,
    PRIMARY KEY(id),
    FOREIGN KEY(user_id_1) REFERENCES users(id),
    FOREIGN KEY(user_id_2) REFERENCES users(id)
);

CREATE TABLE user_school_connection (
    id INT UNSIGNED AUTO_INCREMENT,
    user_id INT UNSIGNED,
    school_id INT UNSIGNED,
    start_date DATE NOT NULL,
    end_date DATE DEFAULT NULL,
    degree VARCHAR(64) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(school_id) REFERENCES schools(id)
);

CREATE TABLE user_company_connection (
    id INT UNSIGNED AUTO_INCREMENT,
    user_id INT UNSIGNED,
    company_id INT UNSIGNED,
    start_date DATE NOT NULL,
    end_date DATE DEFAULT NULL,
    title VARCHAR(128) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(company_id) REFERENCES companies(id)
);
