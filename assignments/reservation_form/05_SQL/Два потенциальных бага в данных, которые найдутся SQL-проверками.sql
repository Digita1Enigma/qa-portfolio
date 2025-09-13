SELECT email, COUNT(*) c FROM users GROUP BY email HAVING COUNT(*) > 1;


SELECT * FROM users WHERE age < 0 OR age > 120;
SELECT * FROM users WHERE email NOT LIKE '%@%.__%';
