select maker
from product 
group by maker
having count(distinct type) = 
            (select count(distinct type) from product);