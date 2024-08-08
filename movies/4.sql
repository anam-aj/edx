--SELECT count(title)
--FROM movies JOIN ratings
--ON movies.id = ratings.movie_id
--WHERE rating = 10.0;

SELECT (title)
FROM movies
WHERE id = (
    select movie_id
    from ratings
    where rating = 10
);

