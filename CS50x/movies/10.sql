-- Select names
SELECT name
FROM people
WHERE id IN (
    -- Select person IDs
    SELECT person_id
    FROM directors
    WHERE movie_id IN (
        -- Select movie IDs
        SELECT movie_id
        FROM ratings
        WHERE rating >= 9.0
    )
);
