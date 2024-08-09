-- Select name
SELECT (name)
FROM people
WHERE id IN(
    -- Select person IDs
    SELECT person_id
    FROM stars
    WHERE movie_id IN(
        SELECT movie_id
        FROM stars
        WHERE person_id = (
            -- Select person ID
            SELECT id
            FROM people
            WHERE name = 'Kevin Bacon'
        )
    )
)
AND name != 'Kevin Bacon'
ORDER BY name;
