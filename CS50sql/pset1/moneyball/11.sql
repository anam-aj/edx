SELECT *
FROM players
JOIN salaries ON players.id = salaries.player_id

ORDER BY year
limit 1
