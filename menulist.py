#imports the ability to get a random number (we will learn more about this later!)
from random import *

sides = ["fries","potatoes","fruit"]
courses = ["filet","hamburger", "salad","porkchop"]
desserts = ["cotton candy","cake","ice cream"]

#Generates a random integer.
first = randint(0, len(sides)-1)
second = randint(0, len(courses)-1)
third = randint(0, len(desserts)-1)

meal= sides[first] + " and " + courses[second] + " and " + desserts[third]

print ("your meal is", meal)
