"""
Smallest Subarray with a given sum:

Given an array of positive numbers and a positive number ‘S,’
find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’.
Return 0 if no such subarray exists.

Example 1:
    Input: [2, 1, 5, 2, 3, 2], S=7
    Output: 2
    Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].
Example 2:
    Input: [2, 1, 5, 2, 8], S=7
    Output: 1
    Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
Example 3:
    Input: [3, 4, 1, 1, 6], S=8
    Output: 3
    Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1]
    or [1, 1, 6].

https://www.educative.io/courses/grokking-the-coding-interview/7XMlMEQPnnQ
"""

"""
Explanation 1:

- Maintain a window of at least length 1 and the sum curr_sum of all its elements
    - if the sum curr_sum is less than s, add a number to the window
    - if the sum curr_sum is greater or equal to s,
        compare the window's length to the previous smallest_window_length & record the smallest then,
        remove the first element from the window
    - if the length of the windom == 1, increase the window size

- return the smallest_window_length
"""


def decrease_window(curr_sum, arr, left):
    curr_sum -= arr[left]
    left += 1
    return left, curr_sum


def increase_window(curr_sum, arr, right):
    right += 1
    curr_sum += arr[right]
    return right, curr_sum


def smallest_subarray_with_given_sum_01(s, arr):
    if not arr or len(arr) < 1:
        return -1
    smallest_len = float('inf')

    # window boundary
    left = 0
    right = 0
    curr_sum = arr[0]

    while left < len(arr):
        if curr_sum >= s:
            smallest_len = min(smallest_len, (right-left)+1)

        # cannot increase window
        if right >= len(arr)-1:
            left, curr_sum = decrease_window(curr_sum, arr, left)

        # cannot decrease window
        elif right == left:
            right, curr_sum = increase_window(curr_sum, arr, right)

        elif curr_sum >= s:
            left, curr_sum = decrease_window(curr_sum, arr, left)
        else:
            right, curr_sum = increase_window(curr_sum, arr, right)

    if smallest_len == float('inf'):
        return -1
    return smallest_len


"""
Explanation 2:

---

- first, we sum up elements from the beginning of the array until their sum becomes >= s
    These elements will constitute our sliding window.
    We will remember the length of this window as the smallest window so far.
- after this we keep adding one element to the window at every loop
- at each step, we try to shrink the window, 
    we shrink the window till its sum is < s to find the smallest window
    - as we do this we try to keep updating the smallest length we have seen soo far

---

- increase the window till you get a sum >= s
- then decrease the window till your sum becomes < s (while keeping track of the smallest lengths)
- repeat till the end of the array

"""


def smallest_subarray_with_given_sum(s, arr):
    if not arr or len(arr) < 1:
        return -1
    smallest_len = float('inf')

    left = 0
    curr_sum = 0
    for right in range(len(arr)):
        curr_sum += arr[right]

        while left <= right and curr_sum >= s:
            smallest_len = min(smallest_len, (right-left)+1)

            # decrease window
            curr_sum -= arr[left]
            left += 1

    if smallest_len == float('inf'):
        return -1
    return smallest_len
