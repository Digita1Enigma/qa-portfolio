SELECT model, COUNT(model) AS Qty_model,
AVG(price) AS avg_price
FROM pc
GROUP BY model
HAVING AVG(price) < 800;