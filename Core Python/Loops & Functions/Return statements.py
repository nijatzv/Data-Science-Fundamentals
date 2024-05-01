
# In order to perform specific task we must call the function
# while executing we want to give some info back from our program/function

# cube a number with RETURN statement
def cube(num):
    num*num*num
print(cube(3)) # nothing happened,but it supposed to be cube a number

def cube(num):
    return num*num*num
print(cube(3))

# we can write name of our function as a variable
def cube(num):
    return num*num*num
result = cube(4)
print(result)   # cube of 4 is stored in result so whatever num we write inside of cube function, result will give the cube of it

# if we write a code after return statement it will not work
# return keyword breaks out of the function
def cube(num):
    return num*num*num
    print('code') # here
result = cube(4)
print(result)


# RETURN TASKS
# Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20
sample_list = [8,2,3,0,7]

def sumof(numbers):
    total = 0
    for i in numbers:
        total = total + i
    return total
print(sumof(sample_list))

# Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336
sam_list = [8, 2, 3, -1, 7]
def multiply(numbers):
    total = 1
    for i in numbers:
        total = i * total
    return total
print(multiply(sam_list))


#  Write a Python function to calculate the factorial of a number
#  (a non-negative integer). 
#  The function accepts the number as an argument.
def factorial(num):
    if num==0:
        return 1
    else:
        return num * factorial(num-1)
    
num=int(input("Add a number: "))
print(factorial(num))        


# Write a Python function to check 
# whether a number falls within a given range.
def test_range(n):
    if n in range(3, 9):
        return True
    else:
        return False
print(test_range(80))