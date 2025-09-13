-- Пример для схемы Ships/Classes (переименуй под свои поля)
SELECT s.name      AS ship_name,
       c.class     AS class_name,
       c.country,
       c.displacement
FROM   Ships s
JOIN   Classes c ON c.class = s.class;
