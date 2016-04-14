"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def isOdd(number):
    return number % 2 != 0

def nextLink(n):
    if isOdd(n):
        return 3*n + 1
    else:
        return n/2

def getChain(n):
    length = 1
    while n > 1:
        length += 1
        n = nextLink(n)
    return length

if __name__ == "__main__":
    # Not efficient to use a dictionary but I haven't used them in a long time so...
    chains = {}

    for i in range(2,1000001):
        chains[i] = getChain(i)

    print(max(chains,key=chains.get))
