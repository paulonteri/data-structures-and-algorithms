"""
0/1 Knapsack:

Given two integer arrays to represent weights and profits of ‘N’ items,
    we need to find a subset of these items which will give us maximum profit
    such that their cumulative weight is not more than a given number ‘C’.
Write a function that returns the maximum profit.
Each item can only be selected once, which means either we put an item in the knapsack or skip it.

https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/RM1BDv71V60
"""


"""
Top-down Dynamic Programming with Memoization:

We can use memoization to overcome the overlapping sub-problems from the brute force solution.
Since we have two changing values (`capacity` and `idx`) in our recursive function `knapsack_recursive()`,
 we can use a two-dimensional array to store the results of all the solved sub-problems.
As mentioned above, we need to store results for every sub-array (i.e., for every possible index ‘i’)
and for every possible capacity ‘c’.


Time and Space complexity 
Since our memoization array cache[profits.length/weights.length][capacity+1] stores the results for all subproblems,
 we can conclude that we will not have more than N*C subproblems 
(where ‘N’ is the number of items and ‘C’ is the knapsack capacity). 
This means that our time complexity will be O(N*C)O(N∗C).
The above algorithm will use O(N*C)O(N∗C) space for the memoization array.
 Other than that, we will use O(N)O(N) space for the recursion call-stack. 
    So the total space complexity will be O(N∗C+N), which is asymptotically equivalent to O(N*C).O(N∗C).


"""

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def knapsack_recursive(profits, weights, cache, capacity, idx, curr_profit):
    if capacity < 0:
        return -1
    if idx == len(weights):
        return curr_profit

    # if we have already solved a similar problem, return the result from memory/cache
    if cache[idx][capacity]:
        return cache[idx][capacity]

    if_chosen = knapsack_recursive(
        profits, weights, cache,
        capacity - weights[idx],
        idx + 1,
        curr_profit + profits[idx]
    )
    if_excluded = knapsack_recursive(
        profits, weights, cache, capacity, idx + 1, curr_profit)

    # store result in cache
    cache[idx][capacity] = max(if_chosen, if_excluded)
    return cache[idx][capacity]


def solve_knapsack(profits, weights, capacity):
    cache = [[False] * (capacity+1)] * len(weights)
    return knapsack_recursive(profits, weights, cache, capacity, 0, 0)
