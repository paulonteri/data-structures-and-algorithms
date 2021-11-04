""" 
Largest Rectangle in Histogram/Largest Rectangle Under Skyline:

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, 
return the area of the largest rectangle in the histogram.

Example 1:
    Input: heights = [2,1,5,6,2,3]
    Output: 10
    Explanation: 5*2 The above is a histogram where width of each bar is 1.
    The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:
    Input: heights = [2,4]
    Output: 4 => 2*2
Example 3:
    heights = [1, 3, 3, 2, 4, 1, 5, 3, 2]
    9

    Below is a visual representation of the sample input.
                 _
             _  | |
       _ _  | | | |_
      | | |_| | | | |_
     _| | | | |_| | | |
    |_|_|_|_|_|_|_|_|_|
"""

#

"""
Brute force:
- for every building, expand outward
"""

"""
- for each height try to find out where it started and calculate the height

- keep track of the largest valid building up to that point:
    - that can still make rectangles
    - the stack will only conttain buildings that can continue expanding to the right

[0,1,2,3,4,5]
[2,1,5,6,2,3]

stack = []

n,  r,s(i,n)
2,[(0,2)]2*1,
1,[(0,1)] # one is in the prev two, 1*2,
5,[(0,1),(2,5)],5*1,1*3
6,[(0,1),(2,5),(3,6)],6*1,5*2,1*4
2,[(0,1),(2,2)],2*3,1*5
3,[(0,1),(2,2),(5,3)],3*1,1*5,2*4


remaining in stack: [(0,1),(2,2),(5,3)]
3*1
2*4
1*5

"""


class RectangleInfo:
    def __init__(self, start_idx, height):
        self.start_idx = start_idx  # far right bound of building
        self.height = height

    def get_area(self, end_idx):
        return (end_idx-self.start_idx + 1) * self.height


class Solution:
    def largestRectangleArea(self, heights):
        max_area = 0
        stack = []

        for idx, height in enumerate(heights):

            # # determine left bound of curr height
            start_idx = idx

            # remove invalid buildings (that cannot be expanded to the right)
            while stack and height < stack[-1].height:
                removed = stack.pop()
                # calculate the area from when the removed was lat valid (using the last valid index)
                max_area = max(max_area, removed.get_area(idx-1))
                # our current rectangle can start from there
                start_idx = removed.start_idx

            stack.append(RectangleInfo(start_idx, height))

        # # empty stack
        while stack:
            removed = stack.pop()
            max_area = max(max_area, removed.get_area(len(heights)-1))

        return max_area
