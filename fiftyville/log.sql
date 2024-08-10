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
-- 3rd witness : thief called someone on phone for less than a minute,
--               asked him to purchase ticket for first flight next day out of fiftyville

-- Get the structure of table bakery_security_logs
SELECT * FROM bakery_security_logs limit 5;

--  Get the security log of the cars exited parking lot around the time of theft
SELECT * FROM bakery_security_logs WHERE (year = 2023 AND month = 7 AND day = 28 AND hour = 10 AND minute <=30 AND activity = 'exit');
-- Licence plate of the cars exited from from from 10:00 to 10:30 are
-- 5P2BI95, 94KL13X, 6P58WS2, 4328GD8, G412CB7, L93JTIZ, 322W7JE, 0NTHK55

-- Get the structure of table atm_transactions
SELECT * FROM atm_transactions limit 5;

-- Get ATM transaction from ATM on Leggett Street on the morning of the theft day
SELECT * FROM atm_transactions WHERE (year = 2023 AND month = 7 AND day = 28 AND transaction_type = 'withdraw' AND atm_location = 'Leggett Street');
/*
+----------------+--------+
| account_number | amount |
+----------------+--------+
| 28500762       | 48     |
| 28296815       | 20     |
| 76054385       | 60     |
| 49610011       | 50     |
| 16153065       | 80     |
| 25506511       | 20     |
| 81061156       | 30     |
| 26013199       | 35     |
+----------------+--------+
*/

-- GET person_id who made withdrawls on theft day morning from leggett street ATM
SELECT person_id
FROM bank_accounts
WHERE account_number IN (
    SELECT account_number
    FROM atm_transactions
    WHERE (
        year = 2023
        AND month = 7
        AND day = 28
        AND transaction_type = 'withdraw'
        AND atm_location = 'Leggett Street'
    )
)

-- Get the structure of table phone_calls
SELECT * FROM phone_calls limit 5;

--  Get the call details on the the day of theft
SELECT * FROM phone_calls WHERE (year = 2023 AND month = 7 AND day = 28 AND duration < 60);
/*
+----------------+----------------+
|     caller     |    receiver    |
+----------------+----------------+
| (130) 555-0289 | (996) 555-8899 |
| (499) 555-9472 | (892) 555-8872 |
| (367) 555-5533 | (375) 555-8161 |
| (499) 555-9472 | (717) 555-1342 |
| (286) 555-6063 | (676) 555-6554 |
| (770) 555-1861 | (725) 555-3243 |
| (031) 555-6622 | (910) 555-3251 |
| (826) 555-1652 | (066) 555-9701 |
| (338) 555-6650 | (704) 555-2131 |
+----------------+----------------+
*/
-- Get details of airport
SELECT * FROM airports WHERE city LIKE '%Fiftyville%';

-- Get flights departuring from fiftyville on next day
SELECT * FROM flights WHERE (year = 2023 AND month = 7 AND day = 29 AND origin_airport_id = 8);




SELECT *
FROM people
WHERE license_plate IN (
    SELECT license_plate
    FROM bakery_security_logs
    WHERE (
        year = 2023
        AND month = 7
        AND day = 28
        AND hour = 10
        AND minute <=30
        AND activity = 'exit'
    )
)
AND
phone_number IN (
    SELECT caller
    FROM phone_calls
    WHERE (
        year = 2023
        AND month = 7
        AND day = 28
        AND duration < 60
    )
)
AND
passport_number IN (
    SELECT passport_number
    FROM passengers
    WHERE flight_id IN (
        SELECT id
        FROM flights
        WHERE (
            year = 2023
            AND month = 7
            AND day = 29
            AND origin_airport_id = 8
        )
    )
)
AND
id IN (
    SELECT person_id
    FROM bank_accounts
    WHERE account_number IN (
        SELECT account_number
        FROM atm_transactions
        WHERE (
            year = 2023
            AND month = 7
            AND day = 28
            AND transaction_type = 'withdraw'
            AND atm_location = 'Leggett Street'
        )
    )
);


SELECT *
FROM people
WHERE passport_number IN (
    SELECT passport_number
    FROM passengers
    WHERE flight_id IN (
        SELECT id
        FROM flights
        WHERE (
            year = 2023
            AND month = 7
            AND day = 29
            AND origin_airport_id = 8
        )
    )
)


SELECT phone_number
FROM people
limit 2
