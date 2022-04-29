
"""
# All Longest Strings
# Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
solution(inputArray) = ["aba", "vcd", "aba"].

"""
# Straightforward 2 liner


def solution(input_array):
    max_length = max([len(str(a)) for a in input_array])
    return [e for e in input_array if len(e) == max_length]
