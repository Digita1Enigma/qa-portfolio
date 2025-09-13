select * from product
except
select * from product where type = 'pc';