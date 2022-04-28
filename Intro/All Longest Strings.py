# All Longest Strings
"""
Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
solution(inputArray) = ["aba", "vcd", "aba"].

"""
# Straightforward 2 liner
def solution(inputArray):
    max_length = max([len(str(a)) for a in inputArray])
    return [e for e in inputArray if len(e) == max_length]