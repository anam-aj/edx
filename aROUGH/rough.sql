CREATE INDEX


select *
from users
where joined_date < '2010-01-01'
order by joined_date
desc limit 10;
