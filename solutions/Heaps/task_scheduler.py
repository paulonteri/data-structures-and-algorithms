"""
621. Task Scheduler

Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task.
Tasks could be done in any order. Each task is done in one unit of time. 
For each unit of time, the CPU could complete either one task or just be idle.
However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), 
    that is that there must be at least n units of time between any two same tasks.
Return the least number of units of times that the CPU will take to finish all the given tasks.

Example 1:
    Input: tasks = ["A","A","A","B","B","B"], n = 2
    Output: 8
    Explanation: 
        A -> B -> idle -> A -> B -> idle -> A -> B
        There is at least 2 units of time between any two same tasks.
Example 2:
    Input: tasks = ["A","A","A","B","B","B"], n = 0
    Output: 6
        Explanation: On this case any permutation of size 6 would work since n = 0.
        ["A","A","A","B","B","B"]
        ["A","B","A","B","A","B"]
        ["B","B","B","A","A","A"]
        ...
        And so on.
Example 3:
    Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
    Output: 16
    Explanation: 
        One possible solution is
        A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A

Constraints:
    1 <= task.length <= 104
    tasks[i] is upper-case English letter.
    The integer n is in the range [0, 100].


https://leetcode.com/problems/task-scheduler
"""

from typing import List
from collections import Counter
from heapq import heapify, heappop, heappush

""" 
tasks = ["A","A","A","B","B","B"], n = 2

A B A B ,n=2 -> A,B,ID,A,B 
A A B A ,n=2 -> A,B,ID,A,ID,A 
A A B B ,n=2 -> A,B,ID,A,B 

["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Counter({'A': 6, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1})
[A, , ,A, , ,A, , ,A, , ,A, , ,A]
[A,B, ,A, , ,A, , ,A, , ,A, , ,A]
[A,B,C,A, , ,A, , ,A, , ,A, , ,A]
[A,B,C,A,D, ,A, , ,A, , ,A, , ,A]
[A,B,C,A,D,E,A,F,G,A, , ,A, , ,A] ... quickly fill
[A,B,C, A,D,E, A,F,G, A,idle,idle, A,idle,idle, A] => length 16

"""


class Solution:
    def leastInterval(self, tasks: List[str], n: int):
        """ 
        Steps:
        - `time_taken` = 0
        - Have a `max_heap` that contains the counts of each task
        - Have a while loop:
            - takes at most n+1 tasks from the `max_heap`
            - processes them (reduce count by one)
            - records how many tasks it has processed ( add them to `time_taken`)
                - if not at the end of the task queue / max_heap is not empty:
                    - the minimum time taken is n+1 `{tasks processed + waiting time(if any)} == n+1`
                - else: time taken is the number of tasks done

        Video tutorials:
        - https://youtu.be/Z2Plc8o1ld4
        - https://youtu.be/ySTQCRya6B0

        """
        if n == 0:
            return len(tasks)

        time_taken = 0

        # create max_heap (negate values added to simulate max_heap)
        max_heap = [-count for count in Counter(tasks).values()]
        heapify(max_heap)
        while max_heap:
            curr_processing = []

            # # get tasks to be processed
            for _ in range(n+1):
                if not max_heap:
                    continue
                curr_processing.append(-heappop(max_heap))

            # # process tasks and return to heap if not yet done with task
            for task_count in curr_processing:
                if task_count-1 > 0:
                    heappush(max_heap, -(task_count-1))

            # # record how many tasks we processed
            if not max_heap:
                # if we reached the end, (no more tasks)
                # we might have processed less than n+1 items as there is no waiting time after each
                time_taken += len(curr_processing)
            else:
                # if not at the end,
                # always, (tasks processed + waiting time(if any)) == n+1
                time_taken += n+1

        return time_taken
