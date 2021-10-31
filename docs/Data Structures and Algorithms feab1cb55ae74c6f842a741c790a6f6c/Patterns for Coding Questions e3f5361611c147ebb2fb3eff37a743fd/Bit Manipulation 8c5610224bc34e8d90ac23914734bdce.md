# Bit Manipulation

# Introduction

[Coding Patterns: Bitwise XOR](https://emre.me/coding-patterns/bitwise-xor/)

[Bit Manipulation - InterviewBit](https://www.interviewbit.com/courses/programming/topics/bit-manipulation/)

[Basics of Bit Manipulation Tutorials & Notes | Basic Programming | HackerEarth](https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/tutorial/)

[Bit Manipulation Tricks](https://emre.me/computer-science/bit-manipulation-tricks/)

[Binary Computation and Bitwise Operators](https://emre.me/computer-science/binary-computation-and-bitwise-operators/)

[Binary | Tech Interview Handbook](https://techinterviewhandbook.org/algorithms/binary/)

### **Important properties of XOR to remember [#](https://www.educative.io/courses/grokking-the-coding-interview/RLPGq6Vx0YY#important-properties-of-xor-to-remember)[#](https://www.educative.io/courses/grokking-the-coding-interview/RLPGq6Vx0YY#Important-properties-of-XOR-to-remember-#)**

Following are some important properties of XOR to remember:

- Taking XOR of a number with itself returns 0, e.g.,
    - 1 ^ 1 = 0
    - 29 ^ 29 = 0
- Taking XOR of a number with 0 returns the same number, e.g.,
    - 1 ^ 0 = 1
    - 31 ^ 0 = 31
- XOR is Associative & Commutative, which means:
    - (a ^ b) ^ c = a ^ (b ^ c)
    - a ^ b = b ^ a
    

todo:

[Sum of Two Integers - LeetCode](https://leetcode.com/problems/sum-of-two-integers/)

## Simple problems

### Single Number

```python
""" 
Single Number:

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

https://leetcode.com/problems/single-number/
"""

""" 
4^4=0          -> cancel out each other
4^0=4
4^7^6^6^4^7=0  -> contains all the pairs
4^7^6^4^7=6    -> missing pair of 6

"""

class Solution:
    def singleNumber(self, nums):

        res = 0
        for num in nums:
            res ^= num
        return res
```

### Missing Number

```python
""" 
Missing Number:

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

Example 1:
    Input: nums = [3,0,1]
    Output: 2
    Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:
    Input: nums = [0,1]
    Output: 2
    Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:
    Input: nums = [9,6,4,2,3,5,7,0,1]
    Output: 8
    Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
Example 4:
    Input: nums = [0]
    Output: 1
    Explanation: n = 1 since there is 1 number, so all numbers are in the range [0,1]. 1 is the missing number in the range since it does not appear in nums.

https://leetcode.com/problems/missing-number/
"""

""" 
Sum formulae:

(sum of all possible numbers) - (sum of given number) = missing_number
"""

class Solution0:
    def missingNumber(self, nums):

        possible = sum(range(len(nums)+1))
        given = sum(nums)

        return possible - given

""" 
Bitwise XOR 
4^4=0          -> cancel out each other
4^0=4
4^7^6^6^4^7=0  -> contains all the pairs
4^7^6^4^7=6    -> missing pair of 6

- XOR all the possible numbers with the given numbers, 
    the result will be the missing as it won't have a partner to cancel it out

example: [3,0,1]
- > all possible: 0^1^2^3
- > given: 3^0^1
- > 0^1^2^3 ^ 3^0^1 = 2 (it won't be canceled out)
"""

class Solution:
    def missingNumber(self, nums):

        res = 0
        for i in range(1, len(nums)+1):
            res ^= i

        for num in nums:
            res ^= num

        return res
```