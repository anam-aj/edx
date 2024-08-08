-- Select names
SELECT *
FROM people
WHERE id IN
    (
    -- Select person IDs
    SELECT person_id
    FROM stars
    WHERE movie_id IN
        (
        -- Select movie ID
        SELECT id
        FROM movies
        WHERE year = 2004
        )
    )
ORDER BY birth limit 10;
