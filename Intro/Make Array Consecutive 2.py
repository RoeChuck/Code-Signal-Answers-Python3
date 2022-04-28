# Make Array Consecutive 2
# Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an
# non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest
# to largest so that each statue will be bigger than the previous one exactly by 1. He may need some
# additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.
# Example
# For statues = [6, 2, 3, 8], the output should be
# solution(statues) = 3.
# Ratiorg needs statues of sizes 4, 5 and 7.

"""
Use range function to create range object starting from the min element of statues
and ending at the max element + 1 in order to include the last/ max element
subtracting the length of this new list with the length of statues gives the amount of additional elements
in the new list which is the minimum number of statues needed
"""

def solution(statues):
    return len(range(min(statues), max(statues) + 1)) - len(statues)

# A simpler way to do this comes when you realize you can just subtract the max(statues) with min(statues)
# to get the length of the new list that I created above. This is a more efficient way to do this with less
# operations

def solution2(statues):
    return max(statues) - min(statues) - len(statues) + 1