SELECT first_name, last_name, salary, HR, salaries.year AS year
FROM players
JOIN salaries ON players.id = salaries.player_id
JOIN performances ON players.id = performances.player_id
