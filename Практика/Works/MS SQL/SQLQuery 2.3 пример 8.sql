with a(a_id) as
(select * from (values('1'),('2'),('3')) x(y)), 
b(b_id) as
(select * from (values('1'),('2'),('4')) x(y)), 
c(c_id) as
(select * from (values('5'),('2'),('3')) x(y))
select a_id, b_id, c_id from (a left join b on a_id=b_id) inner join c on b_id=c_id
union all
select '','',''
union all
select a_id, b_id, c_id from a left join (b inner join c on b_id=c_id) on a_id=b_id;