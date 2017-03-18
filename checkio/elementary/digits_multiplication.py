# DESCRIPTION

"""
You are given a positive integer. Your function should calculate the product of
the digits excluding any zeroes.
For example: The number given is 123405. The result will be 1*2*3*4*5=120
(don't forget to exclude zeroes).

Input: A positive integer.
Output: The product of the digits as an integer.

Example:
checkio(123405) == 120
checkio(999) == 729
checkio(1000) == 1
checkio(1111) == 1
"""

# CODE


def checkio(number):
    res = 1
    for d in str(number):
        res *= int(d) if int(d) else 1
    return res

# VERIFICATION

if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
