"""
Product Sum:

Write a function that takes in a "special" array and returns its product sum.
A "special" array is a non-empty array that contains either integers or other "special" arrays.
The product sum of a "special" array is the sum of its elements, where "special" arrays inside it are summed themselves and then multiplied by their level of depth.
The depth of a "special" array is how far nested it is. For instance, the depth of [] is 1;
 the depth of the inner array in [[]] is 2; the depth of the innermost array in [[[]]] is 3.
Therefore, the product sum of [x, y] is x + y; the product sum of [x, [y, z]] is x + 2 * (y + z);
 the product sum of [x, [y, [z]]] is x + 2 * (y + 3z).

https://www.algoexpert.io/questions/Product%20Sum
"""


# O(n) time | O(d) space - where n is the total number of elements in the array,
# including sub-elements, and d is the greatest depth of "special" arrays in the array
def productSum(array, depth=1):
    total = 0

    for element in array:
        if type(element) == int:
            total += element
        else:
            total += productSum(element, depth+1)

    return total * depth


"""
Sample Input
    array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
Sample Output
    12 // calculated as: 5 + 2 + 2 * (7 - 1) + 3 + 2 * (6 + 3 * (-13 + 8) + 4)
Assumptions:
    - never get empty inner array
    - all array values are valid integers
    - first array is of depth one
    - the array can only contain integers and arrays

# Inputs: array of integers
# Output: integer
# Need to figure out:
    - how to handle nested arrays


## First Approach: 
- have productSum(array, depth=1) function that:
    - will take in the array and
    - will take in / have an initial depth value of one
- declare a total variable in the function
- iterate through each element of the array
    - if element is an int, add it to total
    - if array, calculate productSum on that array but increase the depth by one productSum(array, depth+1)
- return total * depth
# O(n) time - where n is the number of elements in all arrays
# O(d) space - where d is the depth of the deepest array

"""
