""" 
Tower of Hanoi

https://youtu.be/rf6uf3jNjbo
https://runestone.academy/runestone/books/published/pythonds/Recursion/TowerofHanoi.html
https://leetcode.com/discuss/general-discussion/1517167/Tower-of-Hanoi-Algorithm-%2B-Python-code
https://www.notion.so/paulonteri/Recursion-DP-Backtracking-525dddcdd0874ed98372518724fc8753#0fa86da6418247199688a4f435447d86
"""


""" 
Here is a high-level outline of how to move a tower from the starting pole, to the goal pole, using an intermediate pole:
    1. Move a tower of height-1 to an intermediate pole
    2. Move the last/remaining disk to the final pole.
    3. Move the disks height-1 to the first rod and repeat the above steps.
        Move the tower of height-1 from the intermediate pole to the final pole using the original pole.

As long as we always obey the rule that the larger disks remain on the bottom of the stack, 
    we can use the three steps above recursively, 
    treating any larger disks as though they were not even there.

The only thing missing from the outline above is the identification of a base case. 
The simplest Tower of Hanoi problem is a tower of one disk. 
In this case, we need move only a single disk to its final destination. 
A tower of one disk will be our base case. 
"""


def tower_of_hanoi(n, from_rod="A", to_rod="C", aux_rod="B"):
    if n == 1:
        # The simplest Tower of Hanoi problem is a tower of one disk.
        # In this case, we need move only a single disk to its final destination.
        print("Move disk 1 from rod", from_rod, "to rod", to_rod)
        return

    # Move a tower of height-1 to an intermediate pole
    tower_of_hanoi(n-1, from_rod, aux_rod, to_rod)

    # Move the last/remaining disk to the final pole
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)

    # Move the disks height-1 to the first rod and repeat the above steps
    # Move the tower of height-1 from the intermediate pole to the final pole using the original pole.
    tower_of_hanoi(n-1, aux_rod, to_rod, from_rod)


tower_of_hanoi(1)
print("____________")
tower_of_hanoi(2)
print("____________")
tower_of_hanoi(3)
print("____________")
tower_of_hanoi(4)
print("____________")
tower_of_hanoi(5)
