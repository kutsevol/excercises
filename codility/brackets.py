# coding: utf-8
# Task description

"""
A string S consisting of N characters is considered to be properly nested if
any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

    def solution(S)

that, given a string S consisting of N characters, returns 1 if S is properly
nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given
S = "([)()]", the function should return 0, as explained above.

Assume that:

N is an integer within the range [0..200,000];
string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".

Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
"""

# Code

def solution(S):
    s = []
    b = {"(": ")", "{": "}", "[": "]"}
    for i in S:
        if i in b:
            s.append(b[i])
        elif i in b.values():
            if not s:
                return 0
            elif s.pop() != i:
                return 0
    if not s:
        return 1
    else:
        return 0

# Verification

if __name__ == "__main__":
    assert solution("{{{{") == 0
    assert solution(")(") == 0
    assert solution("") == 1
    assert solution("{[()()]}") == 1
    assert solution("([)()]") == 0