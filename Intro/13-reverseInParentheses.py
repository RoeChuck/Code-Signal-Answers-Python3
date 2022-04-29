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
            temp_stack = []
            while ans[-1] != "(":
                temp_stack += ans.pop()
            ans.pop()
            ans.extend(temp_stack)
        else:
            ans.append(i)
    return "".join(ans)

# there are multiple ways to do this, you could also check for occurance of '(' and set a start index and ')' as end
# index and flip, and use recursion to solve it. It would look something like this (not my solution):


def sln2(s):
    for i in range(len(s)):
        if s[i] == "(":
            start = i
        if s[i] == ")":
            end = i
            return sln2(s[:start] + s[start+1:end][::-1] + s[end+1:])
    return s


print(sln2("fsf(fsiftdfjd(sdfsqf(fdsedf)fysfd)fsdfsdf)fdshsg"))
