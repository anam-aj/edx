--SELECT count(title)
--FROM movies JOIN ratings
--ON movies.id = ratings.movie_id
--WHERE rating = 10.0;

SELECT count(title)
FROM movies
WHERE rating = (
    select rating
    from ratings
    where rating = 10
);

