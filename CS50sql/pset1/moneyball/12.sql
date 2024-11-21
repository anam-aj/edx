
    SELECT first_name, last_name
    FROM players
    JOIN salaries ON players.id = salaries.player_id
    JOIN performances ON players.id = performances.player_id
    WHERE salaries.year = performances.year
    AND salaries.year = 2001
    AND H > 0
    AND salary >= 0
    ORDER BY ("salary" / "H"), first_name, last_name
    LIMIT 10
    INTERSECT
    SELECT first_name, last_name, ("salary" / "RBI") AS "RBI per hit"
    FROM players
    JOIN salaries ON players.id = salaries.player_id
    JOIN performances ON players.id = performances.player_id
    WHERE salaries.year = performances.year
    AND salaries.year = 2001
    AND H > 0
    AND salary >= 0
    ORDER BY "dollars per hit", first_name, last_name
    LIMIT 10




