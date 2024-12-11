CREATE INDEX test_index
ON users ()


select *
from users
where joined_date < '2010-01-01'
order by joined_date
desc limit 10;
