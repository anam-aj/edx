UPDATE users
SET password = (
    SELECT password
    FROM users
    WHERE username = 'emily33'
)
WHERE username = 'admin';


UPDATE users
SET password = (
    SELECT password
    FROM users
    WHERE username = 'emily33'
)
WHERE username = 'admin';
