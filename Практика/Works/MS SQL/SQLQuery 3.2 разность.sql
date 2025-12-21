select distinct maker
from product pr1
where type = all 
 (select type from product
 except
 select type from product pr2
 where pr2.maker = pr1.maker);