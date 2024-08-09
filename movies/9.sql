-- Select names
SELECT name
FROM people
WHERE id IN (
    -- Select person IDs
    SELECT person_id
    FROM stars
    WHERE movie_id IN (
        -- Select movie IDs
        SELECT id
        FROM movies
        WHERE year = 2004
    )
)
ORDER BY birth;
