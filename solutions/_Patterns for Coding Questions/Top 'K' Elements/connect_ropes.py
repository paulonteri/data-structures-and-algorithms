""" 
Connect Ropes;

Example 1:
    Input: [1, 3, 11, 5]
    Output: 33
    Explanation: First connect 1+3(=4), then 4+5(=9), and then 9+11(=20). So the total cost is 33 (4+9+20)
Example 2:
    Input: [3, 4, 5, 6]
    Output: 36
    Explanation: First connect 3+4(=7), then 5+6(=11), 7+11(=18). Total cost is 36 (7+11+18)
Example 3:
    Input: [1, 3, 11, 5, 2]
    Output: 42
    Explanation: First connect 1+2(=3), then 3+3(=6), 6+5(=11), 11+11(=22). Total cost is 42 (3+6+11+22)
"""

""" 
Solution:

In this problem, following a greedy approach to connect the smallest ropes first will ensure the lowest cost. 
We can use a Min Heap to find the smallest ropes following a similar approach as discussed in Kth Smallest Number. 
Once we connect two ropes, we need to insert the resultant rope back in the Min Heap so that we can connect it with the remaining ropes.
"""




import heapq
def minimum_cost_to_connect_ropes(ropeLengths):
    minHeap = []
    # add all ropes to the min heap
    for i in ropeLengths:
        heapq.heappush(minHeap, i)

    # go through the values of the heap, in each step take top (lowest) rope lengths from the min heap
    # connect them and push the result back to the min heap.
    # keep doing this until the heap is left with only one rope
    result = 0
    while len(minHeap) > 1:
        temp = heapq.heappop(minHeap) + heapq.heappop(minHeap)
        result += temp
        heapq.heappush(minHeap, temp)

    return result
