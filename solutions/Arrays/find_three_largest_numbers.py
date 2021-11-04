"""
Find Three Largest Numbers:

Write a function that takes in an array of at least three integers and, without sorting the input array,
 returns a sorted array of the three largest integers in the input array.
The function should return duplicate integers if necessary; for example, it should return [10, 10, 12] for an input array of [10, 5, 9, 10, 12].
"""


# O(n) time | O(1) space - where n is the length of the input array
def findThreeLargestNumbers(array):
    output = [float('-inf'), float('-inf'), float('-inf')]

    for num in array:
        if num >= output[2] or num > output[0]:  # can be added
            addFunction(output, num)

    return output


def addFunction(output, num):
    if num > output[2]:  # greater than last element
        output[0], output[1] = output[1], output[2]
        output[2] = num

    # greater than middle element or equal to last
    elif num == output[2] or num > output[1]:
        output[0], output[1] = output[1], num

    else:
        output[0] = num


"""
Sample Input
    array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
Sample Output
    [18, 141, 541]


# Input: Array of integers
# Output: sorted Array of three integers
# Assumptions:
    - all values in the array will be integers
    - len(array) >= 3

# Simple Example:
[3,2,6,10,4,9]
[2,3,6] at 10 -> [3,6,10] at 4 -> [4,6,10] at 9 -> [6,3,10]

[6,9,10]
# We need to figure out:
- how to insert into the output array

# # Simple Solution:  O(n) time | O(1) space
# iterate through each character and at each, 
    - check whether we can add it into out output array
    - if we can, add it (using a function we will create separately) 
# addFunction(array,num):
    - if num > output[2]:
        output[0], output[1] = output[1], output[2]
        output[2] =  num
    - elif num == output[2] or num > output[1]:
        output[0], output[1] = output[1], num
    - else:
        output[0] = num

    # Alternatively:
    - output.append(num)
    - output.sort()
    - output.pop(0)

def findThreeLargestNumbers(array):
    output = [float('-inf'), float('-inf'), float('-inf')]

    for num in array:
        if num >= output[2] or num > output[0]:
            addFunction(array, num)
    
    return output

# O(n) time | O(1) space - where n is the length of the input array

"""


def findThreeLargestNumbers2(array):
    largest = [float('-inf'), float('-inf'), float('-inf')]

    for num in array:
        if num >= largest[0]:
            updateLargest(largest, num)
    return largest


def updateLargest(largest, num):
    largest.append(num)
    largest.sort()
    largest.pop(0)
