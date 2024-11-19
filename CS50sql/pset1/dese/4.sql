SELECT city, count("name") AS "Number of Schools"
FROM schools
GROUP BY city

