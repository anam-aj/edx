SELECT city, count("name") AS "Number of Schools"
FROM schools
GROUP BY city
WHERE "Number of Schools" < 4
ORDER BY "Number of Schools" DESC, city
LIMIT 10
