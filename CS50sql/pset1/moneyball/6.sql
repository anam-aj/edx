SELECT name, SUM(H) AS total hits
FROM teams
JOIN performances on teams.id = performances.team_id

