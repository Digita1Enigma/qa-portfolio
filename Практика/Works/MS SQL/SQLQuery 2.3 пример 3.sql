select distinct pc.model, maker 
from pc, (select maker, model
 from product) as prod (maker, model_1)
 where model = model_1 and price < 600;