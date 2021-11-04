""" 
101. Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

https://leetcode.com/problems/symmetric-tree/

        1
       / \
      2   2  
     / \  / \
    3  4  4  3      
True
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution_:
    def isSymmetric(self, root):

        queue = [(root, 0, 0)]
        store = set()
        while queue:
            node, depth, horizontal = queue.pop(0)

            # # add children
            if node.left:
                queue.append((node.left, depth+1, horizontal-1))
            if node.right:
                queue.append((node.right, depth+1, horizontal+1))

            # # visit
            curr = (node.val, depth, horizontal)
            opposite_curr = (node.val, depth, horizontal*-1)
            #
            if opposite_curr in store:
                store.remove(opposite_curr)
            else:
                store.add(curr)

        return len(store) == 1


""" 
"""


class Solution:
    def isSymmetric(self, root):
        queue = [root.left, root.right]

        while queue:
            one = queue.pop(0)
            two = queue.pop(0)

            if one == None or two == None:
                if one == None and two == None:
                    continue
                else:
                    return False
            if one.val != two.val:
                return False

            # # add children
            # the left child of one will match with the right child of two (diagram)
            queue.append(one.left)
            queue.append(two.right)
            # the right child of one will match with the left child of two (diagram)
            queue.append(one.right)
            queue.append(two.left)

        return True
