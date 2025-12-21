select distinct maker
from product pr1
where not exists
   (select type
    from product
	where type not in
	           (select type
			    from product pr2
				where pr1.maker=pr2.maker
			   )
	);