""" 
Minimum Number of Taps to Open to Water a Garden

There is a one-dimensional garden on the x-axis. The garden starts at the point 0 and ends at the point n. (i.e The length of the garden is n).
There are n + 1 taps located at points [0, 1, ..., n] in the garden.
Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed) means the i-th tap can water the area [i - ranges[i], i + ranges[i]] if it was open.
Return the minimum number of taps that should be open to water the whole garden, If the garden cannot be watered return -1.

Example 1:
    Input: n = 5, ranges = [3,4,1,1,0,0]
    Output: 1
    Explanation: The tap at point 0 can cover the interval [-3,3]
        The tap at point 1 can cover the interval [-3,5]
        The tap at point 2 can cover the interval [1,3]
        The tap at point 3 can cover the interval [2,4]
        The tap at point 4 can cover the interval [4,4]
        The tap at point 5 can cover the interval [5,5]
        Opening Only the second tap will water the whole garden [0,5]
Example 2:
    Input: n = 3, ranges = [0,0,0,0]
    Output: -1
    Explanation: Even if you activate all the four taps you cannot water the whole garden.
Example 3:
    Input: n = 7, ranges = [1,2,1,0,2,1,0,1]
    Output: 3
Example 4:
    Input: n = 8, ranges = [4,0,0,0,0,0,0,0,4]
    Output: 2
Example 5:
    Input: n = 8, ranges = [4,0,0,0,4,0,0,0,4]
    Output: 1

https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden
"""


""" 

Prerequisites:
- https://leetcode.com/problems/jump-game
- https://leetcode.com/problems/jump-game-ii
- https://leetcode.com/problems/video-stitching


https://www.notion.so/paulonteri/Greedy-Algorithms-b9b0a6dd66c94e7db2cbbd9f2d6b50af#d7578cbb76c7423d9c819179fc749be5
https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/discuss/506853/Java-A-general-greedy-solution-to-process-similar-problems
"""


class Solution_:
    def minTaps(self, n, ranges):
        taps = 0

        # # Save the right-most possible jump for each left most index
        jumps = [-1]*(n)
        for idx, num in enumerate(ranges):
            if num == 0:
                continue
            left_most = max(0, idx-num)
            right_most = min(n, idx+num)

            jumps[left_most] = max(jumps[left_most], right_most)

        # # Jump Game II
        current_jump_end = 0
        furthest_can_reach = -1  # furthest jump we made/could have made
        for idx, right_most in enumerate(jumps):

            # we continuously find the how far we can reach in the current jump
            # record the futhest point accessible in our current jump
            furthest_can_reach = max(right_most, furthest_can_reach)

            # if we have come to the end of the current jump, we need to make another jump
            # the new  jump should start immediately after the old jump
            if idx == current_jump_end:
                # if we cannot make a jump and we need to make a jump to increase the furthest_can_reach
                if right_most == -1 and furthest_can_reach <= idx:
                    return -1
                # move end to the furthest possible point
                current_jump_end = furthest_can_reach
                taps += 1

        if furthest_can_reach == n:
            return taps
        return -1


class Solution:
    def minTaps(self, n, ranges):
        taps = 0

        # # Save the right-most possible jump for each left most index
        jumps = [-1]*(n)
        for idx, num in enumerate(ranges):
            if num == 0:
                continue
            left_most = max(0, idx-num)
            right_most = min(n, idx+num)

            jumps[left_most] = max(jumps[left_most], right_most)

        # # Jump Game II
        idx = 0
        furthest_can_reach = -1  # furthest jump we made/could have made
        while idx < n:

            # # create a new jump
            furthest_can_reach = max(jumps[idx], furthest_can_reach)
            # check if we can make a valid jump
            if jumps[idx] == -1 and furthest_can_reach <= idx:
                # if we cannot make a jump and we need to make a jump to increase the furthest_can_reach
                return -1
            # make jump - move end to the furthest possible point
            taps += 1
            current_jump_end = furthest_can_reach

            idx += 1

            # # reach end of jump
            while idx < n and idx < current_jump_end:
                # we continuously find the how far we can reach in the current jump
                # record the futhest point accessible in our current jump
                furthest_can_reach = max(jumps[idx], furthest_can_reach)
                idx += 1

        if furthest_can_reach == n:
            return taps
        return -1
