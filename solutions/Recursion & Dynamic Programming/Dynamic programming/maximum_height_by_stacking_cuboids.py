""" 
Maximum Height by Stacking Cuboids
(Not worth your time lol)

Given n cuboids where the dimensions of the ith cuboid is cuboids[i] = [widthi, lengthi, heighti] (0-indexed). 
Choose a subset of cuboids and place them on each other.

You can place cuboid i on cuboid j if widthi <= widthj and lengthi <= lengthj and heighti <= heightj. 
You can rearrange any cuboid's dimensions by rotating it to put it on another cuboid.

Return the maximum height of the stacked cuboids.

https://leetcode.com/problems/maximum-height-by-stacking-cuboids/

Based on:
    Longest Increasing Subsequence: https://leetcode.com/problems/longest-increasing-subsequence
    Russian Doll Envelopes: https://leetcode.com/problems/russian-doll-envelopes/
"""

""" 
https://leetcode.com/problems/maximum-height-by-stacking-cuboids/discuss/970364/Python-Top-Down-DP
https://leetcode.com/problems/maximum-height-by-stacking-cuboids/discuss/970293/JavaC%2B%2BPython-DP-Prove-with-Explanation
https://leetcode.com/problems/maximum-height-by-stacking-cuboids/discuss/971046/Formal-Proof-for-Greedy-Sorting-Dimensions
"""


class Solution:
    def maxHeight(self, cuboids):
        for cuboid in cuboids:
            cuboid.sort()
        return self.longest_increasing_subsequence(cuboids)

    def longest_increasing_subsequence(self, cuboids):
        result = 0
        cuboids.sort()

        cache = [None]*len(cuboids)
        # subsequence can start at any element
        for idx in range(len(cuboids)):
            result = max(self.lis_helper(cuboids, idx, cache), result)

        return result

    def lis_helper(self, cuboids, idx, cache):
        if cache[idx] is not None:
            return cache[idx]
        result = cuboids[idx][2]

        for i in reversed(range(idx+1, len(cuboids))):
            curr = cuboids[idx]
            nxt = cuboids[i]

            if curr[0] <= nxt[0] and curr[1] <= nxt[1] and curr[2] <= nxt[2]:
                result = max(
                    curr[2]+self.lis_helper(cuboids, i, cache),
                    result
                )

        cache[idx] = result
        return cache[idx]
