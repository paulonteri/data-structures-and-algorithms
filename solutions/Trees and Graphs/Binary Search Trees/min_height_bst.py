"""
Min Height BST:
Convert Sorted Array to Binary Search Tree:

Write a function that takes in a non-empty sorted array of distinct integers, constructs a BST from the integers, and returns the root of the BST.
The function should minimize the height of the BST.
You've been provided with a BST class that you'll have to use to construct the BST.
Each BST node has an integer value, a left child node, and a right child node.
A node is said to be a valid BST node if and only if it satisfies the BST property:
 its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right;
  and its children nodes are either valid BST nodes themselves or None / null.
A BST is valid if and only if all of its nodes are valid BST nodes.
Note that the BST class already has an insert method which you can use if you want.

Sample Input
array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
Sample Output
         10
       /     \
      2      14
    /   \   /   \
   1     5 13   15
          \       \
           7      22
// This is one example of a BST with min height
// that you could create from the input array.
// You could create other BSTs with min height
// from the same array; for example:
         10
       /     \
      5      15
    /   \   /   \
   2     7 13   22
 /           \
1            14

https://www.algoexpert.io/questions/Min%20Height%20BST
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

similar to https://leetcode.com/problems/balance-a-binary-search-tree
"""


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


# ----------------------------------------------------------------------------------------------------------------------


# O(nlog(n)) time | O(n) space - where n is the length of the array
def minHeightBst00(array):
    return minHeightBstHelper00(array, None, 0, len(array)-1)


def minHeightBstHelper00(array, node, left, right):
    if left > right:
        return None

    mid = (left+right) // 2

    if node is None:
        node = BST(array[mid])
    else:
        node.insert(array[mid])

    minHeightBstHelper00(array, node, left, mid-1)  # left
    minHeightBstHelper00(array, node, mid+1, right)  # right

    return node


# ----------------------------------------------------------------------------------------------------------------------

# O(n) time | O(n) space - where n is the length of the array
# faster because we do not use the insert method
def minHeightBst01(array):
    return minHeightBstHelper01(array, 0, len(array)-1)


def minHeightBstHelper01(array, left, right):
    if left > right:
        return None

    mid = (left+right) // 2

    node = BST(array[mid])
    node.left = minHeightBstHelper01(array, left, mid-1)
    node.right = minHeightBstHelper01(array, mid+1, right)

    return node


"""
Sample Input
array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
Sample Output
         10
       /     \
      2      14
    /   \   /   \
   1     5 13   15
          \       \
           7      22
// This is one example of a BST with min height
// that you could create from the input array.
// You could create other BSTs with min height
// from the same array; for example:
         10
       /     \
      5      15
    /   \   /   \
   2     7 13   22
 /           \
1            14



				[1, 2, 5, 7, 10, 13, 14, 15, 22]->10
			[1, 2, 5, 7]->2	                     [13, 14, 15, 22]->
		[1]->1	  [5, 7]->5	  
		            [7][7]->7
"""
