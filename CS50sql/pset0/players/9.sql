SELECT first_name, last_name
FROM players
WHERE last_game
AND birth_state = 'PA'
ORDER BY debut DESC, first_name, last_name;
