""" 
String Rotation:

Assume you have a method isSubstring which checks if one word is a substring of another. 
Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one call to isSubstring 
    (e.g.,"waterbottle" is a rotation of"erbottlewat").
"""


def is_substring(str, substring):
    return substring in str


def string_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    return is_substring(s1+s1, s2)


print(string_rotation("waterbottle", "erbottlewat") == True)
print(string_rotation("waterbottleq", "erbottlewat") == False)
print(string_rotation("waterbottleq", "erbottlewatq") == False)
print(string_rotation("CodingInterview", "erviewCodingInt") == True)
print(string_rotation("Test", "est") == False)
