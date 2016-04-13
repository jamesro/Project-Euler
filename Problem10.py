"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


from math import sqrt
from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))



if __name__ == "__main__":
    primes = []
    i = 1
    while i < 2000000:
        i += 1
        if isPrime(i):
            primes.append(i)

    print(sum(primes))