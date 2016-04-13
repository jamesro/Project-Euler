"""A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers."""



palindrome = False

while not palindrome:
    for i in range(999,0,-1):
        for j in range(999,888,-1):
            if str(i*j)[::-1] == str(i*j):
                print(i*j)
                palindrome = True
                break
    
