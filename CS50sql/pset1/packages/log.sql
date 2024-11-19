
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
WHERE package_id = 5098
/*
+-------+-----------+------------+------------+--------+----------------------------+
|  id   | driver_id | package_id | address_id | action |         timestamp          |
+-------+-----------+------------+------------+--------+----------------------------+
| 30123 | 10        | 5098       | 50         | Pick   | 2023-10-24 08:40:16.246648 |
| 30140 | 10        | 5098       | 348        | Drop   | 2023-10-24 10:08:55.610754 |
+-------+-----------+------------+------------+--------+----------------------------+
*/

-- Get address details for id = 348
SELECT *
FROM addresses
WHERE id = 348
/*
+-----+------------------+----------------+
| id  |     address      |      type      |
+-----+------------------+----------------+
| 348 | 7 Humboldt Place | Police Station |
+-----+------------------+----------------+
*/


-- *** The Forgotten Gift ***

-- Get Details of sender's address
SELECT *
FROM addresses
WHERE address = '109 Tileston Street'
/*
+------+---------------------+-------------+
|  id  |       address       |    type     |
+------+---------------------+-------------+
| 9873 | 109 Tileston Street | Residential |
+------+---------------------+-------------+
*/

-- Find details of package corresponding sender's address
SELECT *
FROM packages
WHERE from_address_id = (
    SELECT id
    FROM addresses
    WHERE address = '109 Tileston Street'
)
/*
+------+----------+-----------------+---------------+
|  id  | contents | from_address_id | to_address_id |
+------+----------+-----------------+---------------+
| 9523 | Flowers  | 9873            | 4983          |
+------+----------+-----------------+---------------+
*/

-- Find scan details of package
SELECT *
FROM scans
WHERE package_id = 9523
/*
+-------+-----------+------------+------------+--------+----------------------------+
|  id   | driver_id | package_id | address_id | action |         timestamp          |
+-------+-----------+------------+------------+--------+----------------------------+
| 10432 | 11        | 9523       | 9873       | Pick   | 2023-08-16 21:41:43.219831 |
| 10500 | 11        | 9523       | 7432       | Drop   | 2023-08-17 03:31:36.856889 |
| 12432 | 17        | 9523       | 7432       | Pick   | 2023-08-23 19:41:47.913410 |
+-------+-----------+------------+------------+--------+----------------------------+
*/

-- Get driver's details
SELECT *
FROM drivers
WHERE id = 17
/*
+----+-------+
| id | name  |
+----+-------+
| 17 | Mikel |
+----+-------+
*/
