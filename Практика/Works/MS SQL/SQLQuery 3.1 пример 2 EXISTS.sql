select distinct maker
from product as lap_product
where type = 'laptop' and
 not exists (select maker
 from product
 where type = 'printer' and
 maker = lap_product.maker);