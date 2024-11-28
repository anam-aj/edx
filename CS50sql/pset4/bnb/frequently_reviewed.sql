CREATE VIEW frequently_reviewed AS
SELECT id, property_type, host_name, accomodates, date
FROM listings
JOIN availabilities ON listings.id = avialabilities.listing_id
WHERE available = 1;
