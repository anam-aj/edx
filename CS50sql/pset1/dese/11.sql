SELECT name, per_pupil_expenditure, graduated AS graduation_rate
FROM schools
JOIN graduation rates ON schools.id = graduation_rates.school_id
JOIN ependitures ON schools.district_id = expenditures.district_id
