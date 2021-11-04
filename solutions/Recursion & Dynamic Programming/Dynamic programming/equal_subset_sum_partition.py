""" 
Equal Subset Sum Partition:

Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both the subsets is equal.

Example 1
    Input: {1, 2, 3, 4}
    Output: True
    Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}
Example 2
    Input: {1, 1, 3, 4, 7}
    Output: True
    Explanation: The given set can be partitioned into two subsets with equal sum: {1, 3, 4} & {1, 7}
Example 3
    Input: {2, 3, 4, 6}
    Output: False
    Explanation: The given set cannot be partitioned into two subsets with equal sum.

https://leetcode.com/problems/partition-equal-subset-sum
https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/3jEPRo5PDvx
https://afteracademy.com/blog/partition-equal-subset-sum
"""

""" 
We know that if we can partition it into equal subsets that each set’s sum will have to be sum/2. 
If the sum is an odd number we cannot possibly have two equal sets.
This changes the problem into finding if a subset of the input array has a sum of sum/2.
We know that if we find a subset that equals sum/2, 
    the rest of the numbers must equal sum/2 so we’re good since they will both be equal to sum/2. 
We can solve this using dynamic programming similar to the knapsack problem.

We basically need to find two groups of numbers that will each be equal to sum(input_array) / 2
Finding one such group (with its sum = sum(input_array)/2) will imply that there will be another with a similar sum
"""


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
""" 
Brute Force 1:
While using recursion, `iterate` through the input array,
choosing whether to include each number in one of two arrays: "one" & "two"
stop once the sum of elements in each of the arrays are equal to sum(input_array) / 2
"""


def can_partition_helper_bf1(num, total, res, idx, one, two):
    # base cases
    if sum(one) == total/2 and sum(two) == total/2:
        res.append([one, two])
        return

    if sum(one) > total/2 or sum(two) > total/2:
        return

    if idx >= len(num):
        return

    can_partition_helper_bf1(num, total, res, idx+1,
                             one+[num[idx]], two)  # one
    can_partition_helper_bf1(num, total, res, idx+1,
                             one, two+[num[idx]])  # two


def can_partition_bf1(num):
    res = []
    total = sum(num)
    can_partition_helper_bf1(num, total, res, 0, [], [])
    return len(res) > 0


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
""" 
Brute Force 2:
While using recursion, `iterate` through the input array,
choosing whether to include each number in one of two sums: "one" & "two"
stop once each of the sums are equal to sum(input_array) / 2

Basically Brute Force 1 without remembering the numbers
"""


def can_partition_helper_bf2(num, total,  idx, one, two):
    # base cases
    if one == total/2 and two == total/2:
        return True

    if one > total/2 or two > total/2:
        return False
    if idx >= len(num):
        return False

    in_one = can_partition_helper_bf2(num, total,  idx+1, one+num[idx], two)
    in_two = can_partition_helper_bf2(num, total,  idx+1, one, two+num[idx])

    return in_one or in_two


def can_partition_bf2(num):
    total = sum(num)
    return can_partition_helper_bf2(num, total,  0, 0, 0)


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
""" 
Brute Force 3:

We basically need to find one group of numbers that will be equal to sum(input_array) / 2
Finding one such group (with its sum = sum(input_array)/2) will imply that there will be another with a similar sum

While using recursion, `iterate` through the input array,
choosing whether to include each number in the sum
stop once the sum is equal to sum(input_array) / 2

Basically Brute Force 2 but dealing with one sum
"""


def can_partition_helper_bf3_0(num, total,  idx, one):
    # base cases
    if one == total/2:
        return True

    if one > total/2:
        return False
    if idx >= len(num):
        return False

    included = can_partition_helper_bf3_0(num, total,  idx+1, one+num[idx])
    excluded = can_partition_helper_bf3_0(num, total,  idx+1, one)

    return included or excluded


# O(2^n) time | O(n) space
def can_partition_bf3_0(num):
    total = sum(num)
    return can_partition_helper_bf3_0(num, total,  0, 0)


# -----------------------------------


def can_partition_helper_bf3(num, total, idx):
    # base cases
    if total == 0:
        return True

    if total < 0:
        return False
    if idx >= len(num):
        return False

    included = can_partition_helper_bf3(num, total-num[idx], idx+1)
    excluded = can_partition_helper_bf3(num, total, idx+1)

    return included or excluded


# O(2^n) time | O(n) space
def can_partition_bf3(num):
    total = sum(num)
    return can_partition_helper_bf3(num, total/2,  0)


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------


"""
Top-down Dynamic Programming with Memoization:

We can use memoization to overcome the overlapping sub-problems. 
Since we need to store the results for every subset and for every possible sum,
 therefore we will be using a two-dimensional array to store the results of the solved sub-problems.
The first dimension of the array will represent different subsets and the second dimension will represent different ‘sums’ that we can calculate from each subset.
These two dimensions of the array can also be inferred from the two changing values (total and idx) in our recursive function.

The above algorithm has time and space complexity of O(N*S), where ‘N’ represents total numbers and ‘S’ is the total sum of all the numbers.
"""


def can_partition_helper_memo(num, cache, total, idx):
    if total == 0:
        return True
    if total < 0 or idx >= len(num):
        return False

    if cache[idx][total] == True or cache[idx][total] == False:
        return cache[idx][total]

    included = can_partition_helper_memo(num, cache, total-num[idx], idx+1)
    excluded = can_partition_helper_memo(num, cache, total, idx+1)

    cache[idx][total] = included or excluded
    return cache[idx][total]


# O(n*(s/2)) time & space -> where n represents total numbers & s is the total sum of all the numbers.
def can_partition_memo(num):
    half_total = int(sum(num)/2)  # convert to int for use in range
    if half_total != sum(num)/2:  # ensure it wasn't a decimal number
        # if sum(num)/2 is an odd number, we can't have two subsets with equal sum
        return False

    cache = [[-1 for _ in range(half_total+1)]
             for _ in range(len(num))]  # type: ignore

    return can_partition_helper_memo(num, cache, half_total,  0)


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------


"""
Bottom-up Dynamic Programming:

dp[n][total] means whether the specific sum 'total' can be gotten from the first 'n' numbers. 
If we can find such numbers from 0-'n' whose sum is total, dp[n][total] is true, otherwise it is false.

dp[0][0] is true since with 0 elements a subset-sum of 0 is possible (both empty sets).


dp[n][total] is true if dp[n-1][total] is true (meaning that we skipped this element, and took the sum of the previous result) 
 or dp[n-1][total- element’s value(num[n])] assuming this isn’t out of range (meaning that we added this value to our subset-sum so we look at the sum — the current element’s value).
This means, dp[n][total] will be ‘true’ if we can make sum ‘total’ from the first ‘n’ numbers.



For each n and sum, we have two options:
1. Exclude the n. In this case, we will see if we can get total from the subset excluding this n: dp[n-1][total]
2. Include the n if its value is not more than ‘total’. In this case, we will see if we can find a subset to get the remaining sum: dp[n-1][total-num[n]]

"""


def can_partition_bu(num):
    half_total = int(sum(num)/2)  # convert to int for use in range
    if half_total != sum(num)/2:  # ensure it wasn't a decimal number
        # if its a an odd number, we can't have two subsets with equal sum
        return False

    dp = [[False for _ in range(half_total+1)]
          for _ in range(len(num))]  # type: ignore

    for n in range(len(num)):
        for total in range(half_total+1):
            if total == 0:  # '0' sum can always be found through an empty set
                dp[n][total] = True
                continue

            included = False
            excluded = False

            # # exclude
            if n-1 >= 0:
                excluded = dp[n-1][total]

            # # include
            if n <= total:
                rem_total = total - num[n]
                included = rem_total == 0  # fills the whole total
                if n-1 >= 0:
                    # prev n can fill the remaining total
                    included = included or dp[n-1][rem_total]

            dp[n][total] = included or excluded

    return dp[-1][-1]
