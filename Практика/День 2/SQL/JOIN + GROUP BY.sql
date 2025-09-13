-- Сколько кораблей у каждой страны (или: сколько картин у каждого художника)
SELECT c.country, COUNT(*) AS ships_count
FROM   Ships s
JOIN   Classes c ON c.class = s.class
GROUP  BY c.country
ORDER  BY ships_count DESC;
