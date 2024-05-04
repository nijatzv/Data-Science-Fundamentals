-- ADVANCED SQL

-- CTEs (common table expressions)


WITH CTE_example AS    # WITH CTE_example (GENDER, AVG_SAL, MAX_SAL, MIN_SAL, COUNT_SAL) AS
(
select gender, avg(salary) avg_sal, max(salary) max_sal, min(salary) min_sal, count(salary) count_sal
from employee_demographics dem
join employee_salary sal
	on dem.employee_id = sal.employee_id
group by gender
)
select avg(avg_sal)
from CTE_example;

select avg(avg_sal)
from CTE_example;    # it will show an error, bcs we should use cte immediatelly after our query



WITH CTE_example AS
(
select employee_id, gender, birth_date
from employee_demographics
where birth_date > '1985-01-01'
),
CTE_example2 AS
(
select *
from employee_salary
where salary > 50000
)
select *
from CTE_example
join CTE_example2    # this is an example not an actual usecase
	on CTE_example.employee_id = CTE_example2.employee_id
;
























