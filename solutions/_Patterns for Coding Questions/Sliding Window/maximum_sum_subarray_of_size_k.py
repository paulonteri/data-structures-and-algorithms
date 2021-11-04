""" 
Maximum Sum Subarray of Size K:

Given an array of positive numbers and a positive number ‘k,’ 
find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:
    Input: [2, 1, 5, 1, 3, 2], k=3 
    Output: 9
    Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:
    Input: [2, 3, 4, 1, 5], k=2 
    Output: 7
    Explanation: Subarray with maximum sum is [3, 4].
https://www.educative.io/courses/grokking-the-coding-interview/JPKr0kqLGNP
"""

""" 
## Q
Given array, find the max contiguous array of size k
"""

""" 
## SOLUTION

# Brute force
- create all contiguous subarrays of size k possible & find each of their sums then return the max 
    - this can be done by iterating k-1 steps forward at each point in the array

# Optimal
- create a window of size k, and record its sum
- iterate through the array, 
    adding the next element to the window (adding it to the sum), & at the same time
    remove the 1st element in the window (remove its value from the sum),
    record the sum if it is larger than the prev recorded sum
- repeat the step above till each subarray is considered

[0,1,2,3,4], k=3 +> 9
"""

# l=0, r=2 c=6, m=3
# l=1, r=3, c=6, m=6
# l=2, r=4, c=9, m=9


def max_sub_array_of_size_k(k, arr):
    if len(arr) < k:
        return -1

    curr_sum = 0
    maximum = -1

    # first subarray -> create window
    for idx in range(k):
        curr_sum += arr[idx]
    maximum = curr_sum

    # other subarrays
    for idx in range(1, len(arr)-(k-1)):
        curr_sum -= arr[idx-1]  # remove from window
        curr_sum += arr[idx+(k-1)]  # add to window
        maximum = max(curr_sum, maximum)

    return maximum


print(max_sub_array_of_size_k(3, [0, 1, 2, 3, 4]))
