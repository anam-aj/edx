-- Keep a log of any SQL queries you execute as you solve the mystery.

--  To get the contents of database
.schema

-- Get the structure of table crime_scene_report
SELECT * FROM crime_scene_reports LIMIT 5;

--  Get the reports of the the day of theft
SELECT * FROM crime_scene_reports WHERE (year = 2023 AND month = 7 AND day = 28);

/*
| 295 | 2023 | 7     | 28  |
Humphrey Street Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery.
*/


-- Get the structure of table interviews
SELECT * FROM interviews limit 5;

--  Get the interviwes of the the day of theft
SELECT * FROM interviews WHERE (year = 2023 AND month = 7 AND day = 28 AND transcript LIKE '%bakery%');

/*
| 161 | Ruth    | 2023 | 7     | 28  |
Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away.
If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.                                                          |

| 162 | Eugene  | 2023 | 7     | 28  |
I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery,
I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.
                                                                                                |
| 163 | Raymond | 2023 | 7     | 28  |
As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call,
I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief
then asked the person on the other end of the phone to purchase the flight ticket.
*/


-- Get the structure of table bakery_security_logs
SELECT * FROM bakery_security_logs limit 5;

--  Get the security log of the cars exited parking lot around the time of theft
SELECT * FROM bakery_security_logs WHERE (year = 2023 AND month = 7 AND day = 28 AND hour = 10 AND minute <=30 AND activity = 'exit');
/*
+-----+------+-------+-----+------+--------+----------+---------------+
| id  | year | month | day | hour | minute | activity | license_plate |
+-----+------+-------+-----+------+--------+----------+---------------+
| 260 | 2023 | 7     | 28  | 10   | 16     | exit     | 5P2BI95       |
| 261 | 2023 | 7     | 28  | 10   | 18     | exit     | 94KL13X       |
| 262 | 2023 | 7     | 28  | 10   | 18     | exit     | 6P58WS2       |
| 263 | 2023 | 7     | 28  | 10   | 19     | exit     | 4328GD8       |
| 264 | 2023 | 7     | 28  | 10   | 20     | exit     | G412CB7       |
| 265 | 2023 | 7     | 28  | 10   | 21     | exit     | L93JTIZ       |
| 266 | 2023 | 7     | 28  | 10   | 23     | exit     | 322W7JE       |
| 267 | 2023 | 7     | 28  | 10   | 23     | exit     | 0NTHK55       |
+-----+------+-------+-----+------+--------+----------+---------------+
*/


-- Get the structure of table atm_transactions
SELECT * FROM atm_transactions limit 5;

-- Get ATM transaction from ATM on Leggett Street on the morning of the theft day
SELECT * FROM atm_transactions WHERE (year = 2023 AND month = 7 AND day = 28 AND transaction_type = 'withdraw' AND atm_location = 'Leggett Street');
/*
+-----+----------------+------+-------+-----+----------------+------------------+--------+
| id  | account_number | year | month | day |  atm_location  | transaction_type | amount |
+-----+----------------+------+-------+-----+----------------+------------------+--------+
| 246 | 28500762       | 2023 | 7     | 28  | Leggett Street | withdraw         | 48     |
| 264 | 28296815       | 2023 | 7     | 28  | Leggett Street | withdraw         | 20     |
| 266 | 76054385       | 2023 | 7     | 28  | Leggett Street | withdraw         | 60     |
| 267 | 49610011       | 2023 | 7     | 28  | Leggett Street | withdraw         | 50     |
| 269 | 16153065       | 2023 | 7     | 28  | Leggett Street | withdraw         | 80     |
| 288 | 25506511       | 2023 | 7     | 28  | Leggett Street | withdraw         | 20     |
| 313 | 81061156       | 2023 | 7     | 28  | Leggett Street | withdraw         | 30     |
| 336 | 26013199       | 2023 | 7     | 28  | Leggett Street | withdraw         | 35     |
+-----+----------------+------+-------+-----+----------------+------------------+--------+
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
/*
+-----------+
| person_id |
+-----------+
| 686048    |
| 514354    |
| 458378    |
| 395717    |
| 396669    |
| 467400    |
| 449774    |
| 438727    |
+-----------+
*/


-- Get the structure of table phone_calls
SELECT * FROM phone_calls limit 5;

--  Get the call details on the the day of theft
SELECT * FROM phone_calls WHERE (year = 2023 AND month = 7 AND day = 28 AND duration < 60);
/*
+-----+----------------+----------------+------+-------+-----+----------+
| id  |     caller     |    receiver    | year | month | day | duration |
+-----+----------------+----------------+------+-------+-----+----------+
| 221 | (130) 555-0289 | (996) 555-8899 | 2023 | 7     | 28  | 51       |
| 224 | (499) 555-9472 | (892) 555-8872 | 2023 | 7     | 28  | 36       |
| 233 | (367) 555-5533 | (375) 555-8161 | 2023 | 7     | 28  | 45       |
| 251 | (499) 555-9472 | (717) 555-1342 | 2023 | 7     | 28  | 50       |
| 254 | (286) 555-6063 | (676) 555-6554 | 2023 | 7     | 28  | 43       |
| 255 | (770) 555-1861 | (725) 555-3243 | 2023 | 7     | 28  | 49       |
| 261 | (031) 555-6622 | (910) 555-3251 | 2023 | 7     | 28  | 38       |
| 279 | (826) 555-1652 | (066) 555-9701 | 2023 | 7     | 28  | 55       |
| 281 | (338) 555-6650 | (704) 555-2131 | 2023 | 7     | 28  | 54       |
+-----+----------------+----------------+------+-------+-----+----------+
*/


-- Get details of airport
SELECT * FROM airports WHERE city LIKE '%Fiftyville%';
/*
+----+--------------+-----------------------------+------------+
| id | abbreviation |          full_name          |    city    |
+----+--------------+-----------------------------+------------+
| 8  | CSF          | Fiftyville Regional Airport | Fiftyville |
+----+--------------+-----------------------------+------------+
*/

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


SELECT *
FROM people
WHERE phone_number = '(375) 555-8161' or '(725) 555-3243'
