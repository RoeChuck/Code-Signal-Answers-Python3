# Last night you partied a little too hard. Now there's a black and white photo of you that's about to go viral! You
# can't let this ruin your reputation, so you want to apply the box blur algorithm to the photo to hide its content.

# The pixels in the input image are represented as integers. The algorithm distorts the input image in the following
# way: Every pixel x in the output image has a value equal to the average value of the pixel values from the 3 × 3 square that has its center at x, including x itself. All the pixels on the border of x are then removed.

# Return the blurred image as an integer, with the fractions rounded down.

# Example

# For

# image = [[1, 1, 1],
#          [1, 7, 1],
#          [1, 1, 1]]
# the output should be solution(image) = [[1]].

# To get the value of the middle pixel in the input 3 × 3 square: (1 + 1 + 1 + 1 + 7 + 1 + 1 + 1 + 1) = 15 / 9 =
# 1.66666 = 1. The border pixels are cropped from the final result.

def solution(matrix):
    tt_vals = []  # all values within each 3 x 3 matrix
    tt_avg = []  # all the avgs of values
    final = []  # avgs formatted correctly

    # to add to the tt_vals how many times it's appended depends on the matrix dimension
    # if 3 x 3, both loops will run once, adding all the values into tt_vals
    # if r x c then outer loop runs r - 2 times and the inner loop c - 2 times
    for row in range(len(matrix) - 2):
        for column in range(len(matrix[row]) - 2):
            # Appends a list within a list r - 2 times
            tt_vals.append([
        matrix[row][column], matrix[row][column + 1], matrix[row][column + 2],
        matrix[row + 1][column], matrix[row + 1][column + 1], matrix[row + 1][column + 2],
        matrix[row + 2][column],matrix[row + 2][column + 1], matrix[row + 2][column + 2] 
      ])
    # append avg of each list element from tt_vals to tt_avg
    for x in range(len(tt_vals)):
        tt_avg.append(int(sum(tt_vals[x]) / len(tt_vals[x])))
    for i in range(0, len(tt_avg), (len(matrix[0]) - 2)): # formats tt_avs to be a 2d array (matrix)
        final.append(tt_avg[i:i + (len(matrix[0]) - 2)])
        # given a 4 x 4 matrix, tt_vals would contain 2 x 2 list elements
        # avg would contain 4 values
        # last loop would iterate twice with 0 and 2 and add avg[0, 2] first then avg[2, 4], making a 2d array
    return final
