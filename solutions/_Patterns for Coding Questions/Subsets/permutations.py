"""
Permutations

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

https://leetcode.com/problems/permutations/
https://www.algoexpert.io/questions/Permutations

"""
# https://leetcode.com/problems/permutations/discuss/18239/a-general-approach-to-backtracking-questions-in-java-subsets-permutations-combination-sum-palindrome-partioning


"""
########################################################################################################################################################################################################################
"""

"""
[
[1,2,3],
[1,3,2],
[2,1,3],
[2,3,1],
[3,1,2],
[3,2,1]
]

                     []
          /               |    \
        [1]              [2]
        / \              / \
    [1,2]  [1,3]     [2,1] [2,3]
      |        |       |      |
[1,2,3]     [1,3,2]  [2,1,3]  [2,3,1]


                                                  ([], [], [1,2,3])

        ([], [1], [2,3])                           (
            [], [2], [1,3])              ([], [3], [1,2])

([], [1, 2], [3]) ([], [1, 3], [3])


[[1,2,3,4],[1,2,4,3],[1,3,2,4],[1,3,4,2],[1,4,2,3],[1,4,3,2],[2,1,3,4],[2,1,4,3],[2,3,1,4],[2,3,4,1],[2,4,1,3],[2,4,3,1],[3,1,2,4],[3,1,4,2],[3,2,1,4],[3,2,4,1],[3,4,1,2],[3,4,2,1],[4,1,2,3],[4,1,3,2],[4,2,1,3],[4,2,3,1],[4,3,1,2],[4,3,2,1]]


# try placing each number at the beginning if the list, then add all the others at all the possible positions

- have result = []
- have a function perm(arr, curr_subset, result)
    - for each num in arr
        - place num in a copy of curr_subset
        - remove the num in a copy of arr
        - pass both copies to perm()
    - do the above step till arr is empty
        - then add curr_subset to result
- return result
"""




from typing import List
def _getPermutationsHelper(result, array, curr_subset):
    if not array:
        return result.append(curr_subset)

    for i in range(len(array)):
        new_array = array[:i]+array[i+1:]
        new_curr_subset = curr_subset+[array[i]]
        _getPermutationsHelper(result, new_array,  new_curr_subset)


def _getPermutations(array):
    result = []
    if not array:
        return result

    _getPermutationsHelper(result, array, [])

    return result


"""

# what subsets can i create with one element in the input array? two? three?

# remove all the elements from nums then insert them back in all positions possible

# place one each number at the beginning of a different list, then insert all the rest in different orders

- have a recursive function perm(nums_array)
    - for each number in the list (iterate through the list)
        - remove it from the list
        - pass the rest of the numbers to the perm() recursive function
        - add it to all the lists returned by perm()
    - with base cases:
        returns [[]] once nums_array is empty
"""


def __getPermutations(array):
    if len(array) == 1:
        return [array[:]]

    result = []
    for _ in range(len(array)):
        # use the first index by default instead of keeping track of indices down the recursive tree
        num = array.pop(0)

        for subset in __getPermutations(array):
            subset.append(num)
            result.append(subset)

        array.append(num)

    return result


""" 
Improvement of above
"""


def ___getPermutations(array):
    if len(array) < 1:
        return array
    return ___getPermutationsHelper(array, 0)


def ___getPermutationsHelper(array, pos):
    if pos == len(array)-1:
        return [[array[pos]]]

    result = []
    for i in range(pos, len(array)):
        # add the number(array[i]) to the permutation
        # place the element of interest at the first position (pos)
        #  Example: for getPermutationsHelper([1,2,3,4], 0), while in this for loop
        #       when at value 1 (i=0), we want 1 to be at pos(0), so that we can iterate through [2,3,4] next without adding 1 again
        #       when at 2, we want 2 to be at pos(0), so that we can iterate through [1,3,4] next ([2,1,3,4])
        #       when at 3, we want it to be at pos(0), so that we can iterate through [2,1,4] next ([3,2,1,4])
        #   so we have to manually place it there (via swapping with the element at pos), then we return it just before the loop ends
        # and move pos forward

        # # num = array[i] (num of interest)
        # place the num at pos because it will be ignored down the recursive tree
        array[i], array[pos] = array[pos], array[i]

        for subset in ___getPermutationsHelper(array, pos+1):
            subset.append(array[pos])
            result.append(subset)

        # return num to its original position
        array[i], array[pos] = array[pos], array[i]

    return result


""" 


perm(1,2,3)
							[1,2,3]
				/			  |                \
		  [1,2,3]	        [2,1,3]           [3,2,1]
		  /  \              /      \              /   \
	[1,2,3] [1,3,2]    [2,1,3] [2,3,1]   [3,2,1] [3,1,2]


Try to get all possible arrangements of nums


"""


def ____getPermutations(array):
    if len(array) < 1:
        return array
    result = []
    ____getPermutationsHelper(result, array, 0)
    return result


def ____getPermutationsHelper(result, array, pos):
    if pos == len(array):
        result.append(array[:])  # found one arrangement
        return

    for i in range(pos, len(array)):
        # add the number(array[i]) to the permutation
        # place the element of interest at the first position (pos)
        #  Example: for getPermutationsHelper([1,2,3,4], 0), while in this for loop
        #       when at value 1 (i=0), we want 1 to be at pos(0), so that we can iterate through [2,3,4] next without adding 1 again
        #       when at 2, we want 2 to be at pos(0), so that we can iterate through [1,3,4] next ([2,1,3,4])
        #       when at 3, we want it to be at pos(0), so that we can iterate through [2,1,4] next ([3,2,1,4])
        #   so we have to manually place it there (via swapping with the element at pos), then we return it just before the loop ends
        # and move pos forward

        # # num = array[i] (num of interest) -> it is array[i]'s turn to be at pos
        # place the num at pos because it will be ignored down the recursive tree
        array[i], array[pos] = array[pos], array[i]

        ____getPermutationsHelper(result, array, pos+1)

        # return num to its original position
        array[i], array[pos] = array[pos], array[i]


""" 
########################################################################################################################################################################################################################
"""


class Solution:
    def getPermutations(self, nums, num):
        array_of_nums = []
        for idx in range(len(nums) + 1):
            new_arr = list(nums)
            new_arr.insert(idx, num)
            array_of_nums.append(new_arr)
        return array_of_nums

    def permute(self, nums: List[int]):
        result = []
        result.append([nums[0]])
        index = 1
        while index < len(nums):
            num = nums[index]

            new_result = []
            for arr in result:
                new_result += self.getPermutations(arr, num)

            result = new_result

            index += 1

        return result


class Solution2:

    def combiner(self, num, arrays):
        for arr in arrays:
            arr.insert(0, num)
        return arrays

    def permute(self, nums):

        if len(nums) == 0:
            return []

        elif len(nums) == 1:  # recursion base case
            return [nums]

        generated = []  # store all generated permutations

        # get premutations with the number at nums[idx] at the front of the list (index 0)
        for idx in range(len(nums)):

            # remove nums[idx] from the list
            new_nums = list(nums)
            temp = new_nums.pop(idx)

            # place nums[idx] at the front of each permutation(list), index 0
            combined = self.combiner(temp, self.permute(new_nums))

            generated += combined

        return generated


class Solution00:
    def helper(self, permutations, curr_perm, elements):
        if len(elements) < 1:
            permutations.append(curr_perm)
            return

        for idx, num in enumerate(elements):
            # for each number in elements create a new permutation (curr_perm)
            #   and pass it to the recursive function
            self.helper(permutations,
                        curr_perm + [num],
                        elements[:idx]+elements[idx+1:]
                        )

    def permute(self, nums: List[int]):
        permutations = []
        self.helper(permutations, [], nums)
        return permutations


"""
[
[1,2,3],
[1,3,2],
[2,1,3],
[2,3,1],
[3,1,2],
[3,2,1]
]

                     []
          /               |    \
        [1]              [2]
        / \              / \     
    [1,2]  [1,3]     [2,1] [2,3]
      |        |       |      |
[1,2,3]     [1,3,2]  [2,1,3]  [2,3,1]


                                                  ([], [], [1,2,3])

        ([], [1], [2,3])                           ([], [2], [1,3])              ([], [3], [1,2])

([], [1, 2], [3]) ([], [1, 3], [3])


[[1,2,3,4],[1,2,4,3],[1,3,2,4],[1,3,4,2],[1,4,2,3],[1,4,3,2],[2,1,3,4],[2,1,4,3],[2,3,1,4],[2,3,4,1],[2,4,1,3],[2,4,3,1],[3,1,2,4],[3,1,4,2],[3,2,1,4],[3,2,4,1],[3,4,1,2],[3,4,2,1],[4,1,2,3],[4,1,3,2],[4,2,1,3],[4,2,3,1],[4,3,1,2],[4,3,2,1]]

"""


class Solution01:
    def permute(self, nums: List[int]):
        if len(nums) == 1:
            return [nums[:]]  # a copy

        result = []
        for _ in range(len(nums)):
            # we always take the first element because the indexes will be mixed up from the
            #  removal and readding
            num = nums.pop(0)

            # for all of the `result`s coming form below (the recursive tree),
            #  we add num to each of their elements, and create our own `result` that was empty
            #  then return it
            perm_results = self.permute(nums)
            for perm in perm_results:
                perm.append(num)
            result += perm_results

            # readd num
            # because it will be used in creating permutations
            nums.append(num)

        return result


"""
Permutations:

Write a function that takes in an array of unique integers
 and returns an array of all permutations of those integers in no particular order.
If the input array is empty, the function should return an empty array.
https://www.algoexpert.io/questions/Permutations
"""


# Upper Bound: O(n^2*n!) time | O(n*n!) space
# Roughly: O(n*n!) time | O(n*n!) space
def getPermutations(array):
    permutations = []
    if not array:
        return []
    getPermutationsHelper(array, [], permutations)
    return permutations


def getPermutationsHelper(array, curr, permutations):

    if not array:
        permutations.append(curr)
        # return

    for idx in range(len(array)):
        # array_copy = list(array)
        # curr_copy = list(curr)
        # curr_copy.append(array_copy.pop(idx))
        # getPermutationsHelper(array_copy, curr_copy, permutations)
        # # use slicing
        getPermutationsHelper(
            array[0:idx] + array[idx+1:],  # (new array) remove idx
            curr + [array[idx]],  # (new curr) add the number at idx
            permutations
        )


"""
Solution:

[1,2,3] <- array
        1,2,3 
        1,3,2 
        ​
        2,1,3
        2,3,1

        3,1,2
        3,2,1





		                           [1,2,3,4] <- array

	[1][2,3,4]           [2][1,3,4]         [3][1,2,4]                [4][1,2,3]

 [1,2] [1,3] [1,4]   [2,1] [2,3] [2,4]    [3,1] [3,2] [3,4]        [4,1] [4,2] [4,3] 

# explanatiion video at 18:00
O(n!.n.n) time 
n! -> number of permutations we have (number of leaves in recusrsive represantation)
n -> total of n*n calls to the factorial method
n -> removal from array ans creating permutations in the helper method (2n)
"""

print(getPermutations([1, 2]))
print(getPermutations([1, 2, 3]))
print(getPermutations([1, 2, 3, 4]))


def getPermutations2(array):
    all_permutations = []
    if array is None or len(array) < 1:
        return all_permutations

    getPermutationsHelper0(array, all_permutations)
    return all_permutations


def getPermutationsHelper0(array, all_permutations, idx=0):
    if idx == len(array) - 1:
        all_permutations.append(array[:])
        return

    for j in range(idx, len(array)):
        swap(array, idx, j)
        getPermutationsHelper0(array, all_permutations, idx+1)
        swap(array, idx, j)


def swap(array, a, b):
    array[a], array[b] = array[b], array[a]


# <----------------------------------------------------------------------------------------------------------->
def getPermutationsHelper01(res, curr_perm, array):
    if len(array) == 0:
        if len(curr_perm) > 0:
            res.append(curr_perm)
        return

    for i in range(len(array)):
        # add the number(array[i]), add it to the permutation and remove it from the array
        new_array = array[:i] + array[i+1:]  # remove number form array
        new_perm = curr_perm + [array[i]]  # add number to the permutation

        getPermutationsHelper01(res, new_perm, new_array)


# -> we have n! leaves each with, n calls to the helper method, & each helper method does n work
# Upper Bound: O(n^2*n!) time | O(n*n!) space
# Roughly: O(n*n!) time | O(n*n!) space
def getPermutations01(array):
    res = []
    getPermutationsHelper01(res, [], array)
    return res


# <----------------------------------------------------------------------------------------------------------->
def swap02(array, a, b):
    array[a], array[b] = array[b], array[a]


def getPermutationsHelper02(res, curr_perm, array, pos):
    if pos >= len(array):
        if len(curr_perm) > 0:
            res.append(curr_perm)
        return

    for i in range(pos, len(array)):
        # add the number(array[i]) to the permutation
        # place the element of interest at the first position (pos)
        #  Example: for getPermutationsHelper02(res, [], [1,2,3], 0), while in this for loop
        #       when at value 1 (i=0), we want 1 to be at pos(0), so that we can iterate through [2,3,4] next without adding 1 again
        #       when at 2, we want 2 to be at pos(0), so that we can iterate through [1,3,4] next ([2,1,3,4])
        #       when at 3, we want it to be at pos(0), so that we can iterate through [2,1,4] next ([3,2,1,4])
        #   so we have to manually place it there (via swapping with the element at pos), then we return it just before the loop ends
        # and move pos forward

        new_perm = curr_perm + [array[i]]  # add number to the permutation

        # place the element of interest at the first position (pos)
        swap02(array, pos, i)
        getPermutationsHelper02(res, new_perm, array, pos+1)
        # return the element of interest to its original position
        swap02(array, i, pos)


# -> we have n! leaves each with, n calls to the helper method, & each helper method does n work
# Upper Bound: O(n^2*n!) time | O(n*n!) space
# Roughly: O(n*n!) time | O(n*n!) space
def getPermutations02(array):
    res = []
    getPermutationsHelper02(res, [], array, 0)
    return res


# <----------------------------------------------------------------------------------------------------------->
def swap03(array, a, b):
    array[a], array[b] = array[b], array[a]


def getPermutationsHelper03(res, array, pos):
    if pos == len(array) - 1:
        res.append(array[:])
        return

    for i in range(pos, len(array)):
        # place the element of interest at the first position (pos)
        #  Example: for getPermutationsHelper03(res, [], [1,2,3], 0), while in this for loop
        #       when at value 1 (i=0), we want 1 to be at pos(0), so that we can iterate through [2,3,4] next without adding 1 again
        #       when at 2, we want 2 to be at pos(0), so that we can iterate through [1,3,4] next ([2,1,3,4])
        #       when at 3, we want it to be at pos(0), so that we can iterate through [2,1,4] next ([3,2,1,4])
        #   so we have to manually place it there (via swapping with the element at pos), then we return it just before the loop ends
        # and move pos forward
        # place the element of interest at the first position (pos)
        swap03(array, pos, i)
        getPermutationsHelper03(res, array, pos+1)
        # return the element of interest to its original position
        swap03(array, i, pos)


# -> we have n! leaves each with, n calls to the helper method, & each helper method does 1 work
# Upper Bound: O(n*n!) time | O(n*n!) space
# Roughly: O(n*n!) time | O(n*n!) space
def getPermutations03(array):
    res = []
    getPermutationsHelper03(res, array, 0)
    return res


"""
order data:

solve little then big cases:
[1] -> [[1]]
[1,2] -> [[1,2], [2,1]]
[1,2,3] -> 

[
[1,2,3], [1,3,2],
[2,1,3], [2,3,1], 
[3,1,2], [3,2,1]
]

recursion stack:
Legend: [current_perm][remaining_nums_in_array]

perm(1,2)
			  [][1,2]
	  [1][2]	 [2][1]
	[1,2][]       [2,1][]     

perm(1,2,3)
							[][1,2,3]
				/			  |                \
		  [1][2,3]	        [2][1,3]           [3][2,1]
		  /  \              /      \              /   \
	[1,2][3] [1,3][2]    [2,1][3] [2,3][1]   [3,2][1] [3,1][2]
	|             |          |         |          |         |
  [1,2,3]      [1,3,2]    [2,1,3]   [2,3,1]    [3,2,1]    [3,1,2]

"""
