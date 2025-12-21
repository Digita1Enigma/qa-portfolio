with t as(select * from (values(-2),(-3),(4),(-5), (null)) x(value)), p as(
select sum(case when value<0 then 1 else 0 end) neg,
sum(case when value>0 then 1 else 0 end) pos,
count(value) total
from t)
select case when total <> pos+neg then 0 else
(case when neg%2=1 then - 1 else +1 end) *exp(sum(log(abs(value))))
end product
from t, p
where value <> 0
group by neg,pos, total;