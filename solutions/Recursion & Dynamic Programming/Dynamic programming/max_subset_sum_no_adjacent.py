"""
Max Subset Sum No Adjacent:

Write a function that takes in an array of positive integers and 
 returns the maximum sum of non-adjacent elements in the array.
If the input array is empty, the function should return 0.

https://www.algoexpert.io/questions/Max%20Subset%20Sum%20No%20Adjacent
"""


def maxSubsetSumNoAdjacentBf(array):
    return bfHelper(array, float('inf'), 0, 0)


def bfHelper(array, last_added, curr_sum, idx):
    if idx >= len(array):
        return curr_sum

    not_chosen = bfHelper(array, last_added, curr_sum, idx+1)  # ignore idx
    chosen = -1
    if last_added != idx-1:  # choose idx
        chosen = bfHelper(array, idx, curr_sum + array[idx], idx+1)

    return max(
        not_chosen,
        chosen
    )

# ------------------------------------------------------------------------------------------------------------------------


""" 
          array: [7, 10, 12,          7,    9,    14]
max_sum_at_pos:  [7, 10, 19,         19,   28,    33]
                 [7, 10, 12+7,  10+7/19, 19+9, 19+14]

         array: [30, 25, 50, 55, 100, 120]
max_sum_at_pos: [30, 30, 80, 80, 180, 200]

max_sums[i] = max( 
                    (max_sums[i-1]),            -> i cannot be included
                    (max_sums[i-2] + array[i])  -> i can be included
                )
"""


# 0(n) time | 0(n) space
def maxSubsetSumNoAdjacent(array):

    if len(array) == 0:
        return 0

    # for each index in the input array,
    #  find the maximum possible sum and store it in the max_sums array
    # max_sums[i] = max( (max_sums[i-1]), (max_sums[i-2] + array[i]) )
    max_sums = [array[0]]
    for idx in range(1, len(array)):

        if idx == 1:
            max_sums.append(max(array[0], array[1]))
            continue

        prev_maxsum = max_sums[idx-1]
        curr_plus_before_prev_maxsum = array[idx] + max_sums[idx-2]

        # maximum sum at index
        max_sums.append(max(
            curr_plus_before_prev_maxsum,
            prev_maxsum)
        )

    return max_sums[-1]


# ------------------------------------------------------------------------------------------------------------------------

# 0(n) time | 0(1) space
def maxSubsetSumNoAdjacent1(array):

    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]

    prev_max = array[0]
    curr_max = max(array[0], array[1])  # at index 1
    # for each index in the input array,
    #  find the maximum possible sum and store it in the max_sums array
    # max sum for array[i] = max( (curr_max), (array[idx] + prev_max) )
    for idx in range(2, len(array)):

        curr_plus_prevmax = array[idx] + prev_max

        prev_max = curr_max
        curr_max = max(curr_plus_prevmax, curr_max)

    return curr_max
