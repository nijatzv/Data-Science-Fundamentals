
employee_file = open("employees.txt", "r")
print(employee_file.read())
employee_file.close()

# lets say i wanna add another employee

employee_file = open("employees.txt", "a")
employee_file.write("\nEmin - Human Resources")
employee_file.close()

# "\n" - new line character (escape caracter)

employee_file = open("employees.txt", "w")
employee_file.write("\nEmin - Human Resources")
employee_file.close()       # after runnig this code (writing) it will overwrite the existing file

# creating a new file
employee_file = open("employees1.txt", "w")
employee_file.write("\nEmin - Human Resources")
employee_file.close()