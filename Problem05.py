"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
"""
1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
x,x,x,x,x,x,x,x,x,x,x,x,x,x,


20,19,18,17,16,14,13,12,11,
"""
from functools import reduce
from itertools import product
import operator



def Factors(n):    
    return set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
"""
n = 20
nums = [i for i in range(11,21)]
Found = False

while not Found:
    print(n)
    if all( i in Factors(n) for i in nums ):
        print(n)
        Found = True
    n += 20
"""




nums = [i for i in range(11,21)]


def solve(step):
    for number in range(step,999999999,step):
        if all( number%_ ==0 for _ in nums):
            return number
    return none

if __name__ == "__main__":
    solution = solve(2520)
    print(solution)
            






