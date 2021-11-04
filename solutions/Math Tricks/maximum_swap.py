""" 
670. Maximum Swap:

You are given an integer num. You can swap two digits at most once to get the maximum valued number.
Return the maximum valued number you can get.

Example 1:
    Input: num = 2736
    Output: 7236
    Explanation: Swap the number 2 and the number 7.
Example 2:
    Input: num = 9973
    Output: 9973
    Explanation: No swap.

Needs many examples to understand
Drawing a chart of heaps and valleys can make it a bit easier to understand

4123 => 4321  
4312 => 4321 
4321 => 4321 
98368 => 98863
1993 => 9913

https://leetcode.com/problems/maximum-swap

similar to https://leetcode.com/problems/next-permutation/
"""


# use two pointers
class Solution:
    def maximumSwap(self, num: int):
        """ 
        Ensure the largest value is as left as possible
        """
        num_arr = list(str(num))

        for i in range(len(num_arr)):
            # find largest that is as right as possible: eg 1993 => 9913
            largest = i
            for idx in range(i+1, len(num_arr)):
                if int(num_arr[idx]) >= int(num_arr[largest]):
                    largest = idx

            # if we found a larger value, swap & return
            if int(num_arr[largest]) > int(num_arr[i]):
                num_arr[largest], num_arr[i] = num_arr[i], num_arr[largest]
                return int("".join(num_arr))

        return num
