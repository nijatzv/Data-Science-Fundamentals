
# Functions is a collection of a code that performs specific tasks
# We can put 1 thing in a function and it allows do it multiple times
# Functions are core of programming.

# def is a keyword, python understands that i wanna use a function and i will give it a name
def say_hi():
    print("Hello user") # text in function must be intended - icinde olmalidi

print("Top")
say_hi()    # we must call the function to execute
print("Bottom")
#Python jums up the say_hi function and will execute everything inside function

def say_hi(name):   #lets write name here
    print("Hello " + name) 
    
say_hi("Mike")
say_hi("Steve")
# Parameters are a piece of function to give info to the function

def say_hi(name, age):  # we can put more than 1 parameter inside the function
    print("Hello " + name + ", you are "+ age) 
    
say_hi("Mike", "35")
say_hi("Nicat", "20")

# lets write age as integers, dont forget to change it to str in function
def say_hi(name, age):  # we can put more than 1 parameter inside the function
    print("Hello " + name + ", you are "+ str(age)) 
    
say_hi("Mike", 35)
say_hi("Nicat", 20)
