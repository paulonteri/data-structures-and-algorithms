"""
Climbing Stairs / Triple Step:

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
https://leetcode.com/problems/climbing-stairs/
"""


class Solution:
    def climbStairs(self, n):
        return self.helper(n)

    # in case we reach remaining=0, then we have found way (a correct set of steps)
    def helper(self, remaining, store={0: 1}):  # store={0:1} is a base case
        if remaining < 0:
            return 0

        if remaining in store:
            return store[remaining]

        total = self.helper(remaining-1, store) + \
            self.helper(remaining-2, store)

        store[remaining] = total

        return store[remaining]


"""
Staircase Traversal:
You're given two positive integers representing the height of a staircase and the maximum number of steps that you can advance up the staircase at a time.
Write a function that returns the number of ways in which you can climb the staircase.

For example, if you were given a staircase of height = 3 and maxSteps = 2 you could climb the staircase in 3 ways.
You could take 1 step, 1 step, then 1 step, you could also take 1 step, then 2 steps, and you could take 2 steps, then 1 step.

Note that maxSteps <= height will always be true.

Sample Input:
    height = 4
    maxSteps = 2
Sample Output:
    5
    // You can climb the staircase in the following ways: 
    // 1, 1, 1, 1
    // 1, 1, 2
    // 1, 2, 1
    // 2, 1, 1
    // 2, 2
    
https://www.algoexpert.io/questions/Staircase%20Traversal
"""


# 0(k^n) time, 0(n) space - where k is the max steps, n - number of steps
def staircaseTraversal00(height, maxSteps):
    return staircaseTraversalHelper00(height, maxSteps)


def staircaseTraversalHelper00(height_remaining, max_steps):

    if height_remaining == 0:
        # if are exactly at the last step, we have found a way
        return 1
    elif height_remaining < 0:
        # if we pass the last step, we made a mistake
        return 0

    ways = 0
    for step in range(1, max_steps+1):
        ways += staircaseTraversalHelper00(height_remaining - step, max_steps)

    return ways


# memoization:
# 0(k*n) time, 0(n) space - where k is the max steps, n - number of steps
# for each call, we'll have to sum k elements together
# for each of our n recursive calls, we have to do k work
def staircaseTraversal(height, maxSteps):
    return staircaseTraversalHelper(height, maxSteps, {0: 1})


def staircaseTraversalHelper(height_remaining, max_steps, store):

    if height_remaining < 0:
        # if we pass the last step, we made a mistake
        return 0

    # memoize
    if height_remaining in store:
        return store[height_remaining]

    ways = 0
    for step in range(1, max_steps+1):
        ways += staircaseTraversalHelper(height_remaining - step,
                                         max_steps, store)

    store[height_remaining] = ways  # memoize

    return store[height_remaining]


"""
ordering:

legend=> [step][remaining]

h=3 max_steps=2
			[][3]
	[1][2]			[2][1]
[1][1]	[2][0]      [1][0]
[1][0]

h=4 max_steps=3
			[][4]
	[1][3]	 			[2][2]				[3][1]
[1][2] [2][1] [3][0]	[1][1] [2][0]		[1][0]

h=0 max_steps=2 ways=1
h=1 max_steps=2 ways=1
h=2 max_steps=2 ways=2
h=3 max_steps=2 ways=3
h=4 max_steps=2 ways=5

we realise that:
ways(n) = ways(n-1) + (n-2) .... + (n-max-steps)

The number of ways to climb a staircase of height k with a max number of steps s is: 
numWays[k - 1] + numWays[k - 2] + ... + numWays[k - s]. 
This is because if you can advance between 1 and s steps, 
    then from each step k - 1, k - 2, ..., k - s, 
    you can directly advance to the top of a staircase of height k. 
By adding the number of ways to reach all steps that you can directly advance to the top step from, 
    you determine how many ways there are to reach the top step.
"""


# <---------------------------------------------------------------------------------------------------------->
# DP Solution
# we will run the loop n times each with k work
# O(k^n) time | O(n) space - where n is the height of the staircase and k is the number of allowed steps
def staircaseTraversal04(height, maxSteps):

    # the indices represent the heights & the values the no. of ways
    max_ways = [0] * (height + 1)
    # base cases
    max_ways[0] = 1
    max_ways[1] = 1

    # try all steps: start from maxSteps, maxSteps-1, ..., 2 & 1
    # ways(n) = ways(n-1) + (n-2) .... + (n-max-steps)
    for idx in range(2, height+1):
        ways = 0

        start_idx = max(idx-maxSteps, 0)  # prevent negatives
        for i in range(start_idx, idx):
            ways += max_ways[i]

        max_ways[idx] = ways

    return max_ways[-1]


# <---------------------------------------------------------------------------------------------------------->
# DP Solution improved
# we will run the loop n times each with k work
# O(n) time | O(n) space - where n is the height of the staircase and k is the number of allowed steps
def staircaseTraversal05(height, maxSteps):

    # the indices represent the heights & the values the no. of ways
    max_ways = [0] * (height + 1)
    # base cases
    max_ways[0] = 1
    max_ways[1] = 1

    # # try all steps: start from maxSteps, maxSteps-1, ..., 2 & 1
    # # ways(n) = ways(n-1) + (n-2) .... + (n-max-steps)

    # start with a window size of one
    window = max_ways[0]
    window_size = 1  # this cab be removed -> (idx == prev window_size)
    for idx in range(1, height+1):
        max_ways[idx] = window

        # manipulate window size
        window += max_ways[idx]
        if window_size == maxSteps:
            window -= max_ways[idx-maxSteps]
        else:
            window_size += 1

    return max_ways[-1]
