-- 1. Create the database
--    sqlite3 Contact.db;

-- 3. Create Contacts table
CREATE TABLE Contacts (
    Contact_ID INT PRIMARY KEY,
    First_Name VARCHAR(50),
    Last_Name VARCHAR(50)
);

-- 4. Create Phone_Numbers table
CREATE TABLE Phone_Numbers (
    Phone_ID INT PRIMARY KEY,
    Contact_ID INT,
    Phone_Type VARCHAR(20),
    Phone_Number VARCHAR(20),
    FOREIGN KEY (Contact_ID) REFERENCES Contacts(Contact_ID)
);

-- 5. Create Emails table
CREATE TABLE Emails (
    Email_ID INT PRIMARY KEY,
    Contact_ID INT,
    Email_Type VARCHAR(20),
    Email_Address VARCHAR(100),
    FOREIGN KEY (Contact_ID) REFERENCES Contacts(Contact_ID)
);

-- 6. Create Addresses table
CREATE TABLE Addresses (
    Address_ID INT PRIMARY KEY,
    Contact_ID INT,
    Address_Type VARCHAR(20),
    Street VARCHAR(100),
    City VARCHAR(50),
    State VARCHAR(50),
    Zip VARCHAR(10),
    Country VARCHAR(50),
    FOREIGN KEY (Contact_ID) REFERENCES Contacts(Contact_ID)
);
