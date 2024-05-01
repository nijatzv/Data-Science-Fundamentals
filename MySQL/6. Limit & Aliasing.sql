-- Limit & Aliasing
-- limit specify how many rows i want in my output

select *
from employee_demographics
limit 3;

select *
from employee_demographics
order by age desc    # it will show top 3 oldest people in table
limit 3;

select *
from employee_demographics
order by age desc
limit 2, 1;



-- Aliasing
-- it is a way of changing the name of the column

select gender, avg(age) as avg_age
from employee_demographics
group by gender
having avg(age) > 40;

select gender, avg(age) avg_age
from employee_demographics
group by gender
having avg(age) > 40;

