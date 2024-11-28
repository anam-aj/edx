CREATE VIEW available AS
SELECT listings.id AS id, property_type, host_name, date
FROM listings
JOIN availabilities ON listings.id = avialabilities.listing_id
WHERE available = 1;
