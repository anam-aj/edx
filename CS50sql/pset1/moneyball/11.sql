SELECT *
FROM players
JOIN salaries ON players.id = salaries.player_id
JOIN performances ON players.id = performances.player_id
ORDER BY players.id
limit 10
