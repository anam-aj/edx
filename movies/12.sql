-- Select title
SELECT count(*)
FROM movies
WHERE id IN
    (
    -- Select movie IDs
    SELECT movie_id
    FROM stars
    WHERE person_id =
        (
        -- Select person ID
        SELECT id
        FROM people
        WHERE name = 'Lupu Pick'
        )
        AND
        (
        -- Select person ID
        SELECT id
        FROM people
        WHERE name = 'Rudolf Klein-Rhoden'
        )
    );
