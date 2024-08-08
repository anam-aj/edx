SELECT title, rating, year
FROM movies JOIN ratings
ON movies.id = ratings.movie_id
WHERE year = 2010
ORDER BY rating DESC, title
limit 20;
