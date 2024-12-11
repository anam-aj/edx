EXPLAIN QUERY PLAN
SELECT phone_number
FROM users
WHERE joined_date < '2020-01-01'
LIMIT 10;

/*
select *
from users
where joined_date < '2010-01-01'
order by joined_date
desc limit 10;?
*/
