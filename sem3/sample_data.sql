-- Contacts
INSERT INTO Contacts (Contact_ID, First_Name, Last_Name) VALUES
(1, 'John', 'Doe'),
(2, 'Alice', 'Smith'),
(3, 'Bob', 'Johnson');

-- Phone_Numbers
INSERT INTO Phone_Numbers (Phone_ID, Contact_ID, Phone_Type, Phone_Number) VALUES
(1, 1, 'Mobile', '9876543210'),
(2, 1, 'Home', '0123456789'),
(3, 2, 'Work', '9998887776'),
(4, 3, 'Mobile', '8887776665'),
(5, 3, 'Work', '7776665554');

-- Emails
INSERT INTO Emails (Email_ID, Contact_ID, Email_Type, Email_Address) VALUES
(1, 1, 'Personal', 'john.doe@example.com'),
(2, 1, 'Work', 'j.doe@company.com'),
(3, 2, 'Work', 'alice.smith@work.com'),
(4, 3, 'Personal', 'bob.johnson@mail.com');

-- Addresses
INSERT INTO Addresses (Address_ID, Contact_ID, Address_Type, Street, City, State, Zip, Country) VALUES
(1, 1, 'Home', '123 Elm St', 'New York', 'NY', '10001', 'USA'),
(2, 2, 'Work', '456 Oak Rd', 'Boston', 'MA', '02110', 'USA'),
(3, 3, 'Home', '789 Pine Ln', 'Chicago', 'IL', '60601', 'USA');
