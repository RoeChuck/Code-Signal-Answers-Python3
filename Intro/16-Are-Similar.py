# Are Similar?

# Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of
# the arrays.

# Given two arrays a and b, check whether they are similar.

# Example

# For a = [1, 2, 3] and b = [1, 2, 3], the output should be
# solution(a, b) = true.

# The arrays are equal, no need to swap any elements.

# For a = [1, 2, 3] and b = [2, 1, 3], the output should be
# solution(a, b) = true.

# We can obtain b from a by swapping 2 and 1 in b.

# For a = [1, 2, 2] and b = [2, 1, 1], the output should be
# solution(a, b) = false.

# Any swap of any two elements either in a or in b won't make a and b equal.


def solution(a, b):
    temp_stack = []
    for i, v in enumerate(a):
        if v not in b[i]:
            temp_stack.append(i)
    if len(temp_stack) > 2:
        return False
    elif len(temp_stack) == 0:
        return True
    elif len(temp_stack) == 2:
        if a[temp_stack[0]] == b[temp_stack[1]] and a[temp_stack[1]] == b[temp_stack[0]]:
            return True
        else:
            return False

# Using lots of if statements to check and account for every case while using temp_stack to keep track of the amount of
# mismatches so you can check later if 2 mismatches are the same
# Someone more clever than me had a different way of thinking about it _top codesignal solution_:


def notmysolution(A, B):
    return sorted(A) == sorted(B) and sum([a != b for a, b in zip(A, B)]) <= 2