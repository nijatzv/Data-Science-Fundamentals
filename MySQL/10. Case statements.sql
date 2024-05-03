-- Case Statements

select first_name,
last_name,
age,
CASE
	WHEN age <= 30 THEN 'Young'
END
from employee_demographics;


select first_name,
last_name,
age,
CASE
	WHEN age <= 30 THEN 'Young'
    WHEN age BETWEEN 31 AND 50 THEN 'Old'
    WHEN age >= 50 THEN "On death's door"
END as age_bracket
from employee_demographics;



-- Pay increase and Bonus
-- < 50000 = 5%
-- > 50000 = 7%
-- Finance = 10% bonus

select first_name, last_name, salary,
CASE
	WHEN salary < 50000 THEN salary + (salary * 1.05)
    WHEN salary > 50000 THEN salary + (salary * 1.07)
END as new_salary,
CASE
	WHEN dept_id = 6 THEN salary * .10
END as bonus
from employee_salary;

select * from employee_salary;
select * from parks_departments;






