""" 
Fruits into Baskets:

Given an array of characters where each character represents a fruit tree,
 you are given two baskets, and your goal is to put maximum number of fruits in each basket. 
The only restriction is that each basket can have only one type of fruit.

You can start with any tree, but you can’t skip a tree once you have started. 
You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both baskets.

Example 1:
    Input: Fruit=['A', 'B', 'C', 'A', 'C']
    Output: 3
    Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
Example 2:
    Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
    Output: 5
    Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
        This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

https://www.educative.io/courses/grokking-the-coding-interview/Bn2KLlOR0lQ
"""
from collections import defaultdict
""" 
Solution:

- we need to find the longest subarray with a max of two distinct characters

- create a subarray with two distinct characters & once we have this,
    - check if lengthening the array will not break the 2 dist char rule, if so, increase the length otherwise,
    - decrease the subarray length by removing the first character in the subarray

['0', '1', '2', '3', '4', '5'] 6
['A', 'B', 'C', 'B', 'B', 'C']

left,right,store
l=0,r=0,{A:1,}
# increase size: we need to have a subarray with two distinct characters
l=0,r=1,{A:1,B:1}
# decrease size: we cannot increase, adding c will break the 2 dist characters rule
l=1,r=1,{B:1,}
# increase size
l=1,r=2,{B:1,C:1}
l=1,r=3,{B:2,C:1}
l=1,r=4,{B:3,C:1}
l=1,r=5,{B:3,C:2}

res = 3 # => {B:3,C:2}

"""

# from collections import defaultdict


def fruits_into_baskets(fruits):
    if not fruits or len(fruits) < 2:
        return -1

    most_fruits = float('-inf')

    left = right = 0
    store = defaultdict(int)
    store[fruits[0]] = 1
    while right < len(fruits):
        if len(store) < 2:
            right += 1
            if right < len(fruits) - 1:
                store[fruits[right]] += 1
            continue

        most_fruits = max(most_fruits, (right-left)+1)

        # can add one more
        if right < len(fruits) - 1 and fruits[right+1] in store:
            right += 1
            store[fruits[right]] += 1

        # can add: so remove one
        else:
            store[fruits[left]] -= 1
            if store[fruits[left]] <= 0:
                store.pop(fruits[left])
            left += 1

    if most_fruits == float('-inf'):
        return -1
    return most_fruits


print("Maximum number of fruits: " +
      str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
print("Maximum number of fruits: " +
      str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))
print("Maximum number of fruits: " +
      str(fruits_into_baskets(['A', ])))
