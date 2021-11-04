"""
Container With Most Water: (do Best Time to Buy and Sell Stock next)

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
Notice that you may not slant the container.

https://leetcode.com/problems/container-with-most-water/
"""


class SolutionBF:
    def maxArea(self, height):

        max_area = 0

        for idx in range(len(height)):

            for idx_two in range(idx+1, len(height)):

                h = min(height[idx], height[idx_two])
                w = idx_two - idx

                max_area = max(max_area, w*h)

        return max_area


""" 
The intuition behind this approach is that the area formed between the lines will always be limited by the height of the shorter line. 
Further, the farther the lines, the more will be the area obtained.

We take two pointers, one at the beginning and one at the end of the array constituting the length of the lines. 

By placing them at these far ends we are already optimising for width.

Futher, we maintain a variable maxarea to store the maximum area obtained till now. 
At every step, we find out the area formed between them, update maxarea and move the pointer pointing to the shorter line towards the other end by one step.
"""


class Solution:
    def maxArea(self, height):

        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:

            # calculate area
            h = min(height[left], height[right])
            w = right - left
            max_area = max(max_area, h*w)

            # move pointer
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return max_area
