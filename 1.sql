SELECT *
FROM people
WHERE id IN (
    -- person_id of people made withdrawl on theft day marning from leggett street ATM
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
)
AND phone_number IN (
    -- Phone number of people who made a call of duration less than 1 min on theft day
    SELECT caller
    FROM phone_calls
    WHERE (
        year = 2023
        AND month = 7
        AND day = 28
        AND duration < 60
    )
)
AND license_plate IN (
    -- License plate of people that match with the security log of the cars
    -- exited parking lot around the time of theft
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
AND passport_number IN (
    -- Passport number of people who took the 1st flight next day out of town
    SELECT passport_number
    FROM passengers
    WHERE flight_id IN (
        SELECT id
        FROM flights
        WHERE (
            year = 2023
            AND month = 7
            AND day = 29
            AND id = 36
        )
    )
)
