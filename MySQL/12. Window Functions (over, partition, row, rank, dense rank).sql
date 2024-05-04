-- Window Functions

Select *
from employee_demographics;

Select gender, avg(salary) as avg_salary
from employee_demographics dem
JOIN employee_salary sal
	ON dem.employee_id = sal.employee_id
group by gender;


select gender, avg(salary) OVER(partition by gender)
from employee_demographics dem
JOIN employee_salary sal
	ON dem.employee_id = sal.employee_id;
    
    
select dem.first_name, dem.last_name, salary,
sum(salary) OVER(partition by gender order by dem.employee_id) as rolling_total
from employee_demographics dem
JOIN employee_salary sal
	ON dem.employee_id = sal.employee_id;


select dem.employee_id, dem.first_name, dem.last_name, gender, salary,
row_number() over(partition by gender order by salary desc) as row_num,
RANK() over(partition by gender order by salary desc) as rank_num,
DENSE_RANK() over(partition by gender order by salary desc) as dense_rank_num
from employee_demographics dem
JOIN employee_salary sal
	ON dem.employee_id = sal.employee_id;
