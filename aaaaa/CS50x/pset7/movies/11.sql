-- Select title
SELECT title
FROM movies
JOIN ratings ON movies.id = ratings.movie_id
WHERE id IN (
    -- Select movie IDs
    SELECT movie_id
    FROM stars
    WHERE person_id = (
        -- Select person ID
        SELECT id
        FROM people
        WHERE name = 'Chadwick Boseman'
    )
)
ORDER BY rating DESC
LIMIT 5;
