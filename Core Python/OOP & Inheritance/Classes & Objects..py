
# Data types we have in python sometimes cant cover what we wanna replace
# we can't replace humans, phone and etc. with booleans, numbers, strings and etc.
# by means of class we can define our data type
# class Student:
#     # we are modelling or "creating student"
#     def __init__(self, name, major, gpa, is_on_probation):      # creating initialize function to add what features do student have
#         self.name = name
#         self.major = major
#         self.gpa = gpa
#         self.is_on_probation = is_on_probation


# class is an template, model how we wanna create the student, object is an actual student
from Student import Student

student1 = Student("Nijat", "Computer Science", 4.7, False)        # inside the parenthesis give student name, major, ...

print(student1.gpa)




