"""
Letter Case Permutation/String Permutations by changing case:

Given a string s, we can transform every letter individually to be lowercase or uppercase to create another string.
Return a list of all possible strings we could create. You can return the output in any order. 

Example 1:
    Input: s = "a1b2"
    Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:
    Input: s = "3z4"
    Output: ["3z4","3Z4"]
Example 3:
    Input: s = "12345"
    Output: ["12345"]
Example 4:
    Input: s = "0"
    Output: ["0"]

https://leetcode.com/problems/letter-case-permutation/
"""

""" 
Brute force:

- result = []
- have a perm(s,idx,curr_perm) helper function
    - for the character at idx:
        perm(s, idx+1, curr_perm+[character])
        - if is not a number:
            perm(s, idx+1, curr_perm+[character.swapcase()])
    - once we reach idx == len(s):
        - result.append(curr_perm)

---

Optimal:

- result = []
- arr = list(s)
- have a perm(arr,idx) helper function
    - for the character at idx:
            perm(arr,idx+1)
            - if is not a number:
                arr[idx] = arr[idx].swapcase()
                perm(arr,idx+1)
                arr[idx] = arr[idx].swapcase()
    - once we reach idx == len(s):
        - result.append(arr[:])


https://leetcode.com/problems/letter-case-permutation/discuss/379928/Python-clear-solution
"""


class Solution:
    def letterCasePermutationHelper(self, result, arr, idx):
        if idx == len(arr):
            result.append("".join(arr))
            return

        # case 1: do nothing
        self.letterCasePermutationHelper(result, arr, idx+1)

        # case 2: change case
        if arr[idx].isalpha():
            arr[idx] = arr[idx].swapcase()
            self.letterCasePermutationHelper(result, arr, idx+1)
            arr[idx] = arr[idx].swapcase()

    def letterCasePermutation(self, s):
        result = []
        if len(s) < 1:
            return result

        self.letterCasePermutationHelper(result, list(s), 0)
        return result
