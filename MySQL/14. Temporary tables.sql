-- Temporary Tables
-- Only visible to the session that is created

# 1st way:
CREATE TEMPORARY TABLE temp_table
(first_name varchar(50),
last_name varchar(50),
fav_movie varchar(100)
);

select *
from temp_table;

insert into temp_table
values('Nijat', 'Zakarya', 'Dark Knight');


# 2nd way

select *
from employee_salary;

create temporary table salary_over_50k
select *
from employee_salary
where salary >= 50000;

select * from salary_over_50k;
