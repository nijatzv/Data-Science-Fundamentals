-- SELECT Statement

SELECT * FROM employee_demographics; -- if the database is highlighted

SELECT * FROM parks_and_recreation.employee_demographics; -- in the database select table

SELECT first_name, last_name, birth_date
FROM parks_and_recreation.employee_demographics;

SELECT first_name, last_name, birth_date
age, (age + 10) * 10
FROM parks_and_recreation.employee_demographics;  -- creating new column named age+10
# PEMDAS is a order of operations that are arithmetic (+ - * /)

-- selecting unique values
SELECT DISTINCT first_name, gender
FROM parks_and_recreation.employee_demographics;


