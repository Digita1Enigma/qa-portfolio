select model, price from pc
union
select model, price from laptop
order by price desc;