-- ������� ��� ���������� ������ (��� ���������� ��� ������������� � �.�.)
SELECT s.name, s.class, c.class AS matched
FROM   Ships s
LEFT JOIN Classes c ON c.class = s.class
WHERE  c.class IS NULL;
