
# Errors or exceptions stop our program running :(
# but we can handle them :)

number = int(input("Add a number: "))
print(number)       # program will work when we enter an integer
# however, if we enter another data type, like string
# we will face "ValueError: invalid literal for int() with base 10:"

# in order to handle errors use: try/except blocks
try:
    number = int(input("Add a number: "))
    print(number)
except:
    print("Invalid input")
    
# but there is also a situation like this
value = 10/0    # cant divide a number by zero
# ZeroDivisionError: division by zero

try:
    value = 10/0
    number = int(input("Add a number: "))
    print(number)
except:
    print("Invalid input")      # output here will be invalid input, but we didnt input anything
    

# In python we can specify the types of errors
try:
    value = 10/0
    number = int(input("Add a number: "))
    print(number)
except ZeroDivisionError:
    print("Divided by zero")
except ValueError as err:
    print(err)
     





