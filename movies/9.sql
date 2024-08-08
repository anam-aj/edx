-- Select names
SELECT name
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
        WHERE year = 'Toy Story'
        )
    );
