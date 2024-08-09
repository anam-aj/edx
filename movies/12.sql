-- Select title
SELECT count(title)
FROM movies
WHERE id IN
    (
    -- Select movie IDs
    SELECT movie_id
    FROM stars
    WHERE person_id = 459023 and 681726
    );
