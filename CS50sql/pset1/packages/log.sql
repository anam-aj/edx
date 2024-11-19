
-- *** The Lost Letter ***

-- Get Details of sender's address
SELECT *
FROM addresses
WHERE address = '900 Somerville Avenue'
/*
+-----+-----------------------+-------------+
| id  |        address        |    type     |
+-----+-----------------------+-------------+
| 432 | 900 Somerville Avenue | Residential |
+-----+-----------------------+-------------+
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

-- Get address details with id 854
SELECT *
FROM addresses
WHERE id = 854
/*
+-----+-------------------+-------------+
| id  |      address      |    type     |
+-----+-------------------+-------------+
| 854 | 2 Finnigan Street | Residential |
+-----+-------------------+-------------+
*/

-- Get scan of the package
SELECT *
FROM scans
WHERE package_id = 384
/*
+----+-----------+------------+------------+--------+----------------------------+
| id | driver_id | package_id | address_id | action |         timestamp          |
+----+-----------+------------+------------+--------+----------------------------+
| 54 | 1         | 384        | 432        | Pick   | 2023-07-11 19:33:55.241794 |
| 94 | 1         | 384        | 854        | Drop   | 2023-07-11 23:07:04.432178 |
+----+-----------+------------+------------+--------+----------------------------+
*/


-- *** The Devious Delivery ***

-- Get details of packages without sender's address
SELECT *
FROM packages
WHERE from_address_id IS NULL
/*
+------+---------------+-----------------+---------------+
|  id  |   contents    | from_address_id | to_address_id |
+------+---------------+-----------------+---------------+
| 5098 | Duck debugger | NULL            | 50            |
+------+---------------+-----------------+---------------+
*/

-- Get address details corresponding to id = 50
SELECT *
FROM addresses
WHERE id = 50
/*
+----+-------------------+-------------+
| id |      address      |    type     |
+----+-------------------+-------------+
| 50 | 123 Sesame Street | Residential |
+----+-------------------+-------------+
*/

-- Get scan details of package
SELECT *
FROM scans
WHERE 


-- *** The Forgotten Gift ***

