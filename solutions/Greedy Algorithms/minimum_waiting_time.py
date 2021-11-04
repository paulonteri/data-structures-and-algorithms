"""
Minimum Waiting Time:

You're given a non-empty array of positive integers representing the amounts of time that specific queries take to execute. 
Only one query can be executed at a time, but the queries can be executed in any order.
A query's waiting time is defined as the amount of time that it must wait before its execution starts.
In other words, if a query is executed second, then its waiting time is the duration of the first query; 
    if a query is executed third, then its waiting time is the sum of the durations of the first two queries.
Write a function that returns the minimum amount of total waiting time for all of the queries. 
For example, if you're given the queries of durations [1, 4, 5], 
    then the total waiting time if the queries were executed in the order of [5, 1, 4] would be (0) + (5) + (5 + 1) = 11. 
The first query of duration 5 would be executed immediately, so its waiting time would be 0, 
    the second query of duration 1 would have to wait 5 seconds (the duration of the first query) to be executed, 
    and the last query would have to wait the duration of the first two queries before being executed.

Note: you're allowed to mutate the input array.
https://www.algoexpert.io/questions/Minimum%20Waiting%20Time
"""


""" 
ensure the longest waiting times are at the end
"""


def minimumWaitingTime(queries):
    queries.sort()
    total = 0

    prev_time = 0
    for time in queries:
        total += prev_time
        prev_time += time

    return total


def minimumWaitingTime2(queries):
    queries.sort()
    total = 0
    for idx, num in enumerate(queries):
        last_idx = len(queries)-1
        # add waiting time for the elements to the right of the current element
        total += num * (last_idx - idx)

    return total
