SELECT * FROM product
WHERE maker='A'
intersect
SELECT * FROM product
WHERE type='pc';