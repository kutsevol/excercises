# coding: utf-8
# Task description

"""
Write a function:

    def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the
range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3,
because there are three numbers divisible by 2 within the range [6..11],
namely 6, 8 and 10.

Assume that:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.

Complexity:

expected worst-case time complexity is O(1);
expected worst-case space complexity is O(1).
"""

# Code

def solution(A, B, K):
    return B / K - A / K + ( 1 if A % K == 0 else 0 )

# Verification

if __name__ == "__main__":
    assert solution(6, 11, 2) == 3
    assert solution(11, 345, 17) == 20
    assert solution(0, 0, 11) == 1
    assert solution(10, 10, 5) == 1
    assert solution(100, 123000000, 2) == 61499951
    assert solution(101, 123000000, 10000) == 12300
