SELECT title
FROM movies
WHERE id = (
    SELECT movie_id
    FROM ratings
    WHERE rating = 10
)
limit 10000;
