
-- *** The Lost Letter ***

-- Get ID of sender's address
SELECT id
FROM addresses
WHERE address = '900 Somerville Avenue'

--
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
    WHERE address LIKE '%2%Finnegan%Street%uptown%'
)


-- *** The Devious Delivery ***

-- *** The Forgotten Gift ***

