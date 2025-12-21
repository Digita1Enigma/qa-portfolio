select ship from outcomes
except all
select name from ships where name<>'california';