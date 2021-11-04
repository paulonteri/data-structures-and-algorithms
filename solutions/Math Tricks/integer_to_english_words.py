""" 
Integer to English Words

Convert a non-negative integer num to its English words representation.

Example 1:
    Input: num = 123
    Output: "One Hundred Twenty Three"
Example 2:
    Input: num = 12345
    Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:
    Input: num = 1234567
    Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:
    Input: num = 1234567891
    Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"

https://leetcode.com/problems/integer-to-english-words
"""


""" 
This problem is about the decomposition of the problem -- how do you break it down. Not about efficiency.

max => 2,147,483,647 ("Two Billion - One Hundred Forty Seven Million - Four Hundred Eighty Three Thousand - Six Hundred Forty Seven")


the `len_three` function and how it's used is what you should understand
"""


class Solution:

    def ones(self, num):
        store = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine'
        }
        return store[num]

    def tens_less_20(self, num):
        store = {
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen'
        }
        return store[num]

    def tens_greater_20(self, num):
        store = {
            2: 'Twenty',
            3: 'Thirty',
            4: 'Forty',
            5: 'Fifty',
            6: 'Sixty',
            7: 'Seventy',
            8: 'Eighty',
            9: 'Ninety'
        }
        return store[num]

    def len_two(self, num):
        if not num:
            return ''
        elif num < 10:
            return self.ones(num)
        elif num < 20:
            return self.tens_less_20(num)
        else:
            tenner = num // 10
            rest = num % 10

            if rest:
                return self.tens_greater_20(tenner) + ' ' + self.ones(rest)
            else:
                return self.tens_greater_20(tenner)

    def len_three(self, num):
        hundred = num // 100
        rest = num % 100

        if hundred and rest:
            return self.ones(hundred) + ' Hundred ' + self.len_two(rest)
        elif hundred and not rest:
            return self.ones(hundred) + ' Hundred'
        elif not hundred and rest:
            return self.len_two(rest)

    def numberToWords(self, num):

        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000

        if not num:
            return 'Zero'

        result = ''
        if billion:
            result = self.len_three(billion) + ' Billion'
        if million:
            result += ' ' if result else ''
            result += self.len_three(million) + ' Million'
        if thousand:
            result += ' ' if result else ''
            result += self.len_three(thousand) + ' Thousand'
        if rest:
            result += ' ' if result else ''
            result += self.len_three(rest)
        return result
