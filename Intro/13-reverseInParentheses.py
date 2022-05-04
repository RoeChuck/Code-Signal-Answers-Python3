# reverseInParentheses
# Write a function that reverses characters in (possibly nested) parentheses in the input string.

# Input strings will always be well-formed with matching ()s.

# Example

# For inputString = "(bar)", the output should be
# solution(inputString) = "rab";
# For inputString = "foo(bar)baz", the output should be
# solution(inputString) = "foorabbaz";

# My solution:

import time


def sln1(inS):
    start_time = time.time()
    input_list = list(inS)
    ans = []
    for i in inS:
        if i == ")":
            temp_stack = []
            while ans[-1] != "(":  # Very neat trick to reverse and paste
                temp_stack += ans.pop()
            ans.pop()
            ans.extend(temp_stack)
        else:
            ans.append(i)
    end_time = time.time()
    return ("".join(ans), end_time - start_time)

# there are multiple ways to do this, you could also check for occurance of '(' and set a start index and ')' as end
# index and flip, and use recursion to solve it. It would look something like this (not my solution):


def sln2(s):
    start_time = time.time()
    for i, v in enumerate(s):
        if v == "(":
            start = i
        if v == ")":
            end = i
            return sln2(s[:start] + s[start+1:end][::-1] + s[end+1:])
    end_time = time.time()
    return (s, end_time-start_time)

# sln2 is has better time complexity, using the time module to verify
# print(sln2("fsf(fsiftdfjd(sdfsqf(fdsedf)fysfd)fsdfsdf)fdshsg"))
