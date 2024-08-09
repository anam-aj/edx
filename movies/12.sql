-- Select title
SELECT title
FROM movies
WHERE id IN
    (
    -- Select movie IDs
    SELECT movie_id
    FROM stars
    GROUP by movie_id
    HAVING SUM(
        -- Select person ID
            person_id = (
            SELECT id
            FROM people
            WHERE name = 'Bradley Cooper'
            )) > 0

        AND SUM(
            -- Select person ID
            person_id = (
            SELECT id
            FROM people
            WHERE name = 'Jennifer Lawrence'
            )) > 0
    );
