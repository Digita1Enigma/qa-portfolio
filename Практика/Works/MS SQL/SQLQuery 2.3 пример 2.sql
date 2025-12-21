select distinct a.model as model_1, b.model as model_2
from pc as a, pc b 
where a.price = b.price and a.model < b.model;