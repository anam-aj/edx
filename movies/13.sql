-- Select name
SELECT name
FROM people
WHERE id IN(
    -- Select person IDs
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
    )
)

