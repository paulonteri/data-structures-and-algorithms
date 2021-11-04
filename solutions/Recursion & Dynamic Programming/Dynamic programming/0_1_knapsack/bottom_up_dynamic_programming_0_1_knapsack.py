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
Bottom-up Dynamic Programming:

Let’s try to populate our dp[][] array from the above solution, working in a bottom-up fashion. 
Essentially, we want to find the maximum profit for every sub-array and for every possible capacity. 
This means, dp[i][c] will represent the maximum knapsack profit for capacity c calculated from the first i items.

So, for each item at index ‘i’ (0 <= i < items.length) and capacity ‘c’ (0 <= c <= capacity), we have two options:

    1. Exclude the item at index ‘i’. 
        In this case, we will take whatever profit we get from the sub-array excluding this item => dp[i-1][c]

    2. Include the item at index ‘i’ if its weight is not more than the capacity. 
        In this case, we include its profit plus whatever profit we get from the remaining capacity 
        and from remaining items => profits[i] + dp[i-1][c-weights[i]]

Finally, our optimal solution will be maximum of the above two values:

    dp[i][c] = max(dp[i-1][c], profits[i] + dp[i-1][c-weights[i]])
    dp[i][c] = max(exclude curr,  include curr + fill the remaining capacity)

"""

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def solve_knapsack(profits, weights, capacity):

    table = [[0 for _ in range(capacity+1)] for _ in range(len(profits))]

    for item in range(len(profits)):
        for cap in range(capacity + 1):
            excluded = 0
            included = 0
            prev_items = item - 1

            # # exclude item -> take prev largest
            if prev_items >= 0:
                excluded = table[prev_items][cap]

            # # include item
            if weights[item] <= cap:
                included = profits[item]

                # fill remaining capacity -> add prev items that can fit in the remaining capacity
                rem_cap = cap - weights[item]
                if rem_cap >= 0 and prev_items >= 0:
                    included += table[prev_items][rem_cap]

            # # record max
            table[item][cap] = max(included, excluded)

    return table[-1][-1]


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()
