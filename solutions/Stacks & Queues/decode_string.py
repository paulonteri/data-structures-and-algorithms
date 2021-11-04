"""
Decode String

Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k.
For example, there won't be input like 3a or 2[4].

https://leetcode.com/problems/decode-string/
"""


# O(n) time | O(n) space
class Solution:
    def decodeString(self, s: str):

        if not s:
            return s

        # before we enter a bracket we store the current word in the prev_multiplier_stack,
        # so as to work on what is in the bracket only first, then
        #  we will restore it to ast it was after the closing bracket,
        #  and add the decoded content(decoded from in the brackets)
        prev_multiplier_stack = []  # add multipliers
        prev_str_stack = []

        current_str = ''

        i = 0
        while i < len(s):
            char = s[i]

            # handle multipliers
            if char.isnumeric():
                # can be one didgit or many:
                # Eg: '384[fsgs]asa'
                num = ''
                while s[i].isnumeric():
                    num += s[i]
                    i += 1
                # store it for easy retrieval
                prev_multiplier_stack.append(int(num))

            # open brackets
            elif char == "[":
                # # we prepare to deal with what is in the brackets first
                # store the current_str in the prev_str_stack
                # will be undone once we hit a closing bracket
                prev_str_stack.append(current_str)
                current_str = ''  # we will now only deal with stuff that is in the brackets []
                i += 1

            # close brackets
            elif char == "]":
                # # leave bracket finally
                # # decode then, return current_string as it was + decoded_chars
                # get the prev(most recently added) multiplier
                multiplier = prev_multiplier_stack.pop()
                # decode
                decoded_chars = current_str * multiplier
                # return current_string as it was, + decoded_chars
                current_str = prev_str_stack.pop() + decoded_chars
                i += 1
                #
                # ignore
                # # made this faster
                # while multiplier > 0:
                #     decoded_chars += current_str
                #     multiplier -= 1
                #
                # # made this faster again
                # decoded_chars = []
                # while multiplier > 0:
                #     decoded_chars.append(current_str)
                #     multiplier -= 1
                # return current_string as it was, + decoded_chars
                # current_str = prev_str_stack.pop() + "".join(decoded_chars)

            # other characters
            else:
                current_str += char
                i += 1

        return current_str


"""
Input:
    "3[a]2[bc]"
    "3[a2[c2[abc]3[cd]ef]]"
    "abc3[cd]xyz"
Output:
    "aaabcbc"
    "acabcabccdcdcdefcabcabccdcdcdefacabcabccdcdcdefcabcabccdcdcdefacabcabccdcdcdefcabcabccdcdcdef"
    "abccdcdcdxyz"
"""


class Solution00:
    def decodeString(self, s: str):
        res = ""

        multiplier_stack = []
        string_stack = []

        i = 0
        curr_string = ""
        while i < len(s):

            # handle numbers
            if s[i].isnumeric():
                curr_num = ""
                while s[i].isnumeric():
                    curr_num += s[i]
                    i += 1

                multiplier_stack.append(int(curr_num))
                continue

            # handle opening brackets
            elif s[i] == "[":
                # # go into bracket
                string_stack.append(curr_string)
                curr_string = ""

            # handle closing brackets
            elif s[i] == "]":
                # # get out of bracket
                # multiply
                prev_multiplier = multiplier_stack.pop()
                multiplied_string = curr_string * prev_multiplier
                # merge with outer bracket
                prev_string = string_stack.pop()
                curr_string = prev_string + multiplied_string

            # handle characters
            else:
                curr_string += s[i]

            i += 1

        return curr_string
