-- Stored Procedures

USE parks_and_recreation;

select *
from employee_salary
where salary >= 50000;

CREATE PROCEDURE large_salaries()
select *
from employee_salary
where salary >= 50000;

CALL large_salaries();


DELIMITER $$
CREATE PROCEDURE large_salaries3()
BEGIN
	select *
	from employee_salary
	where salary >= 50000;
	select *
	from employee_salary
	where salary >= 10000;
END $$
DELIMITER ;

CALL large_salaries3();



# PARAMETERS

DELIMITER $$
CREATE PROCEDURE large_salaries5(isci_id INT)    # we can call here whatever we want
BEGIN
	select salary
	from employee_salary
    where employee_id = isci_id
    ;
END $$
DELIMITER ;

call large_salaries5(1);
