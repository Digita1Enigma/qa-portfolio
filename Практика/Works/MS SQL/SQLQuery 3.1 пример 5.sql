select ship from outcomes
except
select name from ships where name <> 'california';