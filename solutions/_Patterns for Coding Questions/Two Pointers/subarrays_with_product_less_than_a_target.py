""" 
Subarrays with Product Less than a Target:

Given an array with positive numbers and a positive target number,
 find all of its contiguous subarrays whose product is less than the target number.

Example 1:
    Input: [2, 5, 3, 10], target=30 
    Output: [2], [5], [2, 5], [3], [5, 3], [10]
    Explanation: There are six contiguous subarrays whose product is less than the target.
Example 2:
    Input: [8, 2, 6, 5], target=50 
    Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5] 
    Explanation: There are seven contiguous subarrays whose product is less than the target.
"""

""" 

[2, 5, 2, 2, 3, 10], target=30 

2=>2 [    [2],]
2,5=>10[[2],     [2,5],[5]]
2,5,2=>20[[2],[2,5],[5],  [2,5,2],[5,2],[2],]
# Add 2
2,5,2,2=>40
5,2,2=>20 -[[2],[2,5],[5],[2,5,2],[5,2],[2],  [5,2,2],[2,2],[2],]
# Add 3
5,2,2,3=>60
2,2,3=>12 - [[2],[2,5],[5],[2,5,2],[5,2],[2],  [5,2,2],[2,2],[2],]
# Add 10
2,2,3,10=>120
2,3,10=>60
3,10=>30 - [[2],[2,5],[5],[2,5,2],[5,2],[2],[5,2,2],[2,2],[2],   [3,10], [10]]
# 


"""


# O(n^3) time | O(n^3) space in the worst case
def find_subarrays(arr, target):
    result = []

    prod = 1
    left = 0
    for right in range(len(arr)):

        # create window that has a prod < target
        prod *= arr[right]  # add right
        while left <= right and prod >= target:
            prod /= arr[left]
            left += 1

        # since the product of all numbers from left to right is less than the target therefore,
        #   all subarrays from left to right will have a product less than the target too;
        # to avoid duplicates, we will start with a subarray containing only arr[right] and then extend it - done it the other way around here

        # record result (all the subarrays of the current window ending with right)
        # O(n^2) time | O(n^2) space in the worst case
        for i in range(left, right+1):
            result.append(arr[i:right+1])

    return result


print(find_subarrays([2, 5, 3, 10], 30))
print(find_subarrays([8, 2, 6, 5], 50))
