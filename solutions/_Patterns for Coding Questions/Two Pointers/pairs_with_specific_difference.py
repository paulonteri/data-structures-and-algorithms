""" 
Pairs with Specific Difference:

Given an array arr of distinct integers and a nonnegative integer k, 
write a function findPairsWithGivenDifference that returns an array of all pairs [x,y] in arr, 
such that x - y = k. If no such pairs exist, return an empty array.

Note: the order of the pairs in the output array should maintain the order of the y element in the original array.

Examples:
    [4,1], 3
    [[4,1]]

    [0,-1,-2,2,1], 1
    [[1, 0], [0, -1], [-1, -2], [2, 1]]

    [1,5,11,7], 4
    [[5,1], [11,7]]

    [1,5,11,7], 6
    [[7,1],[11,5]]

https://www.pramp.com/challenge/XdMZJgZoAnFXqwjJwnpZ

Similar: https://leetcode.com/problems/k-diff-pairs-in-an-array/
"""


""" 

curr - next = k
curr = k + next
"""


def find_pairs_with_given_difference(arr, k):
    res = []
    store = set(arr)

    for num in arr:
        if num+k in store:
            res.append([num+k, num])

    return res


""" 
Works but doesn't obey ordering

curr - next = k
next = curr - k

def find_pairs_with_given_difference(arr, k):
    res = []
    store = set(arr)

    for num in arr:
        if num-k in store:
            res.append([num, num-k])

    return res

"""


print(find_pairs_with_given_difference(
    [0, -1, -2, 2, 1], 1), "required: ", [[1, 0], [0, -1], [-1, -2], [2, 1]])
print(find_pairs_with_given_difference(
    [1, 5, 11, 7], 4), "required: ", [[5, 1], [11, 7]])
print(find_pairs_with_given_difference(
    [1, 5, 11, 7], 6), "required: ",  [[7, 1], [11, 5]])
