"""
Meeting Rooms II

Given an array of meeting time intervals consisting of start and end times:
[[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Input:
    [[0,30],[5,10],[15,20]]
    [[0,30]]
    [[0,30],[5,10],[1,20],[7,30],[50,10],[15,20],[0,30],[5,10],[15,20]]
Output:
    2
    1
    6

https://leetcode.com/problems/meeting-rooms-ii/
"""
from typing import List
import heapq
"""
Laptop Rentals:

You're given a list of time intervals during which students at a school need a laptop.
These time intervals are represented by pairs of integers [start, end], where 0 <= start < end.
However, start and end don't represent real times; therefore, they may be greater than 24.
No two students can use a laptop at the same time, but immediately after a student is done using a laptop,
    another student can use that same laptop. For example, if one student rents a laptop during the time interval [0, 2],
    another student can rent the same laptop during any time interval starting with 2.
Write a function that returns the minimum number of laptops that the school needs to rent
 such that all students will always have access to a laptop when they need one.

Sample Input
    times =
    [
    [0, 2],
    [1, 4],
    [4, 6],
    [0, 4],
    [7, 8],
    [9, 11],
    [3, 10],
    ]
Sample Output
    3

https://www.algoexpert.io/questions/Laptop%20Rentals
"""


# this can be optimized futher plus variables have been overused:
# this is to help in undertanding the solution
# time O(n log(n)) | space O(n)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]):

        if not intervals:
            return 0

        # sort meetings by starting time
        intervals.sort(key=lambda x: x[0])

        # # Logic:
        # if the next meeting is earlier than the earliest ending time, then no room will be free for it.
        # Otherwise, update the ending time (for the room)

        # # (ending_times heap) used to store the ending times of all meeting rooms
        # if a second meeting is held in a room, we replace the 1st's ending time,
        # we delete the 1st meeting ending time and add the 2nd's

        # create ending times heap
        # the heap will help us in keep the earliest ending time per room 'on top, [0]'
        ending_times = [intervals[0][1]]

        i = 1
        while i < len(intervals):
            # in any case, we will add the meeting's ending time to the ending_times,
            # however, if the earliest ending time is less than it's starting, it means those two can share a room
            # so we remove the earlier one's ending time

            # # check if (curr starting time) overlaps earliest ending time
            curr_meeting = intervals[i]
            # cannot share room
            if curr_meeting[0] < ending_times[0]:
                # similar to adding another meeting room
                heapq.heappush(ending_times, curr_meeting[1])
            # can share room
            # meeting starts later than the earliest ending
            # free room -> not overlap
            else:
                # remove the first room's ending time from the count
                # similar to updating meeting room's earliest ending
                heapq.heappop(ending_times)
                heapq.heappush(ending_times, curr_meeting[1])

            i += 1

        # we always added rooms to the heap and:
        # whenever we found conflicts in times we didn't remove from the heap but,
        # we removed when we were reusing the same room
        # the meeting ending times that were not replaced
        return len(ending_times)


"""
-----------------------------------------------------------------------------------------------------------------------------------------------
[[0, 2], [0, 4], [1, 4], [3, 10], [4, 6], [7, 8], [9, 11]]

[9,7,10]

[[0, 10], [0, 20], [1, 9], [2, 8], [3, 7], [4, 6], [5, 6], [10, 15], [11, 12]]

[15, 20, 12, 8, 7, 6, 6]
"""


# time O(n^2) time | space O(n)
def laptopRentalsBF(times):
    times.sort()

    # will record when the currently borrowed laptop will be free (end time)
    needed = []
    for time in times:

        added = False
        # check if we can find a laptop that we will use once it is free
        for idx in range(len(needed)):
            if needed[idx] <= time[0]:
                # use laptop when it gets free
                needed[idx] = time[1]
                added = True
                break

        if not added:
            # no free laptop -> we need another one
            needed.append(time[1])

    return len(needed)


"""
-----------------------------------------------------------------------------------------------------------------------------------------------
use a min-heap to get the earliest time a laptop will be free
sort the input array to ensure the ones with the earliest times come first
"""


def laptopRentals(times):
    times.sort()

    # will record when the currently borrowed laptop will be free (end time)
    needed = []
    for time in times:

        # # check if we can find a laptop that we will use once it is free
        if needed and needed[0] <= time[0]:
            # replace the earliest free laptop
            heapq.heappop(needed)
            heapq.heappush(needed, time[1])
        else:
            # no free laptop -> we need another one
            heapq.heappush(needed, time[1])

    return len(needed)
