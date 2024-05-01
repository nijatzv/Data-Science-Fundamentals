
# Where we can define functions inside of class and we can create another class, and inherit all of the attributes

from Chef import Chef
from ChineseChef import ChineseChef

myChef = Chef()
myChef.make_chicken()

myChineseChef = ChineseChef()
myChineseChef.make_chicken()
myChineseChef.make_special_dish()
# when we run the last line of code, instead of making his own special dish, program shows us normal chef's special dish bcs of inheritance











