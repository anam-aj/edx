-- Select title
SELECT (title)
FROM movies
WHERE id IN
    (
    -- Select movie IDs
    SELECT movie_id
    FROM stars
    WHERE person_id =
        (
        SELECT 
        )
    )
limit 20;
