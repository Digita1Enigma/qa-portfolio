select coalesce(x.point, y.point) point, coalesce(x.qty, y.qty) qty from
(select cast(point as varchar) point, sum(inc) qty
from income group by point) x
full join 
(select 'all' point, sum(inc) qty
from income) y on 1 = 2;