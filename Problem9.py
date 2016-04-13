"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def PythagoreanTriplet(product):
    for i in range(1,999):
        for j in range(1,999):
            for k in range(1,999):
                if (i + j + k == product):
                    if ((i**2 + j**2) == k**2):
                        return (i*j*k)
                        break

if __name__ == "__main__":
    print(PythagoreanTriplet(1000))