SELECT to_user_id
FROM messages
WHERE from_user_id = (
    SELECT id
    FROM users
    WHERE username = 'creativewisdom377'
)

SELECT *
FROM table1
WHERE column2 = 2
GROUP BY column1
ORDER BY column1
LIMIT 3
