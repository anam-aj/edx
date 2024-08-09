-- Select title
SELECT (title)
FROM movies
WHERE movies.id IN
    (
    -- Select movie IDs
    SELECT movie_id
    FROM stars
    WHERE 
    )
limit 20;
