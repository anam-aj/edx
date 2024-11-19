SELECT name
FROM districts
JOIN expenditures ON districts.id = expenditures.district_id
WHERE pupils = MIN("pupils")

/*IN (
    SELECT MIN("pupils")
    FROM expenditures
)
