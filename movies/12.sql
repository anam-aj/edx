-- Select title
SELECT (title)
FROM movies
WHERE movies.id IN
    (
    -- Select movie IDs
    SELECT movie_id
    FROM stars
    WHERE ((stars.person_id = (2225369 and 177896)))
    )
limit 20;
