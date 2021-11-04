"""
Same BSTs:

An array of integers is said to represent the Binary Search Tree (BST) obtained by inserting each integer in the array, from left to right, into the BST.
Write a function that takes in two arrays of integers and determines whether these arrays represent the same BST. Note that you're not allowed to construct any BSTs in your code.
A BST is a Binary Tree that consists only of BST nodes. 
A node is said to be a valid BST node if and only if it satisfies the BST property:
 its value is strictly greater than the values of every node to its left;
 its value is less than or equal to the values of every node to its right; 
 and its children nodes are either valid BST nodes themselves or None / null.

Sample Input
    arrayOne = [10, 15, 8, 12, 94, 81, 5, 2, 11]
    arrayTwo = [10, 8, 5, 15, 2, 12, 11, 94, 81]
Sample Output
    true // both arrays represent the BST below
            10
        /     \
        8      15
      /       /   \
    5        12     94
    /       /     /
    2       11    81

https://www.algoexpert.io/questions/Same%20BSTs 
"""


# O(n^2) time | O(n^2) space - where n is the number of nodes in each array, respectively
def _sameBsts(arrayOne, arrayTwo):
    return sameBstsHelper(arrayOne, arrayTwo)


def sameBstsHelper(arrayOne, arrayTwo):
    # must be same length
    if len(arrayOne) != len(arrayTwo):
        return False

    # we didn't find anything wrong
    if len(arrayOne) == 0:  # any -> arrayOne/arrayTwo
        return True

    # must have same head
    if arrayOne[0] != arrayTwo[0]:
        return False

    # # split into right and left
    # elements larger or equal to than idx 0
    right_one = []
    right_two = []
    # elements smaller than idx 0
    left_one = []
    left_two = []
    for idx in range(1, len(arrayOne)):  # any -> arrayOne/arrayTwo

        # one
        if arrayOne[idx] < arrayOne[0]:
            left_one.append(arrayOne[idx])
        else:
            right_one.append(arrayOne[idx])

        # two
        if arrayTwo[idx] < arrayTwo[0]:
            left_two.append(arrayTwo[idx])
        else:
            right_two.append(arrayTwo[idx])

    left = sameBstsHelper(left_one, left_two)
    right = sameBstsHelper(right_one, right_two)

    return left and right


"""
# ----------------------------------------------------------------------------------------------------------------------

# check roots
- `build bst `(find all the roots at every point in the tree) and validate that they are same
"""


# O(n^2) time | O(d) space
# where n is the number of nodes in each array, respectively,
# and d is the depth of the BST that they represent
def sameBsts(array_one, array_two):
    return buildTrees(array_one, array_two, 0, 0, float('-inf'), float('inf'))


def buildTrees(array_one, array_two, idx_one, idx_two, minimum, maximum):
    # no extra elements to add (reached end)
    if idx_one == None or idx_two == None:
        return idx_one == idx_two

    # validate roots (roots should be same)
    if array_one[idx_one] != array_two[idx_two]:
        return False

    curr = array_one[idx_one]

    left_one = findNextValidSmaller(array_one, idx_one, minimum)
    left_two = findNextValidSmaller(array_two, idx_two, minimum)
    right_one = findNextValidLargerOrEqual(array_one, idx_one, maximum)
    right_two = findNextValidLargerOrEqual(array_two, idx_two, maximum)

    left = buildTrees(
        # the curr is the largest there will ever be
        array_one, array_two, left_one, left_two, minimum, curr)
    right = buildTrees(
        # curr is the smallest
        array_one, array_two, right_one, right_two, curr, maximum)

    return left and right


def findNextValidSmaller(array, starting_idx, running_minimum):
    # used to find the next left root
    # Find the index of the first smaller value after the startingIdx.
    # Make sure that this value is greater than or equal to the minVal,
    # which is the value of the previous parent node in the BST.
    # If it isn't, then that value is located in the left subtree of the
    # previous parent node.
    for idx in range(starting_idx + 1, len(array)):
        if array[idx] < array[starting_idx] and array[idx] >= running_minimum:
            return idx
    return None


def findNextValidLargerOrEqual(array, starting_idx, running_maximum):
    # used to find the next right root
    # Find the index of the first bigger/equal value after the startingIdx.
    # Make sure that this value is smaller than maxVal, which is the value
    # of the previous parent node in the BST.
    # If it isn't, then that value is located in the right subtree of the previous parent node.
    for idx in range(starting_idx + 1, len(array)):
        if array[idx] >= array[starting_idx] and array[idx] < running_maximum:
            return idx
    return None
