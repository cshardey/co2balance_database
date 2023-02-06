# Have the function BitmapHoles(strArr) take the array of strings stored in strArr, which will be a 2D matrix of 0 and 1's, and determine how many holes, or contiguous regions of 0's, exist in the matrix.
# A contiguous region is one where there is a connected group of 0's going in one or more of four directions: up, down, left, or right. For example: if strArr is ["10111", "10101", "11101", "11111"], then this looks like the following matrix:
# Write the code in python

def BitmapHoles(strArr):
    # strArr is a list of strings
    # convert the list of strings to a list of lists
    matrix = [list(row) for row in strArr]
    # initialize the number of holes to 0
    holes = 0

    def BitmapHolesHelper(matrix, row, col):
        # check if the row and col are within the matrix
        if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
            # check if the current cell is a 0
            if matrix[row][col] == '0':
                # set the current cell to 1
                matrix[row][col] = '1'
                # recursively call the helper function on the 4 adjacent cells
                BitmapHolesHelper(matrix, row + 1, col)
                BitmapHolesHelper(matrix, row - 1, col)
                BitmapHolesHelper(matrix, row, col + 1)
                BitmapHolesHelper(matrix, row, col - 1)

    # loop through the rows
    for i in range(len(matrix)):
        # loop through the columns
        for j in range(len(matrix[i])):
            # check if the element is a 0
            if matrix[i][j] == '0':
                # increment the holes
                holes += 1
                # call the recursive function
                BitmapHolesHelper(matrix, i, j)
    return holes


print(BitmapHoles(["01111", "01101", "00011", "11110"]))

# Write the code in python
# This is a python function called 'BitmapHoles' that takes in a list of strings called 'strArr' as an input. The function converts the list of strings into a list of lists called 'matrix'.
#
# The function then defines a variable called 'holes' and initializes it to 0. It also defines a helper function called 'BitmapHolesHelper' which takes in 3 inputs- 'matrix', 'row', 'col'.
#
# The helper function checks if the 'row' and 'col' are within the range of the matrix. If so, it then checks if the current cell is a '0'. If the cell is '0' then it sets the current cell to '1' and recursively calls the helper function on the 4 adjacent cells (top, bottom, left, right) of the current cell.
#
# After that, the main function loops through the rows and columns of the matrix using two nested for loops. Within the nested for loops, the function checks if the element is a '0'. If it is, the function increments the 'holes' variable by 1 and calls the 'BitmapHolesHelper' function on the current cell.
#
# Finally, the function returns the number of holes found in the matrix.
#
# The function uses a recursive approach where it starts from a '0' cell and fills the adjacent '0' cells with '1' and counting the total number of '0' cells (holes) in the matrix.
