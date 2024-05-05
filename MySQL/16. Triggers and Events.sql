-- Triggers and Events
-- A trigger is a block of code that executes automatically when an event takes place on a specific table

select *
from employee_demographics;

select *
from employee_salary;


DELIMITER $$
create trigger employee_insert
	after insert on employee_salary    # before
    for each row
begin
	insert into employee_demographics (employee_id, first_name, last_name)
    values (new.employee_id, new.first_name, new.last_name);     # old
end $$
DELIMITER ;

insert into employee_salary (employee_id, first_name, last_name, occupation,
salary, dept_id)
values(13, 'Nijat', 'Zakarya', 'Data Scientist', 15000, NULL);



-- EVENTS

select *
from employee_demographics;

# lets think that if employee is over 60, he gonna be retired

delimiter $$
create event delete_olds
on schedule every 30 second
do
begin
	delete
    from employee_demographics
    where age >=60;
end $$
delimiter ;


show variables like 'event%';
