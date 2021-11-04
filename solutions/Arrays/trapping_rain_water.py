""" 
Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

Example 1:
    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:
    Input: height = [4,2,0,3,2,5]
    Output: 9

https://leetcode.com/problems/trapping-rain-water
"""
from typing import List

"""

3               |
2        |      | |   |
1   |    ||   | | | | | |
0 0,1,0,2,1,0,1,3,2,1,2,1

5           |
4 |         |
3 |     |   |
2 | |   | | |
1 | |   | | |
 [4,2,0,3,2,5]


"""


# O(N) space | O(N) time
class Solution:
    def trap(self, height: List[int]):
        """
        - the water stored at a particular height is
            - min(max_left, max_height) - height  # negatives are ignored
        - the max of the furthest ends are the furthest ends heights
        """
        total_water = 0

        # calculate max heights
        max_left = height[:]
        max_right = height[:]
        for idx in range(1, len(height)):
            max_left[idx] = max(height[idx], max_left[idx-1])
        for idx in reversed(range(len(height)-1)):
            max_right[idx] = max(height[idx], max_right[idx+1])

        # calculate water above
        for idx, curr_height in enumerate(height):
            water = min(max_left[idx], max_right[idx]) - curr_height
            if water > 0:
                total_water += water

        return total_water


"""

"""


# O(1) space | O(N) time
class Solution_:
    def trap(self, height: List[int]):
        """
        - maintain max left & right on the go:
            - https://youtu.be/ZI2z5pq0TqA?t=663
            - https://youtu.be/C8UjlJZsHBw?t=1413

        - have a left and right pointer at each end of the array
        - if one pointer (small_pointer) has a value less than the other:
            * the water on small_pointer's next will be most affected by small_pointer as we consider min(max_left, max_height)
            * another way we can think about this is that we can try to increase the small_pointer's value
            - move that pointer forward
            - and record (where we have moved to)'s water
        """
        total_water = 0

        max_left, max_right = height[0],  height[-1]
        left, right = 0, len(height)-1
        while left < right:
            # # left smaller
            if height[left] < height[right]:
                max_left = max(height[left], max_left)
                # calculate water at next position - remember that we know that the water at the right is greater than this
                water_at_next = max_left - height[left+1]
                if water_at_next > 0:
                    total_water += water_at_next
                # move forward
                left += 1

            # # right smaller
            else:
                max_right = max(height[right], max_right)
                # calculate water at next position - remember that we know that the water at the right is equal to/greater than this
                water_at_next = max_right - height[right-1]
                if water_at_next > 0:
                    total_water += water_at_next
                # move forward
                right -= 1

        return total_water
