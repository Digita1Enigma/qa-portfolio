select distinct pc.model, maker
from PC, product
where pc.model = product.model and price < 600;