SELECT title
FROM movies
WHERE id = (
    SELECT movie_id
    WHERE rating = 10.0
)
limit 100;
