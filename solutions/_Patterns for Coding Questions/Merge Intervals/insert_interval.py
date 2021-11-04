""" 
Insert Interval

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval 
    and intervals is sorted in ascending order by starti. 
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
Return intervals after the insertion.

Example 1:
    Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
    Output: [[1,5],[6,9]]
Example 2:
    Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
Example 3:
    Input: intervals = [], newInterval = [5,7]
    Output: [[5,7]]
Example 4:
    Input: intervals = [[1,5]], newInterval = [2,3]
    Output: [[1,5]]
Example 5:
    Input: intervals = [[1,5]], newInterval = [2,7]
    Output: [[1,7]]

https://leetcode.com/problems/insert-interval
"""


""" 
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]

1 2 3 4 5 6 7 8 9 10 11 12 13
####
1-2 3---5 6-7 8---10    12----
      4-------8
####
1---3     6-----9
      4-------8
####
     3---5 6-7 8---10
1-2
####
     3---5 6-7 8---10
                      11-12 
###
     
      
- res = []    
- find the insert position (first interval with ending greater than newInterval's start)
    - if None, add newInterval to the end
    - else:
        - add all before the start to res (Add to the output all the intervals starting before newInterval)
        - add all overlaping intervals
          while the current index's start < newInterval's end:
            - update the newInterval's end to be the max of both ends
            - skip it (interval at current index)(move index forward)
"""




from typing import List
class Solution__:
    def insert(self, intervals: List[List[int]], newInterval: List[int]):

        # - Find the insert position (first interval with ending greater than newInterval's start)
        start_idx = -1
        for idx, interval in enumerate(intervals):
            if interval[1] >= newInterval[0]:
                start_idx = idx
                break
        # if None, add newInterval to the end
        if start_idx == -1:
            return intervals + [newInterval]

        # - Add to the output all the intervals starting before newInterval
        before_start = intervals[:start_idx]

        # - Add all overlaping intervals to inserted_interval
        inserted_interval = [
            min(newInterval[0], intervals[start_idx][0]), newInterval[1]
        ]
        idx = start_idx
        while idx < len(intervals) and inserted_interval[1] >= intervals[idx][0]:
            inserted_interval[1] = max(intervals[idx][1], inserted_interval[1])
            idx += 1

        return before_start + [inserted_interval] + intervals[idx:]


""" 

"""


class Solution_:
    def insert(self, intervals: List[List[int]], newInterval: List[int]):

        # - Find the insert position (first interval with ending greater than newInterval's start)
        start_idx = -1
        for idx, interval in enumerate(intervals):
            if interval[1] >= newInterval[0]:
                start_idx = idx
                break
        # if None, add newInterval to the end
        if start_idx == -1:
            return intervals + [newInterval]

        # - Add to the output all the intervals starting before newInterval
        merged = intervals[:start_idx]
        # - Add newInterval to output
        if len(merged) > 0 and newInterval[0] <= merged[-1][1]:
            merged[-1] = self.merge_intervals(newInterval, merged[-1])
        else:
            merged.append(newInterval)

        # - Add to the output all the intervals starting after newInterval
        for idx in range(start_idx, len(intervals)):
            # Merge it with the last added interval if newInterval starts before the last added interval.
            if intervals[idx][0] <= merged[-1][1]:
                merged[-1] = self.merge_intervals(intervals[idx], merged[-1])
            else:
                merged.append(intervals[idx])

        return merged

    def merge_intervals(self, one, two):
        return [min(one[0], two[0]), max(one[1], two[1])]
