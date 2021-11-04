"""
Leetcode 56: Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

Example:
    Input:
        [[8,10],[15,18], [1,3],[2,6]]
        [[1,3],[2,6],[8,10],[15,18]]
        [[1,3]]
        []
        [[1,4],[4,5]]
        [[1,4],[2,3]]
    Output:
        [[1,6],[8,10],[15,18]]
        [[1,6],[8,10],[15,18]]
        [[1,3]]
        []
        [[1,5]]
        [[1,4]]
https://leetcode.com/problems/merge-intervals
"""

from typing import List

""" 
[[6,7], [2,4], [5,9]]

0 1 2 3 4 5 6 7 8 9

    2---4
          5-------9
            6-7
            
- have a res arrray
- sort the intervals by their start value:
- for each interval (curr_interval):
    - if it overlaps the next, merge the next into it (update the curr_intervals end)
        - skip the next (move the index forward)
        - repeat this until we no longer find an overlap
    - add it to res
- return res
"""


class Solution:
    def merge(self, intervals: List[List[int]]):

        merged = []
        intervals.sort(key=lambda x: x[0])

        i = 0
        while i < len(intervals):
            start = intervals[i][0]
            end = intervals[i][1]
            while i < len(intervals)-1 and end >= intervals[i+1][0]:
                i += 1
                end = max(end, intervals[i][1])

            merged.append([start, end])
            i += 1

        return merged


class Solution2:
    def merge(self, intervals: List[List[int]]):

        # sort
        intervals.sort(key=lambda item: item[0])

        i = 0
        # no need to check the last array
        while (i + 1) < len(intervals):

            curr_a = intervals[i]
            next_a = intervals[i+1]

            # check for overlap
            if curr_a[1] >= next_a[0]:

                # merge
                # we use max coz of such a case: [[1,4],[2,3]]
                # make the last element of the first array be the furthest(largest value)
                intervals[i][1] = max(curr_a[1], next_a[1])

                # delete the second array
                intervals.pop(i+1)

            else:
                i += 1

        return intervals


""" 
Merge Intervals:

Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

Example 1:
    Intervals: [[1,4], [2,5], [7,9]]
    Output: [[1,5], [7,9]]
    Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into one [1,5].
Example 2:
    Intervals: [[6,7], [2,4], [5,9]]
    Output: [[2,4], [5,9]]
    Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].
Example 3:
    Intervals: [[1,4], [2,6], [3,5]]
    Output: [[1,6]]
    Explanation: Since all the given intervals overlap, we merged them into one.
"""

""" 
Solution:

[[6,7], [2,4], [5,9]]

sort
[[2,4], [5,9], [6,7]]
merge
[[2,4], [5,9]]




- so that its easier to know what comes b4 what, we should sort the intervals by their starting interval
- we can then check if a particular interval overlaps the next ones by checking if its ending interval > the next's starting interval
    - the new merged interval will have the start as the first's starting interval and the ending to be the max(the next's ending interval, the first's starting interval)

"""


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def merge(intervals):
    merged = []
    intervals.sort(key=lambda x: x.start)

    i = 0
    while i < len(intervals)-1:
        start = intervals[i].start
        end = intervals[i].end
        while i < len(intervals)-1 and end >= intervals[i+1].start:
            i += 1
            end = max(end, intervals[i].end)

        merged.append(Interval(start, end))

    return merged


"""
Merge Overlapping Intervals:

Write a function that takes in a non-empty array of arbitrary intervals,
 merges any overlapping intervals, and returns the new intervals in no particular order.
Each interval interval is an array of two integers,
 with interval[0] as the start of the interval and interval[1] as the end of the interval.
Note that back-to-back intervals aren't considered to be overlapping.
For example, [1, 5] and [6, 7] aren't overlapping; however, [1, 6] and [6, 7] are indeed overlapping.
Also note that the start of any particular interval will always be less than or equal to the end of that interval.

Sample Input
    intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
Sample Output
    [[1, 2], [3, 8], [9, 10]]
    // Merge the intervals [3, 5], [4, 7], and [6, 8].
    // The intervals could be ordered differently.

https://www.algoexpert.io/questions/Merge%20Overlapping%20Intervals
https://leetcode.com/problems/merge-intervals
"""


def merge0(first_interval_idx, intervals):
    first_interval = intervals[first_interval_idx]
    next_interval = intervals[first_interval_idx+1]

    merged = [
        first_interval[0],
        max(first_interval[1], next_interval[1])
    ]

    intervals[first_interval_idx: first_interval_idx+2] = [merged]


# O(n^2) time | O(1) space
def mergeOverlappingIntervals00(intervals):
    intervals.sort()

    i = 0
    while i < len(intervals) - 1:  # n

        curr_interval = intervals[i]
        next_interval = intervals[i+1]

        if curr_interval[1] >= next_interval[0]:
            merge0(i, intervals)
        else:
            i += 1
    return intervals


# O(nlog(n)) time | O(n) space - where n is the length of the input array
def mergeOverlappingIntervals(intervals):
    intervals.sort()  # sortedIntervals = sorted(intervals, key=lambda x: x[0])

    res = []
    idx = 0
    while idx < len(intervals):
        left = intervals[idx][0]
        right = intervals[idx][1]

        # current interval([left, right]) can be expanded to the next
        while idx+1 < len(intervals) and right >= intervals[idx+1][0]:
            right = max(right, intervals[idx+1][1])
            idx += 1

        res.append([left, right])
        idx += 1

    return res
