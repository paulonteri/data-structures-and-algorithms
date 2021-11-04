"""
Longest Peak:

Write a function that takes in an array of integers and returns the length of the longest peak in the array.
A peak is defined as adjacent integers in the array that are strictly increasing until they reach a tip (the highest value in the peak),
 at which point they become strictly decreasing. At least three integers are required to form a peak.

For example, the integers 1, 4, 10, 2 form a peak, but the integers 4, 0, 10 don't and neither do the integers 1, 2, 2, 0. 
 Similarly, the integers 1, 2, 3 don't form a peak because there aren't any strictly decreasing integers after the 3.

Sample Input
    array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
Sample Output
    6 
    # 0, 10, 6, 5, -1, -3
"""


# O(n) time | O(1) space - where n is the length of the input array
def longestPeak(array):

    def findPeakLength(idx):
        increased_length = 0
        decreased_length = 0

        prev = None
        curr = idx
        if not (curr + 1 < len(array)) or array[curr + 1] <= array[curr]:
            # if next is not increasing
            return 0
        else:
            increased_length += 1
            prev = curr
            curr += 1

        # increasing
        while curr < len(array) and array[curr] > array[prev]:
            if not curr + 1 < len(array):
                return 0  # we won't be able to reach tha decreasing section

            increased_length += 1
            prev = curr
            curr += 1

        # decreasing
        while curr < len(array) and array[curr] < array[prev]:
            decreased_length += 1
            prev = curr
            curr += 1

        if decreased_length > 0:
            return decreased_length + increased_length
        return 0

    longest_len = 0
    for index in range(len(array)):
        longest_len = max(longest_len, findPeakLength(index))

    return longest_len


x = [0, 1, 2, 3, 4, 3, 2]
y = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
z = [5, 4, 3, 2, 1, 2, 1]
p = [5, 4, 3, 2, 1, 2, 10, 12]
q = [1, 2, 3, 4, 3, 2, 1]
print(longestPeak(x))
print(longestPeak(y))
print(longestPeak(z))
print(longestPeak(p))
print(longestPeak(q))
