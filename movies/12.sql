-- Select title
SELECT (title)
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
        WHERE name = 'Jennifer Lawrence'
        )
        AND
        (
        -- Select person ID
        SELECT id
        FROM people
        WHERE name = 'Bradley Cooper'
        )
    );

    select movie_id from stars where person_id = (459029) and (681726);
