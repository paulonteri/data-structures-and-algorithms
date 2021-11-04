"""
Maximum Product Subarray:
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.
Example 1:
    Input: [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.
Example 2:
    Input: [-2,0,-1]
    Output: 0
    Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
    
https://leetcode.com/problems/maximum-product-subarray/
https://afteracademy.com/blog/max-product-subarray
"""


# O(n) time | O(1) space
class Solution:
    def maxProduct(self, array):

        if not array:
            return -1

        max_product = curr_max = curr_min = array[0]

        for idx in range(1, len(array)):

            temp_curr_max = curr_max
            curr_max = max(
                curr_max * array[idx],
                curr_min * array[idx],  # if array[idx] is negative [-2, 3, -4]
                array[idx]  # helps if array[idx-1] is 0 eg: [0, 2]
            )
            curr_min = min(
                temp_curr_max * array[idx],
                curr_min * array[idx],
                array[idx]
            )

            max_product = max(max_product, curr_max)

        return max_product


sol = Solution()
print(sol.maxProduct([2, 2, 2, 1, -1, 5, 5]))
print(sol.maxProduct([-2, 3, -4]))
print(sol.maxProduct([2]))
print(sol.maxProduct([]))
print(sol.maxProduct([-5]))
print(sol.maxProduct([0, 2, 2, 2, 1, -1, -5, -5]))
print(sol.maxProduct([0, 2]))

"""
Dynamic Programming:

Imagine that we have both max_prod[i] and min_prod[i] i.e. max product ending at i and min product ending at i.

Now if we have a negative number at arr[i+1] and if min_prod[i] is negative,
then the product of the two will be positive and can potentially be the largest product.
So, the key point here is to maintain both the max_prod and min_prod such that at iteration i, they refer to the max and min product ending at index i-1.

In short, One can have three options to make at any position in the array.
- You can get the maximum product by multiplying the current element with the maximum product calculated so far. (might work when current
  element is positive).
- You can get the maximum product by multiplying the current element with minimum product calculated so far. (might work when current
  element is negative).
- The current element might be a starting position for maximum product subarray.
Solution Steps

Initialize maxProduct with arr[0] to store the maximum product so far.
Initialize to variables imax and imin to store the maximum and minimum product till i .
Iterate over the arr and for each negative element of arr, swap imax and imin. (Why?)
Update imax and imin as discussed above and finally return maxProduct
"""
