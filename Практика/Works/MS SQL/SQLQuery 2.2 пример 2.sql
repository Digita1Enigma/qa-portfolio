SELECT COUNT(*) AS Qty
FROM PC
WHERE model IN(SELECT model
FROM Product
WHERE maker = 'A'
);