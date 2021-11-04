"""
Rotate Image/Rotate Matrix:

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

https://leetcode.com/problems/rotate-image/
"""


from typing import List


class Solution:
    def rotate(self, matrix):
        height, width = len(matrix), len(matrix[0])

        top = 0
        right = width - 1
        left = 0
        bottom = height - 1

        while left <= right or top <= bottom:

            # swap
            # for idx in range(left, right+1): did not skip last element in every iteration
            for idx in range(left, right):

                prev_top = matrix[top][idx]
                prev_right = matrix[idx][right]
                prev_bottom = matrix[bottom][(width-1)-idx]
                prev_left = matrix[(height-1)-idx][left]

                matrix[idx][right] = prev_top
                matrix[bottom][(width-1)-idx] = prev_right
                matrix[(height-1)-idx][left] = prev_bottom
                matrix[top][idx] = prev_left

            # move perimeter inwards
            top += 1
            right -= 1
            bottom -= 1
            left += 1
        print(matrix)


x = Solution()
x.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
x.rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])
"""


Input: matrix
Output: same matrix
Constraints:
    - must be done in place
Assumptions:
    - matrix will never be empty
    - matrix will contain integers only
    - matrix is not sorted
Edge cases:
    - matrix with one element
    
# we need to figure out:
- how to move:
    top -> right
    right -> bottom
    bottom -> left
    left -> top
- keep track of prev: top, right, left, bottom

# # First Approach:
- iterate through every element in the array
- have top, right, bottom, left variables thet will show where we are in the perimeter
- have a temp array thet will store replaced values
## while loop: (one perimeter at a time)
    # top -> right:
        - move the characters in the top to the right
        - this is done while storing the right elements in an array
        - right -= 1
    # right -> bottom:
        - get the right elements from the temp array
        - move the characters in the right to the bottom
        - this is done while storing the bottom elements in an array
        - bottom -= 1
    # bottom -> left:
        - get the bottom elements from the temp array
        - move the characters in the bottm to the left
        - this is done while storing the left elements in an array
        - left -= 1
    # left -> top:
        - get the left elements from the temp array
        - move the characters in the left to the top
        - bottom -= 1
# O(n.m) time | O(m) space - where n = len(maytrix), m = len(matrix[0])

# # Second Approach:
- swap/shift first/second/nth element to be moved of the top, right, left, bottom at the same time
- we will start at :   ( height = len(matrix), width = len(matrix[0]) )
    top [0][0], right [0][width-1], bottom [height-1][width-1], left [height-1][0]
    top [0][1], right [1][width-1], bottom [height-1][width-2], left [height-2][0]
    ... till we finish the perimeter
- do this till we reach the end of each (which will happen at the same time for all)
- repeat the process for the inner perimeter
# O(n.m) time | O(1) space - where n = len(maytrix), m = len(matrix[0])
        
"""


class Solution0:
    def rotate(self, matrix: List[List[int]]):
        length = len(matrix)

        top = left = 0
        right = bottom = length - 1
        while left <= right or top <= bottom:

            # work on current perimeter
            for idx in range(left, right):

                top_val = matrix[top][idx]
                right_val = matrix[idx][right]
                bottom_val = matrix[bottom][(length-1)-idx]
                left_val = matrix[(length-1)-idx][left]

                # top
                matrix[top][idx] = left_val
                # right
                matrix[idx][right] = top_val
                # bottom
                matrix[bottom][(length-1)-idx] = right_val
                # left
                matrix[(length-1)-idx][left] = bottom_val

            # move perimeter inwards
            top += 1
            right -= 1
            left += 1
            bottom -= 1


"""
[
[5, 1, 9, 11],
[2, 4, 8, 10],
[13,3, 6, 7],
[15,14,12,16]
]
"""
