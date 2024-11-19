SELECT name, per_people_expenditure
FROM districts
JOIN expenditures ON districts.id = expenditures.district_id
ORDER BY per_people_expenditure DESC
LIMIT 10
