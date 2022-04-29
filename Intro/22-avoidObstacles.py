# You are given an array of integers representing coordinates of obstacles situated on a straight line.

# Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.

# Find the minimal length of the jump enough to avoid all the obstacles.

# Example

# For inputArray = [5, 3, 6, 7, 9], the output should be
# solution(inputArray) = 4.

# My first solution is more complicated than it needs to be:

def solution(inputArray):
    # loop for potential answer, +2 to include one more than the max item
    for p_ans in range(2, max(inputArray) + 2):
        flag = False
        for i in sorted(inputArray):
            if i % p_ans == 0:  # condition1 - i is multiple of p_ans - can't be actual answer
                flag = True
                break
            # condition2- i not multiple of p_ans (p_ans could be ans) - continue to check next i
            elif i % p_ans != 0:
                continue
        if flag == True:  # condition1: check with next p_ans
            continue
        else:  # condition 2: return p_ans bc its the answer
            return p_ans
    return p_ans


# Better way to do this:
def notmysolution(inputArray):
    c = 2
    while True:  # keep looping until you return c
        if all(x % c != 0 for x in inputArray):  # no inputarray element is multiple of c
            return c
        c += 1  # if not all inputarray element is multiple of c, check
