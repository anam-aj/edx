SELECT to_user_id
FROM messages
WHERE form_user_id = (
    SELECT id
    FROM users
    WHERE username = 'creativewisdom377'
)

