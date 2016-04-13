"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""



"""
from 3 to sqrt(n)

    check if prime
    check if factor
    add 2
"""
from functools import reduce

from math import sqrt
from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def Factors(n):    
    return set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def PrimeFactors(number):
    factors = Factors(number)
    primefactors = [i for i in factors if isPrime(i)]        
    return primefactors

if __name__ == "__main__":
    print(max(PrimeFactors(600851475143)))