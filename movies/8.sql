SELECT *
--FROM (people JOIN stars ON people.id = stars.person_id)
From  (stars JOIN movies ON stars.movie_id = movies.id)
limit 5;
