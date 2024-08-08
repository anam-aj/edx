SELECT title
FROM movies JOIN ratings
ON 
WHERE id = (
    SELECT movie_id
    FROM ratings
    WHERE rating = 10
);
