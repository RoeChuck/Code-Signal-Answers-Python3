# isLucky
"""
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first 
half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
solution(n) = true;
For n = 239017, the output should be
solution(n) = false.
"""


def solution(n):
    return sum([int(a) for a in str(n)[0:len(str(n))//2:]]) == sum([int(a) for a in str(n)[(len(str(n))+1)//2:]])

# Might be more readable if written with multiple lines. Independent solution.