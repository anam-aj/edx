SELECT city, count("name")
FROM schools
GROUP BY city
