""" 
Robot Bounded In Circle:

On an infinite plane, a robot initially stands at (0, 0) and faces north. 
The robot can receive one of three instructions:
    "G": go straight 1 unit;
    "L": turn 90 degrees to the left;
    "R": turn 90 degrees to the right.
The robot performs the instructions given in order, and repeats them forever.
Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

Example 1:
    Input: instructions = "GGLLGG"
    Output: true
    Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
    When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
Example 2:
    Input: instructions = "GG"
    Output: false
    Explanation: The robot moves north indefinitely.
Example 3:
    Input: instructions = "GL"
    Output: true
    Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...

https://leetcode.com/problems/robot-bounded-in-circle
https://leetcode.com/problems/robot-bounded-in-circle/discuss/290856/JavaC%2B%2BPython-Let-Chopper-Help-Explain
"""
from enum import Enum
""" 
MOVING: 
- moving north is adding 1 to y
- moving left is adding 1 to x
- moving south is subreacting 1 from y
- moving left is subreacting 1 from x

DIRECTIONS:
    north
west    east
    south

SOLUTION:
- if we have a loop,
    because the turnings are of 90 degrees,
    we should return to 0,0 after running the instructions 4 times


if we are done with the instruction once and have changed direction by ((dir) cumulative direction which might be south, east, west)
it means that if this (dir) is applied at most 4 times (for east & west (horizontal)) or even 2 times (for north (vertical)) we will be back to the origin
"""


class Direction(Enum):
    NORTH = "north"
    SOUTH = "south"
    EAST = "east"
    WEST = "west"


class Solution:
    def isRobotBounded(self, instructions: str):
        position = [0, 0]
        direction = Direction.NORTH

        for _ in range(4):
            # run instructions
            for char in instructions:
                if char == "G":
                    self.move(position, direction)
                else:
                    direction = self.change_direction(direction, char)

            # check if back to start
            if position[0] == 0 and position[1] == 0:
                return True

        return False

    def move(self, position, direction):
        if direction == Direction.NORTH:
            position[1] = position[1]+1
        elif direction == Direction.SOUTH:
            position[1] = position[1]-1
        elif direction == Direction.EAST:
            position[0] = position[0]+1
        elif direction == Direction.WEST:
            position[0] = position[0]-1

    def change_direction(self, direction, change):
        if change == "L":
            if direction == Direction.NORTH:
                return Direction.WEST
            elif direction == Direction.SOUTH:
                return Direction.EAST
            elif direction == Direction.EAST:
                return Direction.NORTH
            elif direction == Direction.WEST:
                return Direction.SOUTH
        if change == "R":
            if direction == Direction.NORTH:
                return Direction.EAST
            elif direction == Direction.SOUTH:
                return Direction.WEST
            elif direction == Direction.EAST:
                return Direction.SOUTH
            elif direction == Direction.WEST:
                return Direction.NORTH


""" 
---------------------------------------------
"""


class Solution1:
    def isRobotBounded(self, instructions: str):
        position = [0, 0]
        direction = Direction.NORTH

        for char in instructions:
            if char == "G":
                self.move(position, direction)
            else:
                direction = self.change_direction(direction, char)

        # check if back to start
        if position[0] == 0 and position[1] == 0:
            return True
        # check if changed direction
        return direction != Direction.NORTH

    def move(self, position, direction):
        if direction == Direction.NORTH:
            position[1] = position[1]+1
        elif direction == Direction.SOUTH:
            position[1] = position[1]-1
        elif direction == Direction.EAST:
            position[0] = position[0]+1
        elif direction == Direction.WEST:
            position[0] = position[0]-1

    def change_direction(self, direction, change):
        if change == "L":
            if direction == Direction.NORTH:
                return Direction.WEST
            elif direction == Direction.SOUTH:
                return Direction.EAST
            elif direction == Direction.EAST:
                return Direction.NORTH
            elif direction == Direction.WEST:
                return Direction.SOUTH
        if change == "R":
            if direction == Direction.NORTH:
                return Direction.EAST
            elif direction == Direction.SOUTH:
                return Direction.WEST
            elif direction == Direction.EAST:
                return Direction.SOUTH
            elif direction == Direction.WEST:
                return Direction.NORTH


""" 
---------------------------------------------
"""


# same as above but using math tricks
class Solution2:
    def isRobotBounded(self, instructions: str):
        direction = (0, 1)
        start = [0, 0]

        for x in instructions:
            if x == 'G':
                start[0] += direction[0]
                start[1] += direction[1]
            elif x == 'L':
                direction = (-direction[1], direction[0])
            elif x == 'R':
                direction = (direction[1], -direction[0])

        # check if back to start or if changed direction
        return start == [0, 0] or direction != (0, 1)
