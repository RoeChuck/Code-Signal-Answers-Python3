# Used list slicing and set -1 for the interval parameter
# Returns true if inputstring matches reversed inputstring
def solution(inputstring):
    return inputstring == inputstring[::-1]