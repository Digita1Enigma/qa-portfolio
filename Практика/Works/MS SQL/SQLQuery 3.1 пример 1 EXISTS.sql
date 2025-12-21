select distinct maker
from product as lap_product 
where type='laptop' and
 exists (select maker
 from product
 where type ='printer' and
 maker = lap_product.maker);