SELECT year, salary
FROM salaries
WHERE player_id = (
    SELECT id, first_name, last_name
    FROM players
    WHERE first_name LIKE 'Cal%'
    AND last_name LIKE '%Ripken Jr.'
)
