# Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).

# Example

# For inputString = "crazy", the output should be solution(inputString) = "dsbaz".


alphabet_list = list("abcdefghijklmnopqrstuvwxyza") # add a after z

def solution(inputString):
    solution_string = ""
    for letter in inputString:
        new_letter = alphabet_list[alphabet_list.index(letter) + 1]
        solution_string += new_letter
    return solution_string
    