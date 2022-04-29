# Thought of this nice one line solution using max function, list comprehension, and the zip function
def solution(input_array):
    return max([a * b for (a, b) in zip(input_array[1:], input_array[:-1])])
