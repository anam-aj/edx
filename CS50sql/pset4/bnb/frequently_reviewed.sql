CREATE VIEW frequently_reviewed AS
SELECT listings.id AS id, property_type, host_name, date
FROM listings
JOIN reviews ON listings.id = reviews.listing_id
WHERE available = 1;
