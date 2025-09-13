SELECT * FROM product
where maker = 'a'
union
select * from product
where maker = 'b';