# coding: utf-8
# Task description

"""
A zero-indexed array A consisting of N different integers is given.
The array contains integers in the range [1..(N + 1)], which means that exactly
one element is missing.

Your goal is to find that missing element.

Write a function:
    def solution(A)

that, given a zero-indexed array A, returns the value of the missing element.

For example, given array A such that:
    A[0] = 2
    A[1] = 3
    A[2] = 1
    A[3] = 5
the function should return 4, as it is the missing element.

Assume that:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].

Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(1), beyond input storage (not counting the storage required for input arguments).

Elements of input arrays can be modified.
"""

# Code

def solution(A):
    return sum(xrange(1, len(A) + 2)) - sum(A)

# Verification

if __name__ == "__main__":
    from random import choice, shuffle

    def seq_without_one_element(count):
        """ Function for generated sequence without random element.
        :return: sequence, random number
        """
        seq = range (1, count + 1)
        shuffle(seq)
        random_elem = choice(seq)
        seq.remove(random_elem)
        return seq, random_elem

    assert solution([2, 3, 1, 5]) == 4
    assert solution([]) == 1
    assert solution([2]) == 1
    assert solution([3, 5, 4, 1, 2]) == 6
    assert solution([3, 5, 4, 2]) == 1
    assert solution([1, 3]) == 2
    seq, number = seq_without_one_element(10000)
    assert solution(seq) == number
    seq, number = seq_without_one_element(100000)
    assert solution(seq) == number
