"""
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.
Note: you may assume that n is not less than 2.
"""

def integerBreak(n):
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4
        
        count = 0
        remainder = n % 3
        if remainder == 0:
            while n > (count):
                count += 3
            return 3**(count / 3)
        elif remainder == 1:
            while n > (count + 4):
                count += 3
            return 3**(count / 3) * 4
        elif remainder == 2:
            while n > (count + 2):
                count += 3
            return 3**(count / 3) * 2