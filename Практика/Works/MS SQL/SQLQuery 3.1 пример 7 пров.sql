select maker from (select maker from product
                   where type='pc'
				   intersect all
				   select maker from product
				   where type='printer')
x group by maker having count(*)>1;