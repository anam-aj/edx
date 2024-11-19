
-- *** The Lost Letter ***
SELECT id
FROM packages
WHERE from_address_id = (
    SELECT id
    FROM addresses
    WHERE address = '900 Somerville Avenue'
)


-- *** The Devious Delivery ***

-- *** The Forgotten Gift ***

