"""
Drone Flight Planner:

You’re an engineer at a disruptive drone delivery startup and your CTO asks you
 to come up with an efficient algorithm that calculates the minimum amount of energy required for the company’s drone to complete its flight.
You know that the drone burns 1 kWh (kilowatt-hour is an energy unit) for every mile it ascends, and it gains 1 kWh for every mile it descends.
Flying sideways neither burns nor adds any energy.
Given an array route of 3D points, implement a function calcDroneMinEnergy that computes and returns the minimal amount of energy the drone would need to complete its route.
Assume that the drone starts its flight at the first point in route. That is, no energy was expended to place the drone at the starting point.
For simplicity, every 3D point will be represented as an integer array whose length is 3. Also, the values at indexes 0, 1, and 2 represent the x, y and z coordinates in a 3D point, respectively.

Explain your solution and analyze its time and space complexities.

Example:
    input:  route =[[0,   2, 10],
                    [3,   5,  0],
                    [9,  20,  6],
                    [10, 12, 15],
                    [10, 10,  8]]

    output: 5 # less than 5 kWh and the drone would crash before the finish
            # line. More than `5` kWh and it’d end up with excess energy

"""


"""
Since the drone only expends/gains energy when it flies up and down, we can ignore the x and y coordinates and focus only on the altitude - the z coordinate.
We should come up with the initial energy amount needed to enable the flight. 
In other words, at any given point in route, the drone’s level of energy balance mustn’t go below zero. Otherwise, it’ll crash.

get the x and y coordinates out of the way. 
The z coordinate (i.e. the altitude) is the only coordinate that matters.

ensure we have the min fuel such that the drone never falls from the sky at any point in the flight
- track the lowets negative amount of fuel we will ever have
"""


# O(n) time | O(1) space
def calc_drone_min_energy(route):

    energy = 0
    min_energy = 0
    for idx in range(1, len(route)):

        energy += route[idx-1][-1] - route[idx][-1]
        min_energy = min(min_energy, energy)

    return abs(min_energy)


x = [[0,  2, 10],
     [3,  5,  0],
     [9, 20,  6],
     [10, 12, 15],
     [10, 10,  8]]
y = [[0,  2,  2],
     [3,  5, 38],
     [9, 20,  6],
     [10, 12, 15],
     [10, 10,  8]]

print(calc_drone_min_energy(x))
print(calc_drone_min_energy(y))
print(calc_drone_min_energy([[0, 1, 19]]))
