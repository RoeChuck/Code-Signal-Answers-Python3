# Array Change

# #You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find 
# the minimal number of moves required to obtain a strictly increasing sequence from the input.

# Example

# For inputArray = [1, 1, 1], the output should be
# solution(inputArray) = 3.

def solution(ar1):
    prev = ar1[0]
    increment_num = 0
    for current in ar1[1:]:
        if prev < current:
            # if prev less than current, set prev to current for the next iteration
            prev = current 
            # if prev never less than current, returns 0 as the increment number
        else:
            # if previous is more or equal to the current, adds the difference plus 1 to increment, which is how many 
            # times you'd have to increment it by to make it 1 more than previous
            increment_num += prev - current + 1 
            prev += 1
    return increment_num 