SELECT user_id
FROM friends
WHERE friend_id = (
    SELECT id
    FROM users
    WHERE username = 'lovelytrust487'
)
