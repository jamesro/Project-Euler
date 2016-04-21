"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two
abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the
sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known
that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

from functools import reduce

def FactorSum(n):    
    factors = set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    return sum(factors) - n

def GetAbundantNumbers(min,max):
    abNums = []
    for i in range(min,max+1):
        if i < FactorSum(i):
            abNums.append(i)
    return abNums


def abundantSums(n,abundantNumbers):
    for abNum in abundantNumbers:
        if (n + abNum) < 28123:
            yield (n + abNum)
        else:
            break


def sums(lst, limit):    # prevent global lookups by using a function
    res = set()          # set membership testing is much faster than lists
    res_add = res.add    # cache add method
    for i, first in enumerate(lst):   # get index and item at the same time
        for second in lst[i:]:        # one copy operation saves n index ops.
            res_add(first + second)   # prevent creation/lookup of extra local temporary
    return sorted([x for x in res if x < limit])


if __name__ == "__main__":

    """
    1: get all abundant numbers between 12 and 28123

    2: for each abundant number, add every other abundant number giving a total less than 28123.
    get the set of all totals (ignore duplicates)

    3: get all missing numbers between 1 and 28123

    4: sum them 
    """

    abundantNumbers = GetAbundantNumbers(12,28123)
    
    print(sum( (set([i for i in range(1,28124)]) - set(sums(abundantNumbers,28124))) ))
    # print(sums(abundantNumbers,28124))

