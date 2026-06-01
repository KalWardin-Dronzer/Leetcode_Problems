# Write your MySQL query statement below
select distinct num as ConsecutiveNums from 
(select num,
lag(num,1) over (order by id)  as prev_num,
lag(num,2) over (order by id) as prev_prev_num
from logs
 ) as subquery
where num = prev_num and prev_num = prev_prev_num


