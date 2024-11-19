SELECT city, count(city) AS "Number of Schools"
FROM schools
GROUP BY city
ORDER BY "Number of Schools" DESC, city
LIMIT 10
