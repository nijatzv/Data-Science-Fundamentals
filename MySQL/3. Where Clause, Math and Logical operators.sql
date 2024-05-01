# WHERE statement (to filter our data)

SELECT * FROM employee_salary
WHERE first_name = 'Leslie';  # first_name must be Leslie

SELECT * FROM employee_salary
WHERE salary > 50000;         # comparison operators (=, !=, >, <, )

select * from employee_demographics
where gender != 'Female';

select * from employee_demographics
where birth_date > '1985-01-01';


#Logical operators in where clause
-- AND OR NOT --

select * from employee_demographics
where birth_date > '1985-01-01'
and gender = 'Male';

select * from employee_demographics
where birth_date > '1985-01-01'
or  not gender = 'Male';

select * from employee_demographics
where (first_name = 'Leslie' AND age = 44) OR age > 55;


-- LIKE Statement
-- % (anything), _ (specific element)

select * from employee_demographics
where first_name = 'Jery';

select * from employee_demographics
where first_name LIKE 'Jer%';

select * from employee_demographics
where first_name LIKE '%er%';

select * from employee_demographics
where first_name LIKE 'a__'; # it has 2 chars after 'a'

select * from employee_demographics
where first_name LIKE 'a___%';

select * from employee_demographics
where birth_date LIKE '1989%';  # someone whose birthday year is 1989





