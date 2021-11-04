
"""
Integer to String
"""


def single_digit_to_char(digit):
    return chr(ord('0')+digit)


def int_to_string(x: int):
    if x == 0:
        return "0"

    is_neg = False
    if x < 0:
        is_neg, x = True, -x

    result = []
    while x > 0:
        digit = x % 10
        result.append(single_digit_to_char(digit))
        x = x // 10

    if is_neg:
        result.append('-')
    return "".join(reversed(result))


"""
String to Integer
"""


def single_char_to_int(character):
    # num_mapping = {
    #     "1": 1,
    #     "2": 2,
    #     "3": 3,
    #     "4": 4,
    #     "5": 5,
    #     "6": 6,
    #     "7": 7,
    #     "8": 8,
    #     "9": 9,
    #     "0": 0,
    # }
    # return num_mapping[character]
    return ord(character) - ord('0')


def string_to_int(s: str):
    is_neg = False
    num = 0
    multiplier = 1

    start_idx = 0
    if s and s[0] == "-":
        is_neg, start_idx = True, 1
    if s and s[0] == "+":
        start_idx = 1

    for idx in range(start_idx, len(s)):
        # for idx in range(start_idx, len(s)):
        num *= 10
        num += single_char_to_int(s[idx])  # *multiplier
        # multiplier *= 10

    if is_neg:
        return -num
    return num


print(string_to_int("22"), type(string_to_int("22")))
print(string_to_int("1001"))
print(string_to_int("210"))
print(string_to_int("012"))
print(string_to_int("23"))
print(string_to_int("-2"))
print(string_to_int("34567"))
print(string_to_int("343434"))
print(string_to_int("+7654345"))
