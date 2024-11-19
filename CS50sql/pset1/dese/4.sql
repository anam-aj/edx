SELECT city, count("name") AS "Number of Schools"
FROM schools
GROUP BY city
ORDER BY "Number of Schools" DESC, name
LIMIT 10
