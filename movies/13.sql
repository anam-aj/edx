-- Select name
SELECT title
FROM movies
WHERE id IN(
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

