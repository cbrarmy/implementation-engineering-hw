with test_cte (username)
as 
(select USERname
from users
group by username
having COUNT(username)>1)

select tc.username,signup_date
from (select *,row_number() over(partition by username order by signup_date desc)rn from users)t 
join test_cte as tc on t.username=tc.username
where rn='1'
