"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

numbers = [i for i in range(1,101)]

squaredSum = sum( [i**2 for i in numbers] )
sumSquared = sum( numbers ) ** 2

print( sumSquared - squaredSum)