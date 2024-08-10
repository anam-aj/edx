-- Keep a log of any SQL queries you execute as you solve the mystery.

--  To get the contents of database
.schema

-- Get the structure of table crime_scene_report
SELECT * FROM crime_scene_reports LIMIT 5;

--  Get the reports of the the day of theft
SELECT * FROM crime_scene_reports WHERE (year = 2023 AND month = 7 AND day = 28);
-- Theft time = 10:15, 3 witness interview, all mention bakery

-- Get the structure of table interviews
SELECT * FROM interviews limit 5;

--  Get the interviwes of the the day of theft
SELECT * FROM interviews WHERE (year = 2023 AND month = 7 AND day = 28 AND transcript LIKE '%bakery%');
-- 1st witness : theif left within 10 mins by caar from parking lot
-- 2nd witness : earlier in the morning thief withdrew money from ATM on Leggett Street
-- 3rd witness : thief called someone on phone, asked him to purchase ticket for first flight next day out of fiftyville

-- Get the structure of table bakery_security_logs
SELECT * FROM bakery_security_logs limit 5;

--  Get the security log of the cars exited parking lot around the time of theft
SELECT * FROM bakery_security_logs WHERE (year = 2023 AND month = 7 AND day = 28 AND hour = 10 AND minute <=30 AND activity = 'exit');
-- Licence plate of the cars exited from from from 10:00 to 10:30 are
-- 5P2BI95, 94KL13X, 6P58WS2, 4328GD8, G412CB7, L93JTIZ, 322W7JE, 0NTHK55

-- Get the structure of table atm_transactions
SELECT * FROM atm_transactions limit 5;

-- Get ATM transaction on the morning of the theft day
SELECT * FROM atm_transactions WHERE (year = 2023 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street');
