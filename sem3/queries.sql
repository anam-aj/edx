-- 1. Retrieve full name, all phone numbers, and all email addresses of a
-- contact with a specific Contact_ID
SELECT
    c.First_Name,
    c.Last_Name,
    p.Phone_Type,
    p.Phone_Number,
    e.Email_Type,
    e.Email_Address
FROM Contacts c
LEFT JOIN Phone_Numbers p ON c.Contact_ID = p.Contact_ID
LEFT JOIN Emails e ON c.Contact_ID = e.Contact_ID
WHERE c.Contact_ID = 101;  -- Replace 101 with desired Contact_ID



--2. List all contacts (First Name and Last Name) belonging to the 'Work' category
SELECT DISTINCT c.First_Name, c.Last_Name
FROM Contacts c
LEFT JOIN Phone_Numbers p ON c.Contact_ID = p.Contact_ID
LEFT JOIN Emails e ON c.Contact_ID = e.Contact_ID
LEFT JOIN Addresses a ON c.Contact_ID = a.Contact_ID
WHERE p.Phone_Type = 'Work'
   OR e.Email_Type = 'Work'
   OR a.Address_Type = 'Work';



-- 3. Find the Contact_ID and First_Name of all contacts who have a 'Mobile' phone number
SELECT DISTINCT c.Contact_ID, c.First_Name
FROM Contacts c
INNER JOIN Phone_Numbers p ON c.Contact_ID = p.Contact_ID
WHERE p.Phone_Type = 'Mobile';



-- 4. Count the total number of contacts in each category
SELECT 'Phone' AS Category, COUNT(DISTINCT Contact_ID) AS Total FROM Phone_Numbers
UNION ALL
SELECT 'Email', COUNT(DISTINCT Contact_ID) FROM Emails
UNION ALL
SELECT 'Address', COUNT(DISTINCT Contact_ID) FROM Addresses;



-- 5. List the names of contacts who have more than one phone number registered
SELECT c.First_Name, c.Last_Name
FROM Contacts c
INNER JOIN Phone_Numbers p ON c.Contact_ID = p.Contact_ID
GROUP BY c.Contact_ID, c.First_Name, c.Last_Name
HAVING COUNT(p.Phone_ID) > 1;
