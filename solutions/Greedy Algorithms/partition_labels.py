""" 
763. Partition Labels

You are given a string s. 
We want to partition the string into as many parts as possible so that each letter appears in at most one part.
Return a list of integers representing the size of these parts.

Example 1:
    Input: s = "ababcbacadefegdehijhklij"
    Output: [9,7,8]
    Explanation:
        The partition is "ababcbaca", "defegde", "hijhklij".
        This is a partition so that each letter appears in at most one part.
        A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:
    Input: s = "eccbbbbdec"
    Output: [10]

https://leetcode.com/problems/partition-labels/
Prerequisite: https://leetcode.com/problems/merge-intervals    
"""


""" 
Solution:

Let's try to repeatedly choose the smallest left-justified partition. 
Consider the first label, say it's 'a'. 
The first partition must include it, and also the last occurrence of 'a'. 
However, between those two occurrences of 'a', there could be other labels that make the minimum size of this partition bigger. 
    For example, in "abccaddbeffe", the minimum first partition is "abccaddb". 
This gives us the idea for the algorithm: For each letter encountered, process the last occurrence of that letter, extending the current partition [anchor, j] appropriately.
"""


# O(n) time | O(1) space
class Solution:
    def partitionLabels(self, s: str):
        """ 
        Divide string into intervals/partitions and merge overlapping intervals.
        """
        result = []

        # mark the last index of each character
        last_pos = {}
        for idx, char in enumerate(s):
            last_pos[char] = idx

        # divide the characters into partitions
        partition_start = 0
        partition_end = 0
        for idx, char in enumerate(s):

            # if outside the current partition, save the prev partition length & start a new one
            if idx > partition_end:
                result.append(partition_end-partition_start+1)
                # start new partition
                partition_end = idx
                partition_start = idx

            # update the end of the partition
            partition_end = max(last_pos[char], partition_end)

            # once we find a pertition that ends at the last character, save it
            if partition_end == len(s)-1:
                # save the last partition
                result.append(partition_end-partition_start+1)
                return result

        return result
