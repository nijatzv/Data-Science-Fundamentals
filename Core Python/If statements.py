
is_male = True
if is_male:
    print("You are a male.")    #whatever i put in here, will be executed if the condition is true

# else keyword - otherwise
if is_male:
    print("You are a male.")
else:
    print("You are not a male.")
    
#lets make it a bit complex
is_male = True
is_tall = True

if is_male or is_tall: # if the person is either male or tall
    print("You are a male or tall or both")
else:
    print("You are neither a male nor tall")
    
# in AND operator,both of the conditions must be true

# we can add in one more condition
is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall): # not function will negative the statement
    print("you are a short male")
elif not is_male and is_tall: # 
    print("you are a short male")
else:
    print("You are not a male and not tall")



# COMPARISONS inside IF statemens
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:   #!= means not equal
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(30,45,5)) # we can compare all data types, including strings and booleans

    

