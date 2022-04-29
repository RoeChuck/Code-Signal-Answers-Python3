# array Maximal Adjacent Difference
# Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

# Example

# For inputArray = [2, 4, 1, 0], the output should be
# solution(inputArray) = 3.

def solution(inputArray):
    # make list comprehension of absolute difference between 2 adjecent element using zip
    # get max
    return max([abs(a-b) for (a, b) in zip(inputArray[1:], inputArray[:-1])])