"""
String Compression/Run-Length Encoding:

Given an array of characters chars, compress it using the following algorithm:
Begin with an empty string s. For each group of consecutive repeating characters in chars:
    If the group's length is 1, append the character to s.
    Otherwise, append the character followed by the group's length.
    The compressed string s should not be returned separately, but instead be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.
After you are done modifying the input array, return the new length of the array.

Write a function that takes in a non-empty string and returns its run-length encoding.
From Wikipedia, "run-length encoding is a form of lossless data compression in which runs of data are stored as a single data value and count,
 rather than as the original run."
For this problem, a run of data is any sequence of consecutive, identical characters. So the run "AAA" would be run-length-encoded as "3A".
To make things more complicated, however, the input string can contain all sorts of special characters, including numbers.
And since encoded data must be decodable, this means that we can't naively run-length-encode long runs.
For example, the run "AAAAAAAAAAAA" (12 As), can't naively be encoded as "12A", since this string can be decoded as either "AAAAAAAAAAAA" or "1AA.
Thus, long runs (runs of 10 or more characters) should be encoded in a split fashion; the aforementioned run should be encoded as "9A3A".

https://www.algoexpert.io/questions/Run-Length%20Encoding
https://leetcode.com/problems/string-compression/
"""


# O(n) time | O(n) space - where n is the len of the string
def runLengthEncoding(string):
    encoded = []

    idx = 0
    while idx < len(string):

        count = 1
        while idx < len(string)-1 and string[idx] == string[idx+1]:
            count += 1
            idx += 1

        # add the count to output
        while count > 9:
            encoded.append('9')
            encoded.append(string[idx])
            count -= 9
        encoded.append(str(count))
        encoded.append(string[idx])

        idx += 1

    return "".join(encoded)


"""
Sample Input
    string = "AAAAAAAAAAAAABBCCCCDD"
    "zAAABBBB222"
Sample Output
    "9A4A2B4C2D"
    "1z3A4B32"

"AAAAAAAAAAAAABBCCCCDD"
count for a = 13
- we'll have to make it less than 10: 9 and 4


# Input: non-empty string that can contain special characters and numbers
# Output: encoded string

# # Approach: 
# have and output
# iterate through each character having a starting count of 1
# while the next character is similar to the current, we move to the next and count += 1
# encode the character
    - while the count > 10: add 9char to the output & count -= 9
    - add countchar to the output
# move to next new character and repeat the process

"""


"""
have an output array
Have a running_count var


Iterate through the string,
At each character:
- Check if the next char == curr
	- if it is, increment the running_count by one and move to the next
	- if not record the running_sum in the output array
	
"""


class Solution(object):

    def compress(self, chars):

        length = len(chars)

        # make it a bit faster
        if length < 2:
            return length

        # the start position of the contiguous group of characters we are currently reading.
        anchor = 0

        # position to Write Next
        # we start with 0 then increase it whenever we write to the array
        write = 0

        # we go through each caharcter till we fiand a pos where the next is not equal to it
        # then we check if it has appeared more than once using the anchor and r(read) pointers
        # 1. iterate till we find a diffrent char
        # 2. record the no. of times the current char was repeated
        for pos, char in enumerate(chars):

            # check if we have reached the end or a different char
            # check if we are end or the next char != the current
            if (pos + 1) == length or char != chars[pos+1]:
                chars[write] = char
                write += 1

                # check if char has been repeated
                # have been duplicated if the read pointer is ahead of the anchor pointer
                if pos > anchor:
                    # check no. of times char has been repeated
                    repeated_times = pos - anchor + 1

                    # write the number
                    for num in str(repeated_times):
                        chars[write] = num
                        write += 1

                # move the anchor to the next char in the iteration
                anchor = pos + 1

        return write


"""
Example 1:
    Input: chars = ["a","a","b","b","c","c","c"]
    Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
    Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

Example 2:
    Input: chars = ["a"]
    Output: Return 1, and the first character of the input array should be: ["a"]
    Explanation: The only group is "a", which remains uncompressed since it's a single character.

Example 3:
    Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
    Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
"""
