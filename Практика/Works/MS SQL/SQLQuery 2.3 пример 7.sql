select coalesce(m_pc.maker, m_printer.maker) from
(select distinct maker from product where type='pc') m_pc
full join
(select distinct maker from product where type='printer') m_printer
on m_pc.maker = m_printer.maker
where m_pc.maker is null or m_printer.maker is null;