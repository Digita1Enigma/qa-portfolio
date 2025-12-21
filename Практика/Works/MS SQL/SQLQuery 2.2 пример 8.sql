select model, price, min_price, max_price
from printer cross join
(select min(price) min_price, max(price) max_price
from printer) x;