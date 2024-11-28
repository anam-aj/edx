CREATE VIEW june_vacancies AS
SELECT listings.id AS id, property_type, host_name, COUNT(available)
FROM listings
JOIN availabilities ON listings.id = availabilities.listing_id
WHERE available = 1;
