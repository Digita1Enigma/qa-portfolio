select product.type, pc.model, price from pc inner join
    product on pc.model = product.model
union
select product.type, laptop.model, price from laptop inner join
    product on laptop.model = product.model
order by price desc;