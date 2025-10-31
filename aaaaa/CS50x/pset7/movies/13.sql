-- Select name of co-stars of Kevin Bacon
SELECT name
FROM people
WHERE id IN (
    -- Select co-stars' IDs
    SELECT person_id
    FROM stars
    WHERE movie_id IN (
        -- Select movies of Kevin Bacon
        SELECT movie_id
        FROM stars
        WHERE person_id = (
            -- Select Kevin's ID
            SELECT id
            FROM people
            WHERE (
                name = 'Kevin Bacon'
                AND birth = 1958
            )
        )
    )
)

AND name != 'Kevin Bacon'
ORDER BY name;
