-- Select title
SELECT title
FROM movies
JOIN stars s1 ON movies.id = s1.movie_id

JOIN stars s2 ON movies.id =
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
        WHERE name = 'Bradley Cooper'
        )
    )
