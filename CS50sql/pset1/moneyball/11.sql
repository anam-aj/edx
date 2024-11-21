SELECT *
FROM players
JOIN salaries ON players.id = salaries.player_id

ORDER BY players.id
limit 10
