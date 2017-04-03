# coding: utf-8
# Task description

"""
Write a function:

    def solution(A)

that, given a non-empty zero-indexed array A of N integers, returns the minimal
positive integer (greater than 0) that does not occur in A.

For example, given:

  A[0] = 1
  A[1] = 3
  A[2] = 6
  A[3] = 4
  A[4] = 1
  A[5] = 2

the function should return 5.

Assume that:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].

Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).

Elements of input arrays can be modified.
"""

# Code

def solution(arr):
    arr = filter(lambda x: x > 0, arr)
    arr.sort()

    if not arr or arr[0] != 1:
        return 1

    found = { 1: False }

    for c in arr:
        found[c] = True
        found.setdefault(c+1, False)

    return min([n for n,f in found.iteritems() if not f])

# Verification

if __name__ == "__main__":
    assert solution([1, 6, 3, 4, 1, 2]) == 5
    assert solution([-1, -4, -3, -5, -2]) == 1
    assert solution(xrange(-100, -1)) == 1

    from random import shuffle
    seq = range(100) + range(102, 200)
    shuffle(seq)
    assert solution(seq) == 100
