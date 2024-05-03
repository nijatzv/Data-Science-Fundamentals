-- Subqueries

select *
from employee_demographics;

select *
from employee_salary;


# selecting employees that work in parks and rec department

select *
from employee_demographics
where employee_id IN 
					(SELECT employee_id
						FROM employee_salary
                        WHERE dept_id = 1)
;


# avg salary with comparison person's salary
select first_name, salary,
		(select avg(salary)
		from employee_salary)
from employee_salary
group by first_name, salary;


# grouping genders with their max, min and avg age
select gender, avg(age), max(age), min(age), count(age)
from employee_demographics
group by gender;

# if we have alied a column we can use its name, but if not, we must write like this AVG(`MAX(age)`) - the symbol stands top of the TAB button
select *
from
(select gender, avg(age), max(age), min(age), count(age)
from employee_demographics
group by gender) as agg_table
;

