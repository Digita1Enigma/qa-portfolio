select model, speed, hd from pc
where hd in (10, 20) and model in 
      (select model from product
	  where maker = 'a');