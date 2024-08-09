
    select *
    from (
    SELECT *
    FROM stars
    WHERE person_id =
        (
        -- Select person ID
        SELECT id
        FROM people
        WHERE name = 'Bradley Cooper'
        ))

    join

    (
    SELECT *
    FROM stars
    WHERE person_id =
        (
        -- Select person ID
        SELECT id
        FROM people
        WHERE name = 'Bradley Cooper'
        ))
    
