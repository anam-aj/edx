SELECT count(title)
FROM movies
WHERE id IN
(
    select movie_id
    from ratings
    where rating = 10
);

