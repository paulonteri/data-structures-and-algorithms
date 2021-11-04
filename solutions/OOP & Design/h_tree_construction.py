"""
H-Tree Construction:

An H-tree is a geometric shape that consists of a repeating pattern resembles the letter “H”.
It can be constructed by starting with a line segment of arbitrary length, drawing
two segments of the same length at right angles to the first through its endpoints,
and continuing in the same vein, reducing (dividing) the length of the line segments
drawn at each stage by √2.

Here are some examples of H-trees at different levels of depth:
https://www.pramp.com/challenge/EmYgnOgVd4IElnjAnQqn

Write a function drawHTree that constructs an H-tree, given its center (x and y
coordinates), a starting length, and depth. Assume that the starting line is
parallel to the X-axis.

Use the function drawLine provided to implement your algorithm. In a production
code, a drawLine function would render a real line between two points. However,
this is not a real production environment, so to make things easier, implement
drawLine such that it simply prints its arguments (the print format is left to
your discretion).

Analyze the time and space complexity of your algorithm. In your analysis, assume
that drawLine's time and space complexities are constant, i.e. O(1).

Constraints:
    [time limit] 5000ms
    [input] double x
    [input] double y
    [input] double length
    [input] double depth
    0 ≤ depth ≤ 10

https://www.pramp.com/challenge/EmYgnOgVd4IElnjAnQqn
"""


import math


def drawLine(x1, y1, x2, y2): pass


def drawHTree(x, y, length, depth):
    if depth == 0:
        return

    x0 = x - length/2
    x1 = x + length/2
    y0 = y - length/2
    y1 = y + length/2

    drawLine(x0, y0, x0, y1)
    drawLine(x1, y0, x1, y1)
    drawLine(x0, y, x1, y)

    new_length = length/math.sqrt(2)

    drawHTree(x0, y0, new_length, depth-1)
    drawHTree(x0, y1, new_length, depth-1)
    drawHTree(x1, y0, new_length, depth-1)
    drawHTree(x1, y1, new_length, depth-1)


'''
Time Complexity: every call of drawHTree invokes 9 expressions whose time complexity
is O(1) and 4 calls of drawHTree until depth (denoted here as D) reaches to 0.
Therefore: T(D) = 9 + 4 * T(D-1), where T is the time complexity function and D
is the depth of the H-Tree. Now, if we expand T(D-1) recursively all the way to
T(0), it’ll be easy to see that T(D) = O(4^D).
Space Complexity: recursive calls add overhead since we store them in the execution
stack. The space occupied in the stack will be then O(D), in the worst case scenario.
The stack space occupied will be no more than O(D) at any given point since a sibling
drawHTree will not be called before the current one being executed returns (i.e.
finishes its execution).
'''
