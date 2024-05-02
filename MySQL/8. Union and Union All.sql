-- UNIONs
-- Unions allows us to combine rows together

select age, gender
from employee_demographics
UNION
select first_name, last_name
from employee_salary;

select first_name, last_name
from employee_demographics
UNION    -- it is UNION DISTINCT, which removes all duplicates
select first_name, last_name
from employee_salary;


select first_name, last_name
from employee_demographics
UNION ALL
select first_name, last_name
from employee_salary;


select first_name, last_name, "Old Man" as label
from employee_demographics
where age > 40 and gender = 'Male'
union
select first_name, last_name, 'Old Lady' as label
from employee_demographics
where age> 40 and gender = 'Female'
union
select first_name, last_name, "highly paid employee" as label
from employee_salary
where salary > 70000
order by first_name, last_name
;








