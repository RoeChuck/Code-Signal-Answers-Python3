# In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.

# Example

# For

# matrix = [[true, false, false],
#           [false, true, false],
#           [false, false, false]]
# the output should be

# solution(matrix) = [[1, 2, 1],
#                        [2, 1, 1],
#                        [1, 1, 1]]


def solution(matrix):
    result = [[0] * len(matrix[0])
              for row in matrix]  # 0 for every element in matrix
    row = range(len(matrix))
    column = range(len(matrix[0]))
    for x in row:
        for y in column:
            if matrix[x][y]:  # now we add 1 to its neighbours, but not itself
                for dx in range(x - 1, x + 2):  # includes 1 row up and 1 row down
                    # includes 1 column right and one column left
                    for dy in range(y - 1, y + 2):
                        if dx < 0 or dy < 0 or (dx == x and dy == y):
                            # excludes negative values to be used as index
                            # also excludes the 'true' index to not add to its own cell
                            continue
                        else:
                            try:
                                result[dx][dy] += 1  # add 1 to the neighbours
                            except IndexError:  # this occurs at the rightmost/ last column and the bottom/ last row
                                # excluding negative values takes care of the first row/ column
                                continue
    return result
