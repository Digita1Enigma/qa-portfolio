select p.model, p.type from pc join product p on
pc.model=p.model where maker='b'
union all
select p.model, p.type from printer pr join product p on
pr.model=p.model where maker='b'
union all
select p.model, p.type from laptop lp join product p on
lp.model=p.model where maker='b';