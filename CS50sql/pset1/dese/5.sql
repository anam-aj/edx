SELECT city, COUNT("name") AS "Number of Schools"
FROM schools
WHERE "Number of Schools" < 4
GROUP BY city
ORDER BY "Number of Schools" DESC, city
LIMIT 10
