"""
Next Greater Element:

Write a function that takes in an array of integers
 and returns a new array containing,at each index,
 the next element in the input array that's greater than the element at that index in the input array.
In other words, your function should return a new array
 where outputArray[i] is the next element in the input array that's greater than inputArray[i].
If there's no such next greater element for a particular index,
 the value at that index in the output array should be -1.

For example, given array = [1, 2], your function should return [2, -1].
Additionally, your function should treat the input array as a circular array.
 A circular array wraps around itself as if it were connected end-to-end.
 So the next index after the last index in a circular array is the first index.
 This means that, for our problem, given array = [0, 0, 5, 0, 0, 3, 0 0],
  the next greater element after 3 is 5, since the array is circular.

Sample Input
    array = [2, 5, -3, -4, 6, 7, 2]
    Sample Output
    [5, 6, 6, 6, 7, -1, 5]

https://www.algoexpert.io/questions/Next%20Greater%20Element
"""


# O(n) time | O(n) space - where n is the length of the array
def nextGreaterElement00(array):
    res = [-1] * len(array)

    # stack used to store the previous smaller numbers that haven't been replaced
    # stored in the form of {'idx': 0, 'val': 0}
    be_replaced_stack = []

    for i in range(len(array)*2):  # loop through twice because the array is circular
        array_idx = i % len(array)  # prevent out of bound errors

        # check if we have found some values in the be_replaced_stack stack
        #   that is smaller than the current array value array[array_idx]
        #   then replace them (their corresponding values in res)
        while len(be_replaced_stack) > 0 and be_replaced_stack[-1]['val'] < array[array_idx]:

            to_be_replaced = be_replaced_stack.pop()['idx']
            res[to_be_replaced] = array[array_idx]

        # add the current element to the be_replaced_stack so that it can be checked in the futere for replacement
        be_replaced_stack.append({'idx': array_idx, 'val': array[array_idx]})

    return res


# O(n) time | O(n) space - where n is the length of the array
def nextGreaterElement01(array):
    res = [-1] * len(array)

    # stack used to store the previous smaller numbers' indices that haven't been replaced
    be_replaced_stack = []

    for i in range(len(array)*2):  # loop through twice because the array is circular
        array_idx = i % len(array)  # prevent out of bound errors

        # check if we have found some values in the be_replaced_stack stack
        #   that is smaller than the current array value array[array_idx]
        #   then replace them (their corresponding values in res)
        while len(be_replaced_stack) > 0 and array[be_replaced_stack[-1]] < array[array_idx]:
            res[be_replaced_stack.pop()] = array[array_idx]

        # add the current element to the be_replaced_stack so that it can be checked in the futere for replacement
        be_replaced_stack.append(array_idx)

    return res


"""
# we will use a stack to keep track of the past values that have not been replaced
#  once we find a bigger element, we replace them and remove them from the stack
#  then add the big element to the stack in the hope that it will be replaced

array = [0, 1,  2,  3, 4, 5, 6] <= indices
array = [2, 5, -3, -4, 6, 7, 2]

---
num = 2 (index 0)
res = [-1, -1, -1, -1, -1, -1, -1]
stack = [2]

num = 5 (index 1)
res = [5, -1, -1, -1, -1, -1, -1]
stack = [5] -> replaced all smaller values in res and the stack

num = -3
res = [5, -1, -1, -1, -1, -1, -1]
stack = [5, -3]

num = -4 (index 3)
res = [5, -1, -1, -1, -1, -1, -1]
stack = [5, -3, -4]

num = 6 (index 4)
res = [5, 6, 6, 6, -1, -1, -1]
stack = [6] -> replaced all smaller values in res and the stack

num = 7 (index 5)
res = [5, 6, 6, 6, 7, -1, -1]
stack = [7] -> replaced all smaller values in res and the stack

num = 2 (index 6)
res = [5, 6, 6, 6, 7, -1, -1]
stack = [7,2]

num = 2 (index 0)
res = [5, 6, 6, 6, 7, -1, -1]
stack = [7,2,2]
---

"""


# O(n) time | O(n) space - where n is the length of the array
def nextGreaterElement(array):
    res = [-1] * len(array)

    # stack used to store the previous smaller numbers that haven't been replaced
    next_nums_stack = []

    # loop through twice because the array is circular
    for i in reversed(range(len(array)*2)):
        array_idx = i % len(array)  # prevent out of bound errors

        while len(next_nums_stack) > 0:
            # if value at the top of the stack is smaller than the current value in the array,
            #	remove it from the stack till we find something larger
            if next_nums_stack[-1] <= array[array_idx]:
                next_nums_stack.pop()

            # replace the value in the array by the
            #	value at the top of the stack (if stack[-1] is larger)
            else:
                res[array_idx] = next_nums_stack[-1]
                break

        # add the current element to the next_nums_stack so that it can be checked in the futere for replacement
        next_nums_stack.append(array[array_idx])

    return res
