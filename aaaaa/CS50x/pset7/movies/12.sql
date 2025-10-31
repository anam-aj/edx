-- Select title
SELECT title
FROM movies
WHERE id IN (
    -- Select movie IDs
    SELECT movie_id
    FROM stars
    GROUP by movie_id
    HAVING SUM(
        person_id = (
            -- Select person ID
            SELECT id
            FROM people
            WHERE name = 'Bradley Cooper'
        )
    ) > 0

    AND
    SUM(
        person_id = (
            -- Select person ID
            SELECT id
            FROM people
            WHERE name = 'Jennifer Lawrence'
        )
    ) > 0
);
