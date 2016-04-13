from itertools import count, islice
from math import sqrt
def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

primes = []
i = 2
while len(primes) < 10001:
    if isPrime(i):
        primes.append( i )
    i += 1

print(primes[-1])