BEGIN TRAN;
DELETE FROM dbo.users WHERE id = 1;          -- удаляем Ивана
SELECT COUNT(*) AS orders_after_delete
FROM dbo.orders WHERE user_id = 1;
ROLLBACK;
