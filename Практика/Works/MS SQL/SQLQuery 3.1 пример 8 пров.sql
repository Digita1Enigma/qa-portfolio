select pc.maker from (select maker from product
                      where type='pc' group by maker
					  having count(*)>1) pc 
NATURAL join (select maker from product
                 where type='printer' group by maker
				 having count(*)>1) Pr;