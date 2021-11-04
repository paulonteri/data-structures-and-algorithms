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
Brute force:
A basic brute-force solution could be to try all combinations of the given items (as we did above),
    allowing us to choose the one with maximum profit and a weight that doesn’t exceed ‘C.’ 

The algorithm’s time complexity is exponential O(2^n)
The space complexity is O(n). This space will be used to store the recursion stack. 
Since our recursive algorithm works in a depth-first fashion, 
    which means, we can’t have more than ‘n’ recursive calls on the call stack at any time.
"""

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def solve_knapsack_helper_00(profits, weights, capacity, total_profits):
    if len(profits) == 0 or capacity < 0:
        return -1

    highest = -1
    for idx, weight in enumerate(weights):
        rem_profits = profits[:idx] + profits[idx+1:]
        rem_weights = weights[:idx] + weights[idx+1:]
        highest = max(
            highest,
            solve_knapsack_helper_00(rem_profits, rem_weights,
                                     capacity-weight, total_profits+profits[idx])
        )

    return max(total_profits, highest)


def solve_knapsack_00(profits, weights, capacity):
    return solve_knapsack_helper_00(profits, weights, capacity, 0)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# iterate through all the elements,
#   see which will give max - choosing or excluding the element
def knapsack_recursive_01(profits, weights, capacity, idx, curr_profit):
    if capacity < 0:  # we made an invalid choice & went beyond the capacity
        return -1
    if idx == len(weights):  # no more to choose
        return curr_profit

    if_chosen = knapsack_recursive_01(
        profits, weights,
        capacity - weights[idx],
        idx + 1,
        curr_profit + profits[idx]
    )
    if_excluded = knapsack_recursive_01(
        profits, weights, capacity, idx + 1, curr_profit)

    return max(curr_profit, if_chosen, if_excluded)


def solve_knapsack_01(profits, weights, capacity):
    return knapsack_recursive_01(profits, weights, capacity, 0, 0)

# ----------------------------


def knapsack_recursive_01_2(profits, weights, capacity, currentIndex):
    if capacity <= 0 or currentIndex >= len(profits):
        return 0

    if_chosen = 0
    if weights[currentIndex] <= capacity:
        if_chosen = profits[currentIndex] + knapsack_recursive_01_2(
            profits, weights, capacity - weights[currentIndex], currentIndex + 1)

    if_excluded = knapsack_recursive_01_2(
        profits, weights, capacity, currentIndex + 1)

    return max(if_chosen, if_excluded)


def solve_knapsack_01_2(profits, weights, capacity):
    return knapsack_recursive_01_2(profits, weights, capacity, 0)


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    print(solve_knapsack_00([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack_01([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack_01_2([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack_01_2([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack_01([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack_00([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()
