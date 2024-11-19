SELECT name
FROM schools
JOIN graduation rates ON schools.id = 

SELECT name, per_pupil_expenditure
FROM districts
JOIN expenditures ON districts.id = expenditures.district_id
ORDER BY per_pupil_expenditure DESC
LIMIT 10
