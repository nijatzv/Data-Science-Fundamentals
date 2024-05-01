
employee_file = open("employees.txt", "r")      # first mode is read - r
                                # write mode - w, writing and changing
                                # append mode - a, when i cant change or modify, i can add info
                                # read and writin - r

print(employee_file.readable())   # whether or not the file is readable
print(employee_file.read())
print(employee_file.read())         # read all info in file
print(employee_file.readline())     # read first line of file
print(employee_file.readlines())    # read all lines as one list

employee_file.close()

# printing each line with for loop
employee_file = open("employees.txt", "r")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()



