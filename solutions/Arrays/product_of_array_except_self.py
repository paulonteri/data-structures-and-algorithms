"""
Array Of Products:
Product of Array Except Self:

Write a function that takes in a non-empty array of integers and returns an array of the same length,
 where each element in the output array is equal to the product of every other number in the input array.
In other words, the value at output[i] is equal to the product of every number in the input array other than input[i].

Note that you're expected to solve this problem without using division.

https://www.algoexpert.io/questions/Array%20Of%20Products
https://leetcode.com/problems/product-of-array-except-self/
"""


# O(n) time | O(n) space - where n is the length of the input array (O(3n) time)
def arrayOfProducts(array):
    res = array[:]

    # We know that for each element, the product of all other elements
    #  will be equal to the the products of the elements to its right and and the products of the elements to its left
    # we can try to calculate that beforehand

    # multiply left & right products for each element
    left_products = [0]*len(array)
    running_left = 1  # first element will have a product of 1
    for idx in range(len(array)):
        left_products[idx] = running_left
        running_left = array[idx] * running_left

    # calculate products to the right of elements
    right_products = [0]*len(array)
    running_right = 1  # last element will have a product of 1
    for idx in reversed(range(len(array))):
        right_products[idx] = running_right
        running_right = array[idx] * running_right

    # multiply left & right products for each element
    for idx in range(len(array)):
        res[idx] = left_products[idx] * right_products[idx]

    return res


y = [5, 1, 4, 2]
x = [1, 2, 3, 4, 5]
print(arrayOfProducts(x))
print(arrayOfProducts(y))
