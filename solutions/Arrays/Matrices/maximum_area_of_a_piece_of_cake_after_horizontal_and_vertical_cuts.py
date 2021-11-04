""" 
Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts

You are given a rectangular cake of size h x w and two arrays of integers horizontalCuts and verticalCuts where:
    horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, and
    verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.
Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. 
Since the answer can be a large number, return this modulo 109 + 7.

https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/
https://www.notion.so/paulonteri/Strings-Arrays-Linked-Lists-81ca9e0553a0494cb8bb74c5c85b89c8#c51d21f8b5a045929217972310435c1b
"""


class Solution:
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """ 
        Note that: If we were to consider only the horizontal cuts, then we would end up with many pieces of cake with width = w and varying heights. 
        For each new piece, making a vertical cut will change the width, but not the height.
        - when considering the heights, once we find the largest height, that piece is applicable to all the different possible widths
        - when considering the widths, once we find the largest width, that piece is applicable to all heights

        Therefore, we know the largest piece of cake must have a height equal to the tallest height after applying only the horizontal cuts, 
        and it will have a width equal to the widest width after applying only the vertical cuts.
        """

        # Start by sorting the inputs
        horizontalCuts.sort()
        verticalCuts.sort()

        max_height = max(horizontalCuts[0], h - horizontalCuts[-1])
        for i in range(1, len(horizontalCuts)):
            max_height = max(max_height,
                             horizontalCuts[i] - horizontalCuts[i - 1])

        max_width = max(verticalCuts[0], w - verticalCuts[-1])
        for i in range(1, len(verticalCuts)):
            max_width = max(max_width, verticalCuts[i] - verticalCuts[i - 1])

        return (max_height * max_width) % (10**9 + 7)
