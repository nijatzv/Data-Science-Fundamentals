-- String functions

select length('skyfall');

select first_name, length(first_name)    # gives the length of something we need
from employee_demographics
order by 2;

select LOWER(first_name), UPPER(first_name)    # makes elements lower or upper case
from employee_demographics;

select TRIM('    sky   ');    # trims from both left and right sides
select LTRIM('   sky   ');    # trims from left side
select RTRIM('   sky   ');    # trims from right side


-- SUBSTRINGS

select first_name, 
left(first_name, 4),    # selects 4 chars from left
right(first_name, 4),    # selects 4 chars from right
substring(first_name, 3, 2),    # select the word, from 3rd position, step 2 chars
birth_date,
substring(birth_date, 6, 2) as birth_month
from employee_demographics;


-- REPLACE
SELECT first_name, replace(first_name, 'a', 'z')    # replacing something with something else
from employee_demographics;

select LOCATE('x', 'Alexander');    # tells us the location of character


select first_name, last_name,
concat(first_name, ' ', last_name) as full_name
from employee_demographics;







