SELECT name, SUM(H) AS "total hits"
FROM teams
JOIN performances on teams.id = performances.team_id
GROUP BY name
WHERE performances.year = 2001
ORDER BY "total hits" DESC
LIMIT 5
