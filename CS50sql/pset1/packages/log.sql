
-- *** The Lost Letter ***
SELECT id
FROM packages
WHERE from_address_id = (
    SELECT id
    FROM addresses
    WHERE address = '900 Somerville Avenue'
)
AND to_address_id = (
    SELECT id
    FROM addresses
    WHERE address = '2 Finnegan Street, uptown'
)


-- *** The Devious Delivery ***

-- *** The Forgotten Gift ***

