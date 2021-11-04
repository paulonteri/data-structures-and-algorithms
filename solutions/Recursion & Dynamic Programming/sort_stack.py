""" 
Sort Stack: (Under stacks)

Write a function that takes in an array of integers representing a stack,
 recursively sorts the stack in place (i.e., doesn't create a brand new array), and returns it.
The array must be treated as a stack, with the end of the array as the top of the stack.
Therefore, you're only allowed to:
    Pop elements from the top of the stack by removing elements from the end of the array using the built-in .pop() method in your programming language of choice.
    Push elements to the top of the stack by appending elements to the end of the array using the built-in .append() method in your programming language of choice.
    Peek at the element on top of the stack by accessing the last element in the array.
You're not allowed to perform any other operations on the input array, 
 including accessing elements (except for the last element),
 moving elements, etc.. 
You're also not allowed to use any other data structures, and your solution must be recursive.

Sample Input
    stack = [-5, 2, -2, 4, 3, 1]
    Sample Output
    [-5, -2, 1, 2, 3, 4]
    
https://www.algoexpert.io/questions/Sort%20Stack
"""


# # this will work by looping through all the elements of the stack
# # a bottom-up recursion approach where we start by sorting a stack of len 0, len 1, then 2, then 3
# remove every element till we have an empty stack
#   then insert them one by one at their correct position

# O(n^2) time | O(n) space - where n is the length of the stack
def sortStack(stack):
    # base case
    if len(stack) == 0:
        return stack

    # remove element at the top (element top),
    # sort the rest of the stack,
    # insert top back to the stack but at its correct position
    #   this will be work easily because the rest of the stack is sorted
    top = stack.pop()
    sortStack(stack)
    insertElementInCorrectPosition(stack, top)
    return stack


# assumes stack is sorted or empty
def insertElementInCorrectPosition(stack, num):
    # base cases
    # correct positions to insert num
    if len(stack) == 0 or stack[-1] <= num:
        stack.append(num)

    # remove the element at the top and try to insert num at a lower position
    #   insert num at a lower position than top
    #   return top once that is done
    else:
        top = stack.pop()
        insertElementInCorrectPosition(stack, num)
        stack.append(top)
