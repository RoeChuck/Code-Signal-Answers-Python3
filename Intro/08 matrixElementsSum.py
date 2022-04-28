# matrixElementsSum
"""
After becoming famous, the CodeBots decided to move into a new building together. Each of the rooms has a different cost, and some of them are free, but there's a rumour that all the free rooms are haunted! Since the CodeBots are quite superstitious, they refuse to stay in any of the free rooms, or any of the rooms below any of the free rooms.
Given matrix, a rectangular matrix of integers, where each value represents the cost of the room, your task is to return the total sum of all rooms that are suitable for the CodeBots (ie: add up all the values that don't appear below a 0).
"""

# iterate virtically by keeping col in outer loop and iterate through each row, moving down the col until
# you reach the 0 at which point you break the inner loop and move to the next column, thereby excluding
# elements below 0 in the sum.
def solution(matrix):
    sum = 0
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            if matrix[row][col] != 0:
                sum += matrix[row][col]
            else:
                break
    return sum