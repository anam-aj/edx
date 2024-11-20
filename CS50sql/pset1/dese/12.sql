SELECT name, per_pupil_expenditure, exemplary
FROM districts
JOIN expenditures ON districts.id = expenditures.district_id
JOIN expenditures ON schools.district_id = expenditures.district_id
ORDER BY per_pupil_expenditure DESC, name
