"""
Sunset Views:

Given an array of buildings and a direction that all of the buildings face,
 return an array of the indices of the buildings that can see the sunset.
A building can see the sunset if it's strictly taller than all of the buildings that come after it in the direction that it faces.
The input array named buildings contains positive, non-zero integers representing the heights of the buildings.
A building at index i thus has a height denoted by buildings[i].
All of the buildings face the same direction, and this direction is either east or west,
 denoted by the input string named direction, which will always be equal to either "EAST" or "WEST".
In relation to the input array, you can interpret these directions as right for east and left for west.
Important note: the indices in the ouput array should be sorted in ascending order.

https://www.algoexpert.io/questions/Sunset%20Views
"""


# O(n) time | O(n) space - where n is the length of the input array
def sunsetViews(buildings, direction):

    can_see = []
    tallest_so_far = float('-inf')

    if direction == "EAST":
        for idx in reversed(range(len(buildings))):
            height = buildings[idx]
            if height > tallest_so_far:
                can_see.insert(0, idx)
                tallest_so_far = height
    else:
        for idx in range(len(buildings)):
            height = buildings[idx]
            if height > tallest_so_far:
                can_see.append(idx)
                tallest_so_far = height

    return can_see


# O(n) time | O(n) space
def sunsetViews1(buildings, direction):
    if not len(buildings):
        return []

    stack = []  # stores indexes of the tallest buildings

    if direction == "EAST":
        stack.append(0)
        for idx in range(1, len(buildings)):
            height = buildings[idx]
            while len(stack) > 0 and height >= buildings[stack[0]]:
                stack.pop(0)
            stack.insert(0, idx)

        stack.reverse()

    else:
        stack.append(len(buildings)-1)
        for idx in reversed(range(len(buildings)-1)):
            height = buildings[idx]
            while len(stack) > 0 and height >= buildings[stack[0]]:
                stack.pop(0)
            stack.insert(0, idx)

    return stack


def sunsetViews9(buildings, direction):
    can_see = []
    tallest_so_far = float('-inf')

    is_west = direction == "WEST"
    buildings_range = range(len(buildings)) if is_west else reversed(
        range(len(buildings)))

    for idx in buildings_range:
        height = buildings[idx]

        if height > tallest_so_far:
            can_see.append(idx)
            tallest_so_far = height

    if is_west:
        return can_see
    return sorted(can_see)


def sunsetViews10(buildings, direction):
    stack = []

    is_west = not direction == "WEST"
    buildings_range = range(len(buildings)) if is_west else reversed(
        range(len(buildings)))

    for idx in buildings_range:
        height = buildings[idx]

        if len(stack) == 0:
            stack.append(idx)
            continue

        # remove prev buildings that can be blocked by the current
        while len(stack) > 0 and height >= buildings[stack[-1]]:
            stack.pop()

        # we always add to the stack
        stack.append(idx)

    if is_west:
        return stack
    return sorted(stack)
