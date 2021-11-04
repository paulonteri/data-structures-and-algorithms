""" 
Flood Fill:

An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].
To perform a flood fill, consider the starting pixel, 
 plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, 
 plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. 
Replace the color of all of the aforementioned pixels with newColor.
Return the modified image after performing the flood fill.

Example 1:
    Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
    Output: [[2,2,2],[2,2,0],[2,0,1]]
    Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
    Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
Example 2:
    Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
    Output: [[2,2,2],[2,2,2]]

https://leetcode.com/problems/flood-fill/
"""


class Solution:
    def floodFill(self, image, sr, sc, newColor):
        self.fillColor(image, newColor, image[sr][sc],  sr, sc)
        return image

    def fillColor(self, image, newColor, oldColor, row, col):
        if not (row >= 0 and row < len(image) and col >= 0 and col < len(image[0]) and image[row][col] == oldColor):
            return

        # prevent infinite loop if newColor == oldColor
        image[row][col] = "##"

        # up
        self.fillColor(image, newColor, oldColor, row-1, col)
        # down
        self.fillColor(image, newColor, oldColor, row+1, col)
        # left
        self.fillColor(image, newColor, oldColor, row, col-1)
        # right
        self.fillColor(image, newColor, oldColor, row, col+1)

        image[row][col] = newColor  # remove
