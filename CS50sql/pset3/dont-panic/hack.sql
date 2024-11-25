UPDATE users
SET password = (
    SELECT password
    FROM users
    WHERE id = (
        SELECT id
        FROM users
        WHERE username = 'emily33'
    )
);

