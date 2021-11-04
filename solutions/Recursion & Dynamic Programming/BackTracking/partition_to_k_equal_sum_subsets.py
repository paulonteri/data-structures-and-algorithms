""" 
Partition to K Equal Sum Subsets

Given an integer array nums and an integer k, 
return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:
    Input: nums = [4,3,2,3,5,2,1], k = 4
    Output: true
    Explanation: 
        It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Example 2:
    Input: nums = [1,2,3,4], k = 3
    Output: false
"""

from typing import List


""" 
Our goal is to break the given array into k subsets of equal sums.
Firstly, we will check if the array sum can be evenly divided into k parts by ensuring that totalArraySum % k is equal to 0.
Now, if the array sum can be evenly divided into k parts, we will try to build those k subsets using backtracking.

O(N.N!) time | O(N) space:
- The idea is that for each recursive call, we will iterate over N elements and make another recursive call. 
    Assume we picked one element, then we iterate over the array and make recursive calls for the next N-1 elements and so on.
    Therefore, in the worst-case scenario, 
        the total number of recursive calls will be N⋅(N−1)⋅(N−2)⋅...⋅2⋅1=N! and in each recursive call we perform an O(N) time operation.
- Another way is to visualize all possible states by drawing a recursion tree. 
    From root node we have NN recursive calls. The first level, therefore, has N nodes. 
    For each of the nodes in the first level, we have (N-1) similar choices. 
    As a result, the second level has N∗(N−1) nodes, and so on. The last level must have N⋅(N−1)⋅(N−2)⋅(N−3)⋅...⋅2⋅1 nodes.

- make a subset with sum totalArraySum/k
    - reduce the needed(k) by one
    - start again with other numbers
-repeat the above till the needed substets == 0
"""


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int):
        # get required subset size
        target_sum = sum(nums)/k
        if int(target_sum) != target_sum:
            return False  # cannot have valid subsets

        # nums.sort(reverse=True)
        taken = [False]*len(nums)

        def backtracking(curr_sum, curr_k, idx):
            if curr_sum > target_sum:
                return False
            if curr_k == k:
                return True
            # When current subset sum reaches target sum then one subset is made.
            # Increment count and reset current subset sum to 0.
            if curr_sum == target_sum:
                return backtracking(0, curr_k+1, 0)

            # check if you starting to visit at a current index will give us the subsets
            for i in range(idx, len(nums)):
                # try not picked elements to make some combinations.
                if taken[i]:
                    continue

                # visit (Include this element in current subset)
                taken[i] = True
                if backtracking(curr_sum+nums[i], curr_k, i+1):
                    return True  # if the current index works out, none other can
                # un-visit (Backtrack step)
                taken[i] = False

            # We were not able to make a valid combination after picking
            # each element from the array, hence we can't make k subsets.
            return False

        return backtracking(0, 0, 0)


""" 
Memoization:

O(N.2^N) time | O(N.2^N) space:
- There will be N^2 unique combinations of the taken tuple, 
    in which every combination of the given array will be linearly iterated. 
    And if a combination occurs again then we just return the stored answer for it.
- So for each subset, we are choosing the suitable elements from the array 
    (basically iterate over nums and for each element either use it or skip it, which is O(N.2^N) operation)
- The idea is that we have two choices for each element: include it in the subset OR not include it in the subset. 
    We have N such elements. Therefore, the number of cases for events of including/excluding all numbers is: 2⋅2⋅2⋅...(N times)..⋅2 = 2^N
- Another way is to visualize all possible states by drawing a recursion tree. 
    In the first level, we have 2 choices for the first number, including the first number in the current subset or not. 
    The second level, therefore, has 2 nodes. For each of the nodes in the second level, we have 2 similar choices. 
    As a result, the third level has 2^2 nodes, and so on. 
    The last level must have 2^N nodes.
"""


class Solution_:
    def canPartitionKSubsets(self, nums: List[int], k: int):
        # get required subset size
        target_sum = sum(nums)/k
        if int(target_sum) != target_sum:
            return False  # cannot have valid subsets

        # nums.sort(reverse=True)
        taken = [False]*len(nums)
        cache = {}

        def backtracking(curr_sum, curr_k, idx):
            if curr_sum > target_sum:
                return False
            if curr_k == k:
                return True
            if tuple(taken) in cache:
                return cache[tuple(taken)]
            # When current subset sum reaches target sum then one subset is made.
            # Increment count and reset current subset sum to 0.
            if curr_sum == target_sum:
                cache[tuple(taken)] = backtracking(0, curr_k+1, 0)
                return cache[tuple(taken)]

            # check if you starting to visit at a current index will give us the subsets
            for i in range(idx, len(nums)):
                # try not picked elements to make some combinations.
                if not taken[i]:
                    # visit (Include this element in current subset)
                    taken[i] = True
                    if backtracking(curr_sum+nums[i], curr_k, i+1):
                        return True  # if the current index works out, none other can
                    # un-visit (Backtrack step)
                    taken[i] = False

            # We were not able to make a valid combination after picking
            # each element from the array, hence we can't make k subsets.
            cache[tuple(taken)] = False
            return cache[tuple(taken)]

        return backtracking(0, 0, 0)
