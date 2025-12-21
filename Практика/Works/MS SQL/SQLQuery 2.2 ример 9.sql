select model from (
select distinct top 1 with ties model, price from pc
where price is not null
order by price) x;