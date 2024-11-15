SELECT height AS "Top 10 Tallest heights after 2000"
FROM players
WHERE height IS NOT NULL
    AND debut > 2000-01-01
ORDER BY height DESC
LIMIT 10;
