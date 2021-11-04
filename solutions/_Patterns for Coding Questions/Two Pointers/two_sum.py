"""
Two Sum:

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

https://leetcode.com/problems/two-sum/
https://www.algoexpert.io/questions/Two%20Number%20Sum
https://www.educative.io/courses/grokking-the-coding-interview/xog6q15W9GP

Do next:
- Pairs with Specific Difference
"""


class Solution:
    # O(n) space | O(n) time
    def twoSum(self, nums, target):
        # store to keep the values in the list and their respective indices
        # in the form; { value:indice, value:indice, }
        store = {}

        indice = 0
        for num in nums:
            # calculate the number required
            requiredNum = target - num

            # check if the required number is in the 'store'
            if store.get(requiredNum) is None:
                # add it to store
                store[num] = indice
            else:
                return [indice, store[requiredNum]]

            indice += 1


"""
Two Number Sum:

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order. 
If no two numbers sum up to the target sum, the function should return an empty array.
Note that the target sum has to be obtained by summing two different integers in the array;
you can't add a single integer to itself in order to obtain the target sum.
You can assume that there will be at most one pair of numbers summing up to the target sum.
"""


# θ(n log(n)) time | 0(1) space
def twoNumberSum(array, targetSum):
    array.sort()

    left = 0
    right = len(array)-1
    while left < right:
        curr_sum = array[left] + array[right]
        if curr_sum > targetSum:
            right -= 1
        elif curr_sum < targetSum:
            left += 1
        else:
            return [array[left], array[right]]
        return []


"""
Input: array of integers
Output: array of two integers
Assumptions:
    - (False) there will always be two numbers that will add up to the sum

# simple example:
array = [1,2,5,3,4,9],  target = 9
ans = [5,4]

# Approach one: O(n^2) time
- for each number in the array, try to find a number that will add up to the target

## approach two:
- sort the array
- have two pointers at different ends of the array (left & right)
- the current_sum = array[left] + array[right]
- if current_sum == target: return the values
- if the sum > target:
    - move the right pointer to the left by 1 (decrease the current_sum)
  else:
    - move the left pointer to the right by 1 (increase the current_sum)      

"""
