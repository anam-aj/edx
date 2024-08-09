-- Select title
SELECT *
FROM movies
WHERE id =
    (
    -- Select movie IDs
    SELECT movie_id
    FROM stars
    WHERE person_id =
        (
        -- Select person ID
        SELECT id
        FROM people
        WHERE name = 'Rudolf Klein-Rhoden'
        )
        AND
        (
        -- Select person ID
        SELECT id
        FROM people
        WHERE name = 'Lupu Pick'
        )

    );
