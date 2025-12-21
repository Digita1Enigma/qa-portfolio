select maker, product.model as model_1, pc.model as model_2, price
from product right join
 pc on pc.model = product.model
order by maker, pc.model;