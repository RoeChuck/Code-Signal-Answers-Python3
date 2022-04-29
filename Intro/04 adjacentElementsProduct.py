# Thought of this nice one line solution using max function, list comprehension, and the zip function
def solution(inputArray):
    return max([a * b for (a, b) in zip(inputArray[1:], inputArray[:-1])])
