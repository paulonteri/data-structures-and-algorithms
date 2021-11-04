""" 
Combination Sum

Given an array of distinct integers candidates and a target integer target, 
    return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen numbers is different.
It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 
Example 1:
    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]
    Explanation:
        2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
        7 is a candidate, and 7 = 7.
        These are the only two combinations.
Example 2:
    Input: candidates = [2,3,5], target = 8
    Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:
    Input: candidates = [2], target = 1
    Output: []
Example 4:
    Input: candidates = [1], target = 1
    Output: [[1]]
Example 5:
    Input: candidates = [1], target = 2
    Output: [[1,1]]

https://leetcode.com/problems/combination-sum

Prerequisite:
- https://leetcode.com/problems/combination-sum-iii
"""


"""

candidates = [2,3,6,7], target = 7
                                                    7[]
                                              5[2]         4[3]
                                           3[2,2] 2[2,3]
                                          
                   []rem_target
           /          /     \     \
    [2]5            [3]4  [6]1  [7]0
 /       /    
[2,2]3   [2,3]2  
|        |
[2,2,3]0 [2,3,2]0

"""


class Solution(object):
    def combinationSum(self, candidates, target):
        return self.helper(candidates, 0, target)

    def helper(self, candidates, idx, target):
        # base cases
        if target == 0:
            return [[]]
        if target < 0 or idx >= len(candidates):
            return []
        result = []

        # add number
        # remember to give the current number another chance, rather than moving on (idx instead of idx+1)
        for arr in self.helper(candidates, idx, target-candidates[idx]):
            result.append(arr + [candidates[idx]])

        # skip number
        result += self.helper(candidates, idx+1, target)

        return result


""" 

"""


class Solution_:
    def combinationSum(self, candidates, target):

        results = []

        def backtrack(remain, comb, start):
            if remain == 0:
                results.append(list(comb))
                return
            elif remain < 0:
                return

            for i in range(start, len(candidates)):
                # add the number into the combination
                comb.append(candidates[i])

                # give the current number another chance, rather than moving on (i instead of i+1)
                backtrack(remain - candidates[i], comb, i)

                # backtrack, remove the number from the combination
                comb.pop()

        backtrack(target, [], 0)

        return results
