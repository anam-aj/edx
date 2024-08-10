-- Keep a log of any SQL queries you execute as you solve the mystery.

--  To get the contents of database
.schema

-- Get the structure of table crime_scene_report
SELECT * FROM crime_scene_reports LIMIT 5;

--  Get the reports of the the day of theft
SELECT * FROM crime_scene_reports WHERE (year = 2023 AND month = 7 AND day = 28);

-- Get the structure of table interviews
SELECT * FROM interviews limit 5;

--  Get the interviwes of the the day of theft
SELECT * FROM interviews WHERE (year = 2023 AND month = 7 AND day = 28 AND transcript LIKE '%bakery%');

-- Get the structure of table bakery_security_logs
SELECT * FROM bakery_security_logs limit 5;

--  Get the security log of the day of theft
SELECT * FROM bakery_security_logs WHERE (year = 2023 AND month = 7 AND day = 28 AND hour = 10 AND minute <=30 and );
