# reverseInParentheses
"""
Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.

Example

For inputString = "(bar)", the output should be
solution(inputString) = "rab";
For inputString = "foo(bar)baz", the output should be
solution(inputString) = "foorabbaz";
"""
# My solution:

from turtle import st


def sln1(inS):
    input_list = list(inS)
    ans = []
    for i in inS:
        if i == ")":
            t_st = []
            while ans[-1] != "(":
                t_st += ans.pop()
            ans.pop()
            ans.extend(t_st)
        else:
            ans.append(i)
    return "".join(ans)

# there are multiple ways to do this, you could also check for occurance of '(' and set a start index and ')' as end 
# index and flip, and use recursion to solve it. It would look something like this (not my solution):

def sln2(iS):
    for i, v in enumerate(iS):
        if v == ")":
            s = i
        if v == "(":
            e = i
            return sln2(iS[:s]+iS[e-1:s:-1]+s[e+1:])
    return s