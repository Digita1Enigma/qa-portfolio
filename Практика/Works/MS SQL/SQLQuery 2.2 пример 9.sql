select distinct max(avg(price)) over () max_avg_price
from product p join pc on p.model = pc.model
group by maker;