"""
Add Border
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
           "ded"]
the output should be

solution(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
"""


def solution(picture):
    final_output = []
    b = ''

    # add '*' to b (number of columns + 2) times
    for a in range(0, len(picture[0]) + 2):
        b += '*'

    final_output.append(b)  # adds the border to the top

    # add one * on left and right of each row
    for index, value in enumerate(picture):
        final_output.append('*' + value + "*")

    final_output.append(b)  # add border to bottom

    return final_output
