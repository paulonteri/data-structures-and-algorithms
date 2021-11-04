""" 
Recursive multiply
"""


def recursive_multiply(x, y):
    # reduce number of recursive calls - ensure y is smaller
    if y > x:
        return recursive_multiply(y, x)

    return recursive_multiply_helper(x, y)


def recursive_multiply_helper(x, y):
    if y == 0:
        return 0
    if y == 1:
        return x

    return x + recursive_multiply_helper(x, y-1)


print(recursive_multiply(5, 4))
print(recursive_multiply(7, 3))
print(recursive_multiply(2, 2))
