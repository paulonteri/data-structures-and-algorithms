"""
Task Assignment:

You're given an integer k representing a number of workers and an array of positive integers representing durations of tasks that must be completed by the workers.
Specifically, each worker must complete two unique tasks and can only work on one task at a time.
The number of tasks will always be equal to 2k such that each worker always has exactly two tasks to complete.
All tasks are independent of one another and can be completed in any order. Workers will complete their assigned tasks in parallel, and the time taken to complete all tasks will be equal to the time taken to complete the longest pair of tasks.

Write a function that returns the optimal assignment of tasks to each worker such that the tasks are completed as fast as possible.
Your function should return a list of pairs, where each pair stores the indices of the tasks that should be completed by one worker. 
The pairs should be in the following format: [task1, task2], where the order of task1 and task2 doesn't matter.
Your function can return the pairs in any order. If multiple optimal assignments exist, any correct answer will be accepted.
Note: you'll always be given at least one worker (i.e., k will always be greater than 0).

https://www.algoexpert.io/questions/Task%20Assignment
"""


def taskAssignment(k, tasks):
    output = []

    # add indices to tasks
    for idx in range(len(tasks)):
        tasks[idx] = [tasks[idx], idx]
    # sort by task duration
    tasks.sort(key=lambda x: x[0])

    # add first half to output
    for idx in range(k):
        output.append([tasks[idx][1]])

    # add second half: from largest task to smallest
    pos = 0
    for idx in reversed(range(k, len(tasks))):
        output[pos] = output[pos] + [tasks[idx][1]]
        pos += 1

    return output


def taskAssignment1(k, tasks):
    output = []

    # add indices to tasks
    for idx in range(len(tasks)):
        tasks[idx] = [tasks[idx], idx]
    # sort by task duration
    tasks.sort(key=lambda x: x[0])

    tasks_length = len(tasks)
    # add largest and smallest task
    for idx in range(k):
        first_task = tasks[idx][1]
        second_task = tasks[(tasks_length - 1) - idx][1]
        output.append([first_task, second_task])

    return output
