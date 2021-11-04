""" 
4Sum:

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
    0 <= a, b, c, d < n
    a, b, c, and d are distinct.
    nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:
    Input: nums = [1,0,-1,0,-2,2], target = 0
    Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:
    Input: nums = [2,2,2,2,2], target = 8
    Output: [[2,2,2,2]]
"""


""" 
[1,0,-1,0,-2,2]

[-2, -1, 0, 0, 1, 2]

- four sum is a combination of two two_sums

- sort the input array so that we can skip duplicates

- have two loops with to iterate through all the possible two number combinations:
    - for the rest of the numbers: find a two sum that = target - (arr[idx_loop_one] + arr[idx_loop_two])
                
"""


class Solution:

    def fourSum(self, nums, target):
        res = []
        nums.sort()

        for one in range(len(nums)):
            if one > 0 and nums[one] == nums[one-1]:
                continue  # skip duplicates
            for two in range(one+1, len(nums)):
                if two > one+1 and nums[two] == nums[two-1]:
                    continue  # skip duplicates

                # # two sum
                needed = target - (nums[one] + nums[two])
                left = two + 1
                right = len(nums)-1
                while left < right:
                    # skip duplicates
                    if left > two + 1 and nums[left] == nums[left-1]:
                        left += 1
                        continue
                    if right < len(nums)-1 and nums[right] == nums[right+1]:
                        right -= 1
                        continue

                    total = nums[left] + nums[right]
                    if total < needed:
                        left += 1
                    elif total > needed:
                        right -= 1
                    else:
                        res.append(
                            [nums[one], nums[two], nums[left], nums[right]])
                        left += 1
                        right -= 1

        return res
