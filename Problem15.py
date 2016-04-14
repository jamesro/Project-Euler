"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
"""

# This is just arranging two sets of 20 objects. so 40!/(20!(40-20)!)
from math import factorial

print(factorial(40)/(factorial(20)*factorial(20)))