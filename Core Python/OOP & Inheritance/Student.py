class Student:
    # we are modelling or "creating student"
    def __init__(self, name, major, gpa, is_on_probation):      # creating initialize function to add what features do student have
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
        
# putting functions in class
    def on_honor_roll(self):
        if self.gpa >= 3.5:
           return True
        else:
            return False
        
        
