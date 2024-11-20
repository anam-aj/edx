SELECT year, salary
FROM salaries
WHERE player_id = (
    SELECT id
    FROM players
    WHERE 
)
