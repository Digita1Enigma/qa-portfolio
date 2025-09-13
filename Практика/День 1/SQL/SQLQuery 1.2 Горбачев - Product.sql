SELECT maker, model, type
FROM Product
WHERE type='pc' AND (maker='A' OR maker='B')