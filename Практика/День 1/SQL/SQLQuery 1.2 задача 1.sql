SELECT * FROM product
WHERE maker = 'A'
INTERSECT
SELECT * FROM product
WHERE type = 'pc'