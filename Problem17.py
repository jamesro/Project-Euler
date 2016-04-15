"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

words = {   1:"one",
            2:"two",
            3:"three",
            4:"four",
            5:"five",
            6:"six",
            7:"seven",
            8:"eight",
            9:"nine",
            10:"ten",
            11:"eleven",
            12:"twelve",
            13:"thirteen",
            14:"fourteen",
            15:"fifteen",
            16:"sixteen",
            17:"seventeen",
            18:"eighteen",
            19:"nineteen",
            20:"twenty",
            30:"thirty",
            40:"forty",
            50:"fifty",
            60:"sixty",
            70:"seventy",
            80:"eighty",
            90:"ninety",
            }

def one(n):
    return len(words[int(n)])

def two(n):
    if n[0] == "0":
        return one(n[-1])
    elif (n[0] == "1") or ((n[0]!="0") and (n[-1]=="0")):
        return len(words[int("".join(n))])
    else:
        return len(words[int("".join((n[0],"0")))]) + one(n[-1])

def three(n):
    if n[1]==n[2]=="0":
        return one(n[0]) + len("hundred")
    else:
        return one(n[0]) + len("hundred") + len("and") + two(n[1:])

def getLength(number):
    # Max 1000
    number = list(str(number))
    length = 0
    print(number)

    if len(number)==3:
        return three(number)
    elif len(number)==2:
        return two(number)
    else:
        return one(number[0])

if __name__ == "__main__":
    total = 0
    for i in range(1,1000):
        total += getLength(i)
    total += len("onethousand")
    print(total)