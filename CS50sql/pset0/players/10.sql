SELECT height AS "Top 10 Tallest Players after 2000"
FROM players
WHERE debut > 2000-01-01
ORDER BY height
LIMIT 10;
