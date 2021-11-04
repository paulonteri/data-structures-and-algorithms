""" 
0/1 Knapsack:

Given two integer arrays to represent weights and profits of ‘N’ items, 
    we need to find a subset of these items which will give us maximum profit 
    such that their cumulative weight is not more than a given number ‘C’. 
Write a function that returns the maximum profit.
Each item can only be selected once, which means either we put an item in the knapsack or skip it.

https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/RM1BDv71V60
"""

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
""" 
Brute force:
A basic brute-force solution could be to try all combinations of the given items (as we did above),
    allowing us to choose the one with maximum profit and a weight that doesn’t exceed ‘C.’ 

"""


def solve_knapsack_helper_bf(profits, weights, capacity, total_profits):
    output = -1
    if len(profits) == 0 or capacity < 0:
        return output
    if capacity == 0:
        return total_profits

    for idx, weight in enumerate(weights):
        rem_profits = profits[:idx] + profits[idx+1:]
        rem_weights = weights[:idx] + weights[idx+1:]
        output = max(
            output,
            solve_knapsack_helper_bf(rem_profits, rem_weights,
                                     capacity-weight, total_profits+profits[idx])
        )

    return output


def solve_knapsack_bf(profits, weights, capacity):
    return solve_knapsack_helper_bf(profits, weights, capacity, 0)


def main():
    print(solve_knapsack_bf([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack_bf([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


"""
Knapsack Problem:

You're given an array of arrays where each subarray holds two integer values and represents an item;
 the first integer is the item's value, and the second integer is the item's weight.
You're also given an integer representing the maximum capacity of a knapsack that you have.
Your goal is to fit items in your knapsack without having the sum of their weights exceed the knapsack's capacity,
 all the while maximizing their combined value. Note that you only have one of each item at your disposal.
Write a function that returns the maximized combined value of the items that you should pick as well as an array of the indices of each item picked.
If there are multiple combinations of items that maximize the total value in the knapsack, your function can return any of them.
https://www.algoexpert.io/questions/Knapsack%20Problem
"""


# O(2^n) time | O(n) space
def knapsackProblem(items, capacity, idx=0, added=[]):
    if idx >= len(items):
        return [0, added]

    curr_weight = items[idx][1]
    curr_value = items[idx][0]

    if curr_weight > capacity:
        result = knapsackProblem(items, capacity, idx+1, added)  # skip current
    else:
        # add current to knapsack
        not_skip = knapsackProblem(
            items, capacity-curr_weight, idx+1, added + [idx])
        not_skip[0] = curr_value + not_skip[0]

        skip = knapsackProblem(items, capacity, idx+1, added)  # skip current

        if skip[0] > not_skip[0]:
            result = skip
        else:
            result = not_skip

    return result
