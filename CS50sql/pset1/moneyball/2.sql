SELECT year, salary
FROM salaries
WHERE player_id = (
    SELECT id, fr
    FROM players
    WHERE first_name LIKE 'Cal%'
    AND last_name LIKE '%Ripken Jr.'
)
