/* 0) Создать БД, если нет */
IF DB_ID(N'qa_portfolio') IS NULL
BEGIN
  CREATE DATABASE qa_portfolio;
END
GO

/* 1) Переключиться на неё */
USE qa_portfolio;
GO

/* 2) Чистый старт: удаляем таблицы, если уже существуют */
IF OBJECT_ID(N'dbo.orders', N'U') IS NOT NULL DROP TABLE dbo.orders;
IF OBJECT_ID(N'dbo.users',  N'U') IS NOT NULL DROP TABLE dbo.users;
GO

/* 3) Пользователи (как в задании) */
CREATE TABLE dbo.users (
    id     INT IDENTITY(1,1) CONSTRAINT PK_users PRIMARY KEY,
    name   NVARCHAR(100)  NOT NULL,
    email  NVARCHAR(255)  NOT NULL CONSTRAINT UQ_users_email UNIQUE,
    age    INT            NOT NULL CONSTRAINT CK_users_age CHECK (age BETWEEN 0 AND 120),
    status NVARCHAR(16)   NOT NULL CONSTRAINT CK_users_status CHECK (status IN (N'active', N'inactive'))
);
GO

/* 4) Данные — обратим внимание на префикс N'' для кириллицы */
INSERT INTO dbo.users (name, email, age, status) VALUES
(N'Иван',   N'ivan@test.com',  25, N'active'),
(N'Ольга',  N'olga@test.com',  30, N'inactive'),
(N'Сергей', N'serg@test.com',  22, N'active'),
(N'Мария',  N'maria@test.com', 35, N'active');
GO

/* 5) Заказы (для демонстрации каскада) */
CREATE TABLE orders (
    id         INT IDENTITY(1,1) CONSTRAINT PK_orders PRIMARY KEY,
    user_id    INT NOT NULL
               CONSTRAINT FK_orders_users
               REFERENCES dbo.users(id) ON DELETE CASCADE,
    total      DECIMAL(10,2) NOT NULL CONSTRAINT DF_orders_total DEFAULT (0.00),
    created_at DATETIME2(0)  NOT NULL CONSTRAINT DF_orders_created DEFAULT (SYSUTCDATETIME())
);
GO

/* 6) Пара заказов: у Ивана (id=1) и у Сергея (id=3) */
INSERT INTO orders (user_id, total) VALUES
(1, 10.00), (1, 25.50),
(3,  5.00);
GO

/* ===== Примеры запросов из задания ===== */

/* A) Активные пользователи старше 25 */
SELECT * FROM users
WHERE status = N'active'
  AND age > 25;


/* B) Количество неактивных пользователей */
SELECT COUNT(*) AS inactive_count
FROM users
WHERE status = N'inactive';


/* C) Имя и email, сортировка по убыванию возраста */
SELECT name, email
FROM users
ORDER BY age DESC;
GO

/* D) Демонстрация каскадного удаления */
BEGIN TRAN;
DELETE FROM dbo.users WHERE id = 1;          -- удаляем Ивана
SELECT COUNT(*) AS orders_after_delete
FROM dbo.orders WHERE user_id = 1;
ROLLBACK;


/* E) Два потенциальных бага в данных, которые найдутся SQL-проверками */
SELECT email, COUNT(*) c FROM users GROUP BY email HAVING COUNT(*) > 1;

SELECT * FROM users WHERE age < 0 OR age > 120;
SELECT * FROM users WHERE email NOT LIKE '%@%.__%';