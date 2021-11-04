""" 
Video Stitching

You are given a series of video clips from a sporting event that lasted time seconds. 
These video clips can be overlapping with each other and have varying lengths.
Each video clip is described by an array clips where clips[i] = [starti, endi] indicates that the ith clip started at starti and ended at endi.
We can cut these clips into segments freely.
For example, a clip [0, 7] can be cut into segments [0, 1] + [1, 3] + [3, 7].
Return the minimum number of clips needed so that we can cut the clips into segments that cover the entire sporting event [0, time]. 
If the task is impossible, return -1.

Example 1:
    Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], time = 10
    Output: 3
    Explanation: 
        We take the clips [0,2], [8,10], [1,9]; a total of 3 clips.
        Then, we can reconstruct the sporting event as follows:
        We cut [1,9] into segments [1,2] + [2,8] + [8,9].
        Now we have segments [0,2] + [2,8] + [8,10] which cover the sporting event [0, 10].
Example 2:
    Input: clips = [[0,1],[1,2]], time = 5
    Output: -1
    Explanation: We can't cover [0,5] with only [0,1] and [1,2].
Example 3:
    Input: clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], time = 9
    Output: 3
    Explanation: We can take clips [0,4], [4,7], and [6,9].
Example 4:
    Input: clips = [[0,4],[2,8]], time = 5
    Output: 2
    Explanation: Notice you can have extra video after the event ends.

https://leetcode.com/problems/video-stitching
"""


""" 

Prerequisites:
- https://leetcode.com/problems/jump-game
- https://leetcode.com/problems/jump-game-ii


https://www.notion.so/paulonteri/Greedy-Algorithms-b9b0a6dd66c94e7db2cbbd9f2d6b50af#d7578cbb76c7423d9c819179fc749be5
https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/discuss/506853/Java-A-general-greedy-solution-to-process-similar-problems
"""


class SolutionDP:
    def videoStitching(self, clips, time):
        clips.sort()

        dp = [float('inf')] * (time+1)
        dp[0] = 0

        for left, right in clips:
            # ignore ranges that will be greater than the time
            if left > time:
                continue

            # reach every point possible
            for idx in range(left, min(right, time)+1):
                # steps to reach idx = min((prevoiusly recorded), (steps to reach left + the one step to idx))
                dp[idx] = min(dp[idx], dp[left]+1)

        if dp[-1] == float('inf'):
            return -1
        return dp[-1]


class Solution:
    def videoStitching(self, clips, T):
        result = 0

        # # Save the right-most possible valid jump for each left most index
        max_jumps = [-1]*(T+1)
        for left, right in clips:
            if left > T:
                continue
            if right-left <= 0:
                continue
            max_jumps[left] = max(max_jumps[left], min(right, T))

        # Jump Game II: it is then a jump game
        idx = 0
        current_jump_end = 0
        furthest_jump = 0  # furthest jump we made/could have made
        while idx < T:

            # # create a new jump
            furthest_jump = max(max_jumps[idx], furthest_jump)
            # check if we can make a valid jump
            if max_jumps[idx] == -1 and furthest_jump <= idx:
                # if we cannot make a jump and we need to make a jump to increase the furthest_jump
                return -1
            # make jump - move end to the furthest possible point
            result += 1
            current_jump_end = furthest_jump

            idx += 1

            # # reach end of jump
            while idx <= T and idx < current_jump_end:
                # we continuously find the how far we can reach in the current jump
                # record the futhest point accessible in our current jump
                furthest_jump = max(max_jumps[idx], furthest_jump)
                idx += 1

        return result
