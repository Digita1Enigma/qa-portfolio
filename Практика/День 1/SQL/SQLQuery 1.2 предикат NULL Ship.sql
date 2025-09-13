select ship, case launched
 when null 
 then 1900 
 else launched
 end 'year'
from outcomes o left join
 ships s on o.ship=s.name;