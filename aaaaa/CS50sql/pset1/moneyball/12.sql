SELECT first_name, last_name
FROM (
    SELECT *
    FROM (
        SELECT first_name, last_name, players.id
        FROM players
        JOIN salaries ON players.id = salaries.player_id
        JOIN performances ON players.id = performances.player_id
        WHERE salaries.year = performances.year
        AND salaries.year = 2001
        AND H > 0
        AND salary >= 0
        ORDER BY ("salary" / "H")
        LIMIT 10
    )

    INTERSECT

    SELECT *
    FROM (
        SELECT first_name, last_name, players.id
        FROM players
        JOIN salaries ON players.id = salaries.player_id
        JOIN performances ON players.id = performances.player_id
        WHERE salaries.year = performances.year
        AND salaries.year = 2001
        AND RBI > 0
        AND salary >= 0
        ORDER BY ("salary" / "RBI")
        LIMIT 10
    )
)

ORDER BY id
