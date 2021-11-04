""" 
Continuous Subarray Sum:

Given an integer array nums and an integer k, 
    return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, 
    or false otherwise.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

Example 1:
    Input: nums = [23,2,4,6,7], k = 6
    Output: true
    Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
Example 2:
    Input: nums = [23,2,6,4,7], k = 6
    Output: true
    Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
    42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
Example 3:
    Input: nums = [23,2,6,4,7], k = 13
    Output: false

https://leetcode.com/problems/continuous-subarray-sum

Prerequisite: Subarray Sum Equals K https://leetcode.com/problems/subarray-sum-equals-k/
"""


"""

    [1, 2, 3, 4,]
    [1, 3, 6, 10]
    10-1 =  19  = 2+3+4
    6-1  =   5  = 2+3

if we store the cumulative sum for every point (idx) in the array,
    if (sum2-sum1) % k = 0
    then the numbers between sum2-sum1 add up to a multiple of k


Remember, there's another aspect to this problem. The subarray must have a minimum size of 2.
"""


class SolutionBF:
    def checkSubarraySum(self, nums, k):
        if len(nums) < 2:
            return False

        # 0: -1 is for edge case that current sum mod k == 0
        # for when the current running sum is cleanly divisible by k
        # e.g: nums = [4, 2], k = 3
        sums = {0: -1}  # 0
        cumulative_sum = 0
        for idx, num in enumerate(nums):
            cumulative_sum += num

            for prev_sum in sums:
                if (cumulative_sum-prev_sum) % k == 0 and idx-sums[prev_sum] >= 2:
                    return True

            # if current sum mod k not in dict, store it so as to ensure the further values stay
            if cumulative_sum not in sums:
                sums[cumulative_sum] = idx

        return False


"""
    [1, 2, 3, 4,]  <= array
    [1, 3, 6, 10] <= cumulative sums
    10 -1 =  19  = 2+3+4
    6 -1  =   5  = 2+3

if we store the cumulative sum for every point (idx) in the array,
    if (sum2-sum1) % k = 0
    then the numbers between sum2-sum1 add up to a multiple of k

if you find duplicated sum%k values, then that the sub array between those two indexes will actually be the solution.

---

eg: [15,10,10], k = 10
    15%10 = 5
    25%10 = 5
    35%10 =5

Did you realize something? No
Let's see- the sums 15 and 25 are giving the remainder 5 when divided by 10 and the difference between 15 and 25 i.;e. 10 is divisible by 10.
Let's check with sums 15 and 35 , both giving the remainder 5 but their difference is divisible by 10.

---

eg: [23, 2, 4, 6, 7], k = 6
    [23,25,29, ...]

    23%6 = 5
    25%6 = 1
    29%6 = 5

The cumulative sums 23 and 29 have the same remainder,
    and their difference is a multiple of 6 (6 (2+4))

Why is getting 5 twice significant here?
    Given any number, let's say 11 and another number 5.
    11%5 = 1

    After adding how much to 11 would we get remainder with 5 equal to 1 again?
    The answer is 5.
    In order to repeat a remainder you need to add the number you are dividing by, in this case 5.

    if 11%5 = 1
    then (11+5)%5 = 1
    (11+10)%5 = 1 and so on

    Therefore as in the above example, because we saw 5 as remainder repeat, that means that, 
        there was a cumulative sum somewhere in the list that added up to 6 (number we are dividing by). 
    That's why we would return true.


---

If two sums A and B are giving the same remainder when divided by a number K, then their difference abs(A-B) is always divisible by K.
Simply, If you get the same remainder again, it means that you've encountered some sum which is a multiple of K.
- Their difference is a multiple of k, that's why they have the same remainder

Additional logic:
(sum2-sum1) % k = 0
sum2%k - sum1%k = 0
sum2%k = sum1%k

https://leetcode.com/problems/continuous-subarray-sum/discuss/688125/Lehman-explanation-of-the-math
https://leetcode.com/problems/continuous-subarray-sum/discuss/1208948/Complete-explanation-or-mathematical-or-code-with-proper-comments-or-O(N)-or-continuous-subarray-sum
https://leetcode.com/problems/continuous-subarray-sum/discuss/338417/Python-Solution-with-explanation
https://www.notion.so/paulonteri/Strings-Arrays-Linked-Lists-81ca9e0553a0494cb8bb74c5c85b89c8#1a8542c704d949a196a82d0d08117435

Remember, there's another aspect to this problem. The subarray must have a minimum size of 2.
"""


class Solution:
    def checkSubarraySum(self, nums, k):
        if len(nums) < 2:
            return False

        # 0: -1 is for edge case that current sum mod k == 0
        # for when the current running sum is cleanly divisible by k
        # e.g: nums = [4, 2], k = 3
        sums = {0: -1}  # 0
        cumulative_sum = 0
        for idx, num in enumerate(nums):
            cumulative_sum += num
            remainder = cumulative_sum % k

            # if current_sum mod k is in dict and index idx - sums[remainder] > 1, we got the Subarray!
            # we use 2 not 1 because the element at sums[remainder] is not in the subarray we are talking about
            if remainder in sums and idx - sums[remainder] >= 2:
                return True

            # if current sum mod k not in dict, store it so as to ensure the further values stay
            if remainder not in sums:
                sums[remainder] = idx
