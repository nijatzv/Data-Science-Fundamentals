
# While loop is a structure that loop through a code and executes it many times
# It will loop through till our condition is False
# while condition
i = 1 
while i <= 10:
    print(i)
    i = i+1     # i += 1
print("Done with loop")


# TASKS
# Write a while loop 
# to print only the even numbers from 0 – 20.
num = 0
while num <= 20:
    if num % 2 == 0:
        print(num)
    num += 1

# Write a while loop
# to print the numbers from 1 to 100.
num = 1
while num <= 100:
    if num % 3 == 0 and num % 5 == 0:
        print(num, "Tres Cinco")
    elif num % 3 == 0:
        print(num, "Tres")
    elif num % 5 == 0:
        print(num, "Cinco")
    else:
        print(num)
    num += 1
    
# Create a function named remove_sql_specialists(people_list).
# Given a list of tuples, it removes people whose job titles
# contain the word "SQL" from the list. You can use the 
# in operator to check if a given job title contains the word "SQL". 
# Use the following data containing employee names, job titles, and salaries:
new_hires = [('Mark Adams', 'SQL Analyst', 4000),
             ('Leslie Burton', 'HR Specialist', 2300),
             ('Dorothy Castillo', 'UX Designer', 3100)]
def remove_sql_specialists(people_list):
    for person in people_list[:]:
        if "SQL" in person[1]:
            people_list.remove(person)
print(remove_sql_specialists(new_hires))
print(new_hires)
        
