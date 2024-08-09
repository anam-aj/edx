-- Select name
SELECT name
FROM people
WHERE id IN(
    -- Select person IDs
    SELECT person_id
    FROM stars
    WHERE movie_id
    HAVING SUM(
        person_id = (
            -- Select person ID
            SELECT id
            FROM people
            WHERE name = 'Bradley Cooper'
        )
    )
)

