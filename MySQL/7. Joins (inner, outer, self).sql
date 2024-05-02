# INTERMEDIATE SQL

-- Joins

select *
from employee_demographics;

select *
from employee_salary;


# INNER JOINS will return rows that are the same in both columns and both tables

select *
from employee_demographics
inner join employee_salary    -- by default join represents INNER JOIN
	on employee_demographics.employee_id = employee_salary.employee_id
;

select *
from employee_demographics as dm
inner join employee_salary as sal
	on dm.employee_id = sal.employee_id
;

select dem.employee_id, age, occupation    # if do not mention dem, program not gonna know where to pull it from
from employee_demographics as dem
inner join employee_salary as sal
	on dem.employee_id = sal.employee_id;
    
    
    
-- OUTER JOINS (left or right)
-- Left join takes everything from left table and matches them with right table, and opposite is correct for right join

select *
from employee_demographics as dem
left join employee_salary as sal
	on dem.employee_id = sal.employee_id;

# taking everything from right table and matching with left table
select *
from employee_demographics as dem
right join employee_salary as sal
	on dem.employee_id = sal.employee_id;
    
    
    
-- SELF JOIN
-- it is a join to tie table to itself

select *
from employee_salary emp1
join employee_salary emp2
	on emp1.employee_id + 1 = emp2.employee_id
;

select emp1.employee_id as emp_santa, 
emp1.first_name as first_name_santa,
emp1.last_name as last_name_santa,
emp2.employee_id as emp_name, 
emp2.first_name as first_name_emp,
emp2.last_name as last_name_emp
from employee_salary emp1
join employee_salary emp2
	on emp1.employee_id + 1 = emp2.employee_id
;



-- Joining multiple tables together

select *
from employee_demographics as dem
inner join employee_salary as sal
	on dem.employee_id = sal.employee_id
inner join parks_departments pd
	on sal.dept_id = pd.department_id
;

select *
from parks_departments;  # reference table








