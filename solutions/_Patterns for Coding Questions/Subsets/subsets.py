"""
Subsets/Powerset:

Write a function that takes in an array of unique integers and returns its powerset.
The powerset P(X) of a set X is the set of all subsets of X. 
For example, the powerset of [1,2] is [[], [1], [2], [1,2]].
Note that the sets in the powerset do not need to be in any particular order.
https://www.algoexpert.io/questions/Powerset
# https://leetcode.com/problems/subsets/
"""
# https://leetcode.com/problems/permutations/discuss/18239/a-general-approach-to-backtracking-questions-in-java-subsets-permutations-combination-sum-palindrome-partioning


# O(n*2^n) time | O(n*2^n) space
# 2^n because we are doubling the subsests in every iteration
# n for the len(array)
def powerset(array):
    subsets = [[]]
    for num in array:
        for idx in range(len(subsets)):
            subsets.append(subsets[idx] + [num])
    return subsets


# O(n*2^n) time | O(n*2^n) space
def powerset0(array, idx=None):
    if len(array) == 0:
        return [[]]

    if idx is None:  # first time function runs
        idx = len(array)-1
    elif idx < 0:  # base case -> create first subset then recurse up
        return [[]]

    sets = powerset(array, idx-1)

    for i in range(len(sets)):
        sets.append(sets[i] + [array[idx]])

    return sets


# -> we have 2^n subsets
# O(n*2^n) time | O(n*2^n) space
def powerset9(array):
    powersets = [[]]
    for num in array:
        # create powersets for num by ->
        # adding num to all existing powersets
        for idx in range(len(powersets)):
            powersets.append(powersets[idx] + [num])

    return powersets


"""
array = [1]
powersets = [[], [1]]

array = [1,2]
powersets = [[], [1], [2], [1,2]]

array = [1,2, 3]
powersets = [[], [1], [2], [1,2], [3], [2,3], [1,2,3]]
"""


def powerset10(array):
    return powersetHelper10(array, len(array) - 1)


def powersetHelper10(array, idx):

    # deal with first subset and empty array
    if idx < 0:
        return [[]]

    subsets = powersetHelper10(array, idx-1)

    num = array[idx]
    for i in range(len(subsets)):
        subsets.append(subsets[i] + [num])

    return subsets
