
-- *** The Lost Letter ***

-- Get ID of sender's address
SELECT id
FROM addresses
WHERE address = '900 Somerville Avenue'
/*
+-----+
| id  |
+-----+
| 432 |
+-----+
*/

-- Get ID of receiver's address
SELECT id
FROM addresses
WHERE address LIKE '%2%Finnegan%Street%uptown%'
-- Not Found

-- Find details of package corresponding sender's address
SELECT *
FROM packages
WHERE from_address_id = (
    SELECT id
    FROM addresses
    WHERE address = '900 Somerville Avenue'
)
-- | 384  | Congratulatory letter | 432             | 854

-- Get address with id 854




-- *** The Devious Delivery ***

-- *** The Forgotten Gift ***

