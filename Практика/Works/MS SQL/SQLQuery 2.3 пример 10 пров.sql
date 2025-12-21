select * from income left join outcome using(date, point, code)
where month(date) >= 4;