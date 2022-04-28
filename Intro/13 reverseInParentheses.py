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

def solution(inputString):
    input_list = list(inputString)
    answer = []
    for i in inputString:
        if i == ")":
            temp_stack = []
            while answer[-1] != "(":
                temp_stack += answer.pop()
            answer.pop()
            answer.extend(temp_stack)
        else:
            answer.append(i)
    return "".join(answer)