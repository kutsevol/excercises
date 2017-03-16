# coding: utf-8
# Task description

"""
A binary gap within a positive integer N is any maximal sequence of consecutive
zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap
of length 2. The number 529 has binary representation 1000010001 and contains
two binary gaps: one of length 4 and one of length 3. The number 20 has binary
representation 10100 and contains one binary gap of length 1. The number 15 has
binary representation 1111 and has no binary gaps.

Write a function:
    def solution(N)

that, given a positive integer N, returns the length of its longest binary gap.
The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary
representation 10000010001 and so its longest binary gap is of length 5.

Assume that:

    N is an integer within the range [1..2,147,483,647].

Complexity:

    expected worst-case time complexity is O(log(N));
    expected worst-case space complexity is O(1).
"""

# Code

def solution(N):
    b_number = bin(N)[2:]
    zero_seq = []
    length = 0

    for digit in b_number:
        if digit != "1":
            length += 1
        else:
            zero_seq.append(length)
            length = 0

    return max(zero_seq)

# Verification

if __name__ == "__main__":
    assert solution(1041) == 5
    assert solution(15) == 0
    assert solution(1) == 0
    assert solution(5) == 1
    assert solution(2147483647) == 0
    assert solution(6) == 0
    assert solution(328) == 2
    assert solution(16) == 0
    assert solution(1024) == 0
    assert solution(9) == 2
    assert solution(11) == 1
    assert solution(19) == 2
    assert solution(42) == 1
    assert solution(1162) == 3
    assert solution(51712) == 2
    assert solution(20) == 1
    assert solution(561892) == 3
    assert solution(66561) == 9
    assert solution(6291457) == 20
    assert solution(74901729) == 4
    assert solution(805306373) == 25
    assert solution(1376796946) == 5
    assert solution(1073741825) == 29
    assert solution(1610612737) == 28
