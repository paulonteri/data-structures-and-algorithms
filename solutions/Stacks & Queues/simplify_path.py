""" 
Simplify Path/Shorten Path:

Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system,
 convert it to the simplified canonical path.
In a Unix-style file system, 
    a period '.' refers to the current directory, 
    a double period '..' refers to the directory up a level, 
    and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. 
    For this problem, any other format of periods such as '...' are treated as file/directory names.
The canonical path should have the following format:
    The path starts with a single slash '/'.
    Any two directories are separated by a single slash '/'.
    The path does not end with a trailing '/'.
    The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
Return the simplified canonical path.

Example 1:
    Input: path = "/home/"
    Output: "/home"
    Explanation: Note that there is no trailing slash after the last directory name.
Example 2:
    Input: path = "/../"
    Output: "/"
    Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
Example 3:
    Input: path = "/home//foo/"
    Output: "/home/foo"
    Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
Example 4:
    Input: path = "/a/./b/../../c/"
    Output: "/c"

https://leetcode.com/problems/simplify-path/
https://www.algoexpert.io/questions/Shorten%20Path
"""


""" 
- have a stack and all all directories we find there
- if we find a '..', remove the directory at the top of the stack
- if we find a '//' or '.' skip it
"""


class Solution0:
    def simplifyPath(self, path):

        stack = []
        start = 0
        end = 0
        while start < len(path):
            # cannot add to stack
            if not (end == len(path)-1 or path[end] == "/"):
                end += 1
                continue

            # # check logic
            substring = path[start:end]
            if end == len(path)-1 and path[end] != "/":
                # deal with cases like "/home"
                substring = path[start:end+1]

            # # path creation logic
            # if we find a '//' or '.' skip it
            if substring == '' or substring == '.':
                pass
            # if we find a '..', remove the directory at the top of the stack
            elif substring == '..':
                if stack:
                    stack.pop()
            # add directory
            else:
                stack.append(substring)

            # # next
            start = end+1
            end = end+1

        return "/" + "/".join(stack)


class Solution:
    def simplifyPath(self, path):
        stack = []

        paths = path.split("/")
        for substring in paths:

            # # path creation logic
            # if we find a '//' or '.' skip it
            if substring == '' or substring == '.':
                pass
            # if we find a '..', remove the directory at the top of the stack
            elif substring == '..':
                if stack:
                    stack.pop()
            # add directory
            else:
                stack.append(substring)

        return "/" + "/".join(stack)


""" 
Algoexpert
"""


def shortenPath(path):

    stack = []
    past_relative_arr = []
    is_relative = path[0] != "/"

    paths = path.split("/")
    for substring in paths:

        # # path creation logic
        # if we find a '//' or '.' skip it
        if substring == '' or substring == '.':
            pass
        # if we find a '..', remove the directory at the top of the stack
        elif substring == '..':
            if stack:
                stack.pop()
            elif is_relative:
                past_relative_arr.append(substring)

        # add directory
        else:
            stack.append(substring)

    if is_relative:
        if past_relative_arr and stack:
            return "/".join(past_relative_arr) + "/" + "/".join(stack)
        elif stack:
            return "/".join(stack)
        else:
            return "/".join(past_relative_arr)

    return "/" + "/".join(stack)
