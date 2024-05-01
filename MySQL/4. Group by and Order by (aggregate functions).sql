-- GROUP BY

select *
from employee_demographics;

select gender
from employee_demographics
group by gender;

select count(first_name), gender
from employee_demographics
group by gender;

select AVG(age), gender
from employee_demographics
group by gender;

select occupation, salary
from employee_salary
group by occupation, salary;

select gender, avg(age), max(age), min(age), count(age)
from employee_demographics
group by gender;


-- ORDER BY -- sorts results in an ascending or descending order
select *
from employee_demographics
order by first_name;

select *
from employee_demographics
order by first_name ASC;

select *
from employee_demographics
order by first_name DESC;

select *
from employee_demographics
order by gender, age;

select *
from employee_demographics
order by age, gender;  # we sort for age and there is no unique values so it will sort only for age

select *
from employee_demographics
order by 5, 4;        # not recommended so much
