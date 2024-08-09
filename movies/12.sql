-- Select title
SELECT title
FROM movies
WHERE id IN
    (
    -- Select movie IDs
    SELECT movie_id
    FROM stars
    GROUP by movie_id
    HAVING COUNT(
        -- Select person ID
            person_id = (
            SELECT id
            FROM people
            WHERE name = 'Bradley Cooper'
            ) = 1
        )

        AND COUNT(
            -- Select person ID
            person_id = (
            SELECT id
            FROM people
            WHERE name = 'Bradley Cooper'
            ) = 1
    )
