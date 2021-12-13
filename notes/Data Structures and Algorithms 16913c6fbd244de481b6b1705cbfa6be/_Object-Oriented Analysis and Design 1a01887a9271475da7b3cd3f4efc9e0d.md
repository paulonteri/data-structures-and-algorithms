# _Object-Oriented Analysis and Design

[GitHub - knightsj/object-oriented-design: 面向对象设计的设计原则和设计模式](https://github.com/knightsj/object-oriented-design)

[Python Design Patterns](https://python-patterns.guide/)

[Python Object Oriented Programming](https://www.programiz.com/python-programming/object-oriented-programming)

[How to Ace Object-Oriented Design Interviews](https://thinksoftware.medium.com/how-to-ace-object-oriented-design-interviews-4f9a667e0780)

[GitHub - tssovi/grokking-the-object-oriented-design-interview](https://github.com/tssovi/grokking-the-object-oriented-design-interview)

[Grokking the Object Oriented Design Interview - Learn Interactively](https://www.educative.io/courses/grokking-the-object-oriented-design-interview)

[One Stop OOP Guide | Useful and Short topics for interviews | Object Oriented Programming (C++) - LeetCode Discuss](https://leetcode.com/discuss/study-guide/1389824/One-Stop-OOP-Guide-or-Useful-and-Short-topics-for-interviews-or-Object-Oriented-Programming-(C%2B%2B))

# Introduction

## Examples

[GitHub - tuvo1106/ctci_6th_edition: Practice problems and solutions for Cracking the Coding Interview](https://github.com/tuvo1106/ctci_6th_edition)

[GitHub - w-hat/ctci-solutions: Python solutions to Cracking the Coding Interview (6th edition)](https://github.com/w-hat/ctci-solutions)

use botom up design - design smallest components to the largest

### Simple Examples

- Design Underground System
    
    ```python
    """
    Design Underground System:
    
    Implement the class UndergroundSystem that supports three methods:
        1. checkIn(int id, string stationName, int t)
            A customer with id card equal to id, gets in the station stationName at time t.
            A customer can only be checked into one place at a time.
        2. checkOut(int id, string stationName, int t)
            A customer with id card equal to id, gets out from the station stationName at time t.
        3. getAverageTime(string startStation, string endStation) 
            Returns the average time to travel between the startStation and the endStation.
            The average time is computed from all the previous traveling from startStation to endStation that happened
            directly.
            Call to getAverageTime is always valid.
    You can assume all calls to checkIn and checkOut methods are consistent. 
    That is, if a customer gets in at time t1 at some station, then it gets out at time t2 with t2 > t1. 
    All events happen in chronological order.
    
    https://leetcode.com/problems/design-underground-system
    """
    
    class CustomerCheckIn:
        def __init__(self, station_name, time):
            self.station_name = station_name
            self.time = time
    
    class RouteHistory:
        def __init__(self):
            self.total_time = 0
            self.trips = 0
    
        def add_trip_time(self, time):
            self.total_time += time
            self.trips += 1
    
        def get_avg_time(self):
            return self.total_time / self.trips
    
    class UndergroundSystem:
    
        def __init__(self):
            self.check_ins = {}
            self.route_histories = {}
    
        def checkIn(self, id: int, stationName: str, t: int):
            self.check_ins[id] = CustomerCheckIn(stationName, t)
    
        def checkOut(self, id: int, stationName: str, t: int):
            check_in = self.check_ins[id]
            self.check_ins.pop(id)
    
            route = (check_in.station_name, stationName)
    
            if route not in self.route_histories:
                self.route_histories[route] = RouteHistory()
    
            self.route_histories[route].add_trip_time(t-check_in.time)
    
        def getAverageTime(self, startStation: str, endStation: str):
            route = (startStation, endStation)
            return self.route_histories[route].get_avg_time()
    
    # Your UndergroundSystem object will be instantiated and called as such:
    # obj = UndergroundSystem()
    # obj.checkIn(id,stationName,t)
    # obj.checkOut(id,stationName,t)
    # param_3 = obj.getAverageTime(startStation,endStation)
    """ 
    
    """
    
    class UndergroundSystem_:
    
        def __init__(self):
            self.checkin_details = {}
            self.route_total_time = {}
    
        def checkIn(self, id: int, stationName: str, t: int) -> None:
            # save journey start details for each passenger
            # save cutomer checkin details
            self.checkin_details[id] = {
                "station": stationName,
                "time": t
            }
    
        def checkOut(self, id: int, stationName: str, t: int) -> None:
            checkin = self.checkin_details[id]
            # time taken = end time - start time
            time_taken = t - checkin["time"]
    
            # path = start station + end station
            path = checkin["station"] + stationName
    
            # increase total time and count
            if path in self.route_total_time:
                prev_total = self.route_total_time[path]
    
                self.route_total_time[path] = {
                    "total": prev_total["total"] + time_taken,
                    "count": prev_total["count"] + 1
                }
    
            # create entry in route_total_time: record total time and the count as 1
            else:
                self.route_total_time[path] = {
                    "total": time_taken,
                    "count": 1
                }
    
            # end customer journey
            self.checkin_details.pop(id)
    
        def getAverageTime(self, startStation: str, endStation: str) -> float:
            path = startStation + endStation
            # calculate average
            return self.route_total_time[path]["total"] / self.route_total_time[path]["count"]
    
    """
    Input:
        ["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime",
        "getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
        [[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],
        ["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],
        ["Leyton","Waterloo"]]
    Output:
        [null,null,null,null,null,null,null,14.00000,11.00000,null,11.00000,null,12.00000]
    """
    ```
    
- Design an Ordered Stream
    
    [Screen Recording 2021-11-13 at 20.38.32.mov](_Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Screen_Recording_2021-11-13_at_20.38.32.mov)
    
    ```python
    """ 
    1656. Design an Ordered Stream
    
    There is a stream of n (idKey, value) pairs arriving in an arbitrary order, where idKey is an integer between 1 and n and value is a string. 
    No two pairs have the same id.
    Design a stream that returns the values in increasing order of their IDs by returning a chunk (list) of values after each insertion. 
    The concatenation of all the chunks should result in a list of the sorted values.
    Implement the OrderedStream class:
        OrderedStream(int n) Constructs the stream to take n values.
        String[] insert(int idKey, String value) Inserts the pair (idKey, value) into the stream, then returns the largest possible chunk of currently inserted values that appear next in the order.
     
    
    Example:
        Input
            ["OrderedStream", "insert",     "insert",     "insert",      "insert",     "insert"]
            [[5],             [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"],  [5, "eeeee"], [4, "ddddd"]]
        Output
            [null,            [],           ["aaaaa"],    ["bbbbb", "ccccc"], [],      ["ddddd", "eeeee"]
        Explanation
            // Note that the values ordered by ID is ["aaaaa", "bbbbb", "ccccc", "ddddd", "eeeee"].
            OrderedStream os = new OrderedStream(5);
            os.insert(3, "ccccc"); // Inserts (3, "ccccc"), returns [].
            os.insert(1, "aaaaa"); // Inserts (1, "aaaaa"), returns ["aaaaa"].
            os.insert(2, "bbbbb"); // Inserts (2, "bbbbb"), returns ["bbbbb", "ccccc"].
            os.insert(5, "eeeee"); // Inserts (5, "eeeee"), returns [].
            os.insert(4, "ddddd"); // Inserts (4, "ddddd"), returns ["ddddd", "eeeee"].
            // Concatentating all the chunks returned:
            // [] + ["aaaaa"] + ["bbbbb", "ccccc"] + [] + ["ddddd", "eeeee"] = ["aaaaa", "bbbbb", "ccccc", "ddddd", "eeeee"]
            // The resulting order is the same as the order above.
            
    
    Constraints:
        1 <= n <= 1000
        1 <= id <= n
        value.length == 5
        value consists only of lowercase letters.
        Each call to insert will have a unique id.
        Exactly n calls will be made to insert.
        
    https://leetcode.com/problems/design-an-ordered-stream
    """
    
    """ 
    ["init", "insert",   "insert",     "insert",     "insert",     "insert"]
    [[5],  [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]
    Output
    [null,           [], ["aaaaa"],     ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]]
    
    """
    
    class OrderedStream:
    
        def __init__(self, n: int):
            self.store = [None] * (n+1)
            self.pointer = 1
    
        def insert(self, idKey: int, value: str):
            self.store[idKey] = value
    
            pointer_start = self.pointer
            while self.pointer < len(self.store) and self.store[self.pointer] is not None:
                self.pointer += 1
    
            if pointer_start != self.pointer:
                return self.store[pointer_start:self.pointer]
            return []
    
    # Your OrderedStream object will be instantiated and called as such:
    # obj = OrderedStream(n)
    # param_1 = obj.insert(idKey,value)
    ```
    
    Thought it was related to this:
    
- Count Unhappy Friends
    
    ```python
    """ 
    1583. Count Unhappy Friends
    
    You are given a list of preferences for n friends, where n is always even.
    For each person i, preferences[i] contains a list of friends sorted in the order of preference. 
    In other words, a friend earlier in the list is more preferred than a friend later in the list. Friends in each list are denoted by integers from 0 to n-1.
    All the friends are divided into pairs. The pairings are given in a list pairs, where pairs[i] = [xi, yi] denotes xi is paired with yi and yi is paired with xi.
    However, this pairing may cause some of the friends to be unhappy. A friend x is unhappy if x is paired with y and there exists a friend u who is paired with v but:
        x prefers u over y, and
        u prefers x over v.
    Return the number of unhappy friends.
    
    Example 1:
        Input: n = 4, preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], pairs = [[0, 1], [2, 3]]
        Output: 2
        Explanation:
            Friend 1 is unhappy because:
            - 1 is paired with 0 but prefers 3 over 0, and
            - 3 prefers 1 over 2.
            Friend 3 is unhappy because:
            - 3 is paired with 2 but prefers 1 over 2, and
            - 1 prefers 3 over 0.
            Friends 0 and 2 are happy.
    Example 2:
        Input: n = 2, preferences = [[1], [0]], pairs = [[1, 0]]
        Output: 0
        Explanation: Both friends 0 and 1 are happy.
    Example 3:
        Input: n = 4, preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], pairs = [[1, 3], [0, 2]]
        Output: 4
     
    
    Constraints:
        2 <= n <= 500
        n is even.
        preferences.length == n
        preferences[i].length == n - 1
        0 <= preferences[i][j] <= n - 1
        preferences[i] does not contain i.
        All values in preferences[i] are unique.
        pairs.length == n/2
        pairs[i].length == 2
        xi != yi
        0 <= xi, yi <= n - 1
        Each person is contained in exactly one pair.
        
    https://leetcode.com/problems/count-unhappy-friends
    """
    
    """ 
    n - even
    [
    0 [1, 3, 2], u
    1 [2, 3, 0],
    2 [1, 3, 0],
    3 [0, 2, 1]
    ], 
     
    pairs = [[1, 3], [0, 2]]
    
    { 
    1:3,
    3:1,
    0:2,
    2:0
    }
    
    # x unhappy
    x -> y
    u -> v
    
    # if there exists such a condition
    x -> u (x prefers u than what it currently has)
    u -> x (prefers x than what it has)
    
    - count = 0
    - store the preferences in a dict/list:
        { 
        x1: { u1: pref_u1, u2: pref_u2 }
        x2: { u1: pref_u1, u2: pref_u2 }
        }
    - store the friendships in a dict/list:
        {
        x1:u1,
        u1:x1
        }
    - for each x in the pairings:
        - if not with the highest priority friend
            - if can_get_higher_prio(x):
                count += 1
    
                
    can_get_higher_prio(x):
        - check if for all the higher priority friends u1, u2, u2
            - any of them is matched with a friend they prefer less than x 
    
    https://www.notion.so/paulonteri/_Object-Oriented-Analysis-and-Design-1a01887a9271475da7b3cd3f4efc9e0d#3b876eef896b482ea279ebdfbd918590
    """
    
    from typing import List
    class Solution:
        def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]):
            count = 0
    
            pref_lookup = [{} for _ in range(n)]
            friendships_lookup = [-1 for _ in range(n)]
    
            # store the preferences in a dict
            for person, preferences_list in enumerate(preferences):
                for priority, other_person in enumerate(preferences_list):
                    pref_lookup[person][other_person] = priority
            # store the friendships in a dict
            for x, y in pairs:
                friendships_lookup[x] = y
                friendships_lookup[y] = x
    
            for person, paired_with in enumerate(friendships_lookup):
                if pref_lookup[person][paired_with] == 0:
                    continue
                if self.can_get_higher_prio(pref_lookup, friendships_lookup, person, paired_with):
                    count += 1
    
            return count
    
        def can_get_higher_prio(self, pref_lookup, friendships_lookup, person, paired_with):
            """ 
            - check if for all the higher priority friends u1, u2, u2 of person
                - if any of them is matched with a friend they prefer less than x:
                    - return True
            - return False
            """
    
            for other_friend in pref_lookup[person]:
                # other_friend is of a lower priority
                if pref_lookup[person][other_friend] > pref_lookup[person][paired_with]:
                    continue
                # person is not under other_friend's priorities
                if person not in pref_lookup[other_friend]:
                    continue
    
                # check other_friend's preference with person vs preference with who they were paired with
                pref_w_person = pref_lookup[other_friend][person]
                pref_w_paired_with = pref_lookup[other_friend][friendships_lookup[other_friend]]
    
                if pref_w_paired_with > pref_w_person:
                    return True
    
            return False
    ```
    

- LRU Cache
    
    [LRU Cache - Twitch Interview Question - Leetcode 146](https://youtu.be/7ABFKPK2hD4)
    
    ![Screenshot 2021-10-23 at 13.23.26.png](_Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Screenshot_2021-10-23_at_13.23.26.png)
    
    ```python
    from collections import OrderedDict
    class LRUCache(OrderedDict):
    
        def __init__(self, capacity):
            """
            :type capacity: int
            """
            self.capacity = capacity
    
        def get(self, key):
            """
            :type key: int
            :rtype: int
            """
            if key not in self:
                return - 1
            
            self.move_to_end(key)
            return self[key]
    
        def put(self, key, value):
            """
            :type key: int
            :type value: int
            :rtype: void
            """
            if key in self:
                self.move_to_end(key)
            self[key] = value
            if len(self) > self.capacity:
                self.popitem(last = False)
    
    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)
    ```
    
    ![Screenshot 2021-10-23 at 13.25.16.png](_Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Screenshot_2021-10-23_at_13.25.16.png)
    
    ![Screenshot 2021-11-09 at 06.27.01.png](_Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Screenshot_2021-11-09_at_06.27.01.png)
    
    ```python
    """
    LRU Cache: Leecode 146
    
    Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
    Implement the LRUCache class:
        LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
        int get(int key) Return the value of the key if the key exists, otherwise return -1.
        void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
    
    Follow up:
    Could you do get and put in O(1) time complexity?
    
    https://leetcode.com/problems/lru-cache
    """
    
    from collections import OrderedDict
    from typing import Dict
    
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None
            self.prev = None
    
    # special Doubly Linked List
    class DLL:
        # head & tail will help in easily finding the beginning and end
        def __init__(self, head: Node, tail: Node):
            head.next = tail
            tail.prev = head
            self.head = head
            self.tail = tail
    
        def remove_between_head_and_tail(self, node: Node):
            # special remove function for our cache
            pr = node.prev
            nxt = node.next
            pr.next = nxt
            nxt.prev = pr
    
        def add_after_head(self, node: Node):
            after_head = self.head.next
    
            # update head
            self.head.next = node
            # update node that was after head
            after_head.prev = node
            # node
            node.next = after_head
            node.prev = self.head
    
        # ignore this
        # it is used for testing only
        def print_all(self):
            curr = self.head
            elements = []
    
            while curr is not None:
                pr = None
                nxt = None
    
                if curr.prev:
                    pr = curr.prev
                if curr.next:
                    nxt = curr.next
                elements.append([curr.key, curr.value, {"prev": pr, "next": nxt}])
    
            print(elements)
            return elements
    
    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)
    
    # SOLUTION:
    # get O(1) time | put O(1)
    class LRUCache:
    
        def __init__(self, capacity: int):
            self.capacity = capacity
            self.count = 0
            # used to store all the key value pairs
            self.store: Dict[int, Node] = {}
            # actual cache
            self.cache = DLL(Node(-1, -1), Node(-1, -1))
    
        def get(self, key: int):
            if not key in self.store:
                return -1
            else:
                node = self.store[key]
                # move to front (make most recent)
                self.cache.remove_between_head_and_tail(node)
                self.cache.add_after_head(node)
                return node.value
    
        def put(self, key: int, value: int):
            # have key in store
            if key in self.store:
                node = self.store[key]
                # update
                node.value = value
                # move to front (make most recent)
                self.cache.remove_between_head_and_tail(node)
                self.cache.add_after_head(node)
            # new key
            else:
                # create
                node = Node(key, value)
                self.store[key] = node
                self.cache.add_after_head(node)
                self.count += 1
    
            # check for excess
            if self.count > self.capacity:
                before_last = self.cache.tail.prev
                self.cache.remove_between_head_and_tail(before_last)
                self.store.pop(before_last.key)
                self.count -= 1
    
    """
    Input:
        ["LRUCache","put","put","put","put","get","get"]
        [[2],       [2,1],[1,1],[2,3],[4,1],[1],   [2]]
    
        ["LRUCache","put","put","get","put","get","put","get","get","get"]
        [[2],      [1,10],[2,20],[1], [3,30],[2], [4,40],[1],  [3],[4]]
    Output:
        [null,null,null,null,null,-1,3]
    
        [null,null,null,10,null,-1,null,-1,30,40]
    """
    
    """ 
    Ordered dictionary
    ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    """
    
    class LRUCache2(OrderedDict):
    
        def __init__(self, capacity):
            """
            :type capacity: int
            """
            self.capacity = capacity
    
        def get(self, key):
            """
            :type key: int
            :rtype: int
            """
            if key not in self:
                return - 1
    
            self.move_to_end(key)
            return self[key]
    
        def put(self, key, value):
            """
            :type key: int
            :type value: int
            :rtype: void
            """
            if key in self:
                self.move_to_end(key)
            self[key] = value
            if len(self) > self.capacity:
                self.popitem(last=False)
    
    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)
    ```
    

- Range Sum Query - Immutable
    
    ```python
    """
    Range Sum Query - Immutable
    
    Given an integer array nums, handle multiple queries of the following type:
    Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
    Implement the NumArray class:
        NumArray(int[] nums) Initializes the object with the integer array nums.
        int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
     
    
    Example 1:
        Input
            ["NumArray", "sumRange", "sumRange", "sumRange"]
            [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
        Output
            [null, 1, -1, -3]
        Explanation
            NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
            numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
            numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
            numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
    
    https://leetcode.com/problems/range-sum-query-immutable
    """
    
    class NumArray:
        """ 
        Pre-compute the cumulative sums to give O(1) lookup
        """
    
        def __init__(self, nums):
            self.cumulative_sums = [0]*len(nums)
    
            running_sum = 0
            for idx, num in enumerate(nums):
                running_sum += num
                self.cumulative_sums[idx] = running_sum
    
        def sumRange(self, left: int, right: int):
            left_val = 0
            if left > 0:
                left_val = self.cumulative_sums[left-1]
            return self.cumulative_sums[right] - left_val
    
    # Your NumArray object will be instantiated and called as such:
    # obj = NumArray(nums)
    # param_1 = obj.sumRange(left,right)
    ```
    
- Range Sum Query 2D - Immutable
    
    ![Screenshot 2021-10-24 at 07.34.42.png](_Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Screenshot_2021-10-24_at_07.34.42.png)
    
    ![Screenshot 2021-10-24 at 07.35.22.png](_Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Screenshot_2021-10-24_at_07.35.22.png)
    
    ![Screenshot 2021-10-24 at 07.35.43.png](_Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Screenshot_2021-10-24_at_07.35.43.png)
    
    ![Screenshot 2021-10-24 at 07.36.37.png](_Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Screenshot_2021-10-24_at_07.36.37.png)
    
    [Summed-area table - Wikipedia](https://en.wikipedia.org/wiki/Summed-area_table)
    
    [Computer Vision - The Integral Image](https://computersciencesource.wordpress.com/2010/09/03/computer-vision-the-integral-image/)
    
    ![Screenshot 2021-10-24 at 07.38.21.png](_Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Screenshot_2021-10-24_at_07.38.21.png)
    
    ![Screenshot 2021-10-24 at 07.38.34.png](_Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Screenshot_2021-10-24_at_07.38.34.png)
    
    ```python
    """ 
    Range Sum Query 2D - Immutable
    
    Given a 2D matrix matrix, handle multiple queries of the following type:
    Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
    Implement the NumMatrix class:
        NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
        int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
     
    
    Example 1:
        Input
            ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
            [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
        Output
            [null, 8, 11, 12]
        Explanation
            NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
            numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
            numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
            numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)
     
    
    Constraints:
        m == matrix.length
        n == matrix[i].length
        1 <= m, n <= 200
        -105 <= matrix[i][j] <= 105
        0 <= row1 <= row2 < m
        0 <= col1 <= col2 < n
        At most 104 calls will be made to sumRegion.
    
    https://leetcode.com/problems/range-sum-query-2d-immutable
        https://www.notion.so/paulonteri/Object-Oriented-Analysis-and-Design-1a01887a9271475da7b3cd3f4efc9e0d#4925b17f4f7142b88467b45d66602384
    """
    
    class NumMatrix:
        """ 
        Pre-compute the cumulative sums for each row to give O(R) lookup 
        where R in the number of rows requested
        """
    
        def __init__(self, matrix):
            self.row_sums = [
                [0 for _ in range(len(matrix[0]))]for _ in range(len(matrix))
            ]
    
            for row_idx in range(len(matrix)):
                running_sum = 0
                for col_idx, num in enumerate(matrix[row_idx]):
                    running_sum += num
                    self.row_sums[row_idx][col_idx] = running_sum
    
        def sumRegion(self, row1: int, col1: int, row2: int, col2: int):
            total = 0
    
            for row_idx in range(row1, row2+1):
                total += self._get_row_sum(self.row_sums[row_idx], col1, col2)
    
            return total
    
        def _get_row_sum(self, row, left, right):
            left_val = 0
            if left > 0:
                left_val = row[left-1]
            return row[right] - left_val
    
    # Your NumMatrix object will be instantiated and called as such:
    # obj = NumMatrix(matrix)
    # param_1 = obj.sumRegion(row1,col1,row2,col2)
    
    """ 
    
    """
    
    class NumMatrix2:
        """ 
        Here we use the technique of integral image, which is introduced to speed up block computation.
        https://www.notion.so/paulonteri/Object-Oriented-Analysis-and-Design-1a01887a9271475da7b3cd3f4efc9e0d#4925b17f4f7142b88467b45d66602384
        """
    
        def __init__(self, matrix):
    
            # build integral image by recurrence relationship
            self.integral_image = [
                [0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))
            ]
    
            for row in range(len(matrix)):
    
                running_sum = 0
                for col in range(len(matrix[0])):
                    running_sum += matrix[row][col]
                    self.integral_image[row][col] = running_sum
                    # add top row
                    if row > 0:
                        self.integral_image[row][col] += self.integral_image[row-1][col]
    
        def sumRegion(self, row1: int, col1: int, row2: int, col2: int):
    
            bottom_right = self.integral_image[row2][col2]
            #
            bottom_left = 0
            if col1 > 0:
                bottom_left = self.integral_image[row2][col1-1]
            #
            top_right = 0
            if row1 > 0:
                top_right = self.integral_image[row1-1][col2]
            #
            top_left = 0
            if col1 > 0 and row1 > 0:
                top_left = self.integral_image[row1 - 1][col1-1]
    
            # calculate area
            return bottom_right - bottom_left - top_right + top_left
    
    # Your NumMatrix object will be instantiated and called as such:
    # obj = NumMatrix(matrix)
    # param_1 = obj.sumRegion(row1,col1,row2,col2)
    ```
    

[Insert Delete GetRandom O(1) - LeetCode](https://leetcode.com/problems/insert-delete-getrandom-o1/)

- LFU Cache
    
    [LFU CACHE (Leetcode) - Code & Whiteboard](https://youtu.be/Jn4mbZVkeik)
    
    [Python concise solution **detailed** explanation: Two dict + Doubly linked list - LeetCode Discuss](https://leetcode.com/problems/lfu-cache/discuss/207673/Python-concise-solution-**detailed**-explanation%3A-Two-dict-%2B-Doubly-linked-list)
    
    [LFU Cache - LeetCode](https://leetcode.com/problems/lfu-cache/)
    

- Design Browser History *
    - Use a special `DLL` to manage the history.
    - Have a `current_page` pointer pointing to a node in the DLL
    - `back(steps):`
        - `self.current_page = self.current_page.prev` for the number of steps
    - `forward(steps):`
        - `self.current_page = self.current_page.nxt` for the number of steps
    - `visit(url):`
        - `self.history.remove_all_after_node(self.current_page)` <- clear forward history
        - `DLL.add_node(url)`
    
    ```python
    """ 
    1472. Design Browser History
    
    You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.
    Implement the BrowserHistory class:
        BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
        void visit(string url) Visits url from the current page. It clears up all the forward history.
        string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
        string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.
        
    
    Example:
        Input:
        ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
        [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
        Output:
        [null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]
    
        Explanation:
            BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
            browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
            browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
            browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
            browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
            browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
            browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
            browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
            browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
            browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
            browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
     
    
    Constraints:
        1 <= homepage.length <= 20
        1 <= url.length <= 20
        1 <= steps <= 100
        homepage and url consist of  '.' or lower case English letters.
        At most 5000 calls will be made to visit, back, and forward.
        
    https://leetcode.com/problems/design-browser-history
    """
    
    class Node:
        def __init__(self, val, nxt, prev):
            self.val = val
            self.prev = prev
            self.nxt = nxt
    
    class DLL:
        def __init__(self, head_val):
            self.head = Node(head_val, None, None)
            self.tail = Node("", None, self.head)
            self.head.nxt = self.tail
    
        def add_node(self, val):
            prev = self.tail.prev
    
            node = Node(val, self.tail, prev)
    
            self.tail.prev = node
            prev.nxt = node
    
            return node
    
        def remove_all_after_node(self, node):
            node.nxt = self.tail
            self.tail.prev = node
    
        # for debugging
        def print_all(self):
            curr = self.head
            res = []
            while curr:
                res.append(curr.val)
                curr = curr.nxt
            print(res)
    
    class BrowserHistory:
        """ 
        - Use a special DLL to manage the history.
        - Have a `current_page` pointer pointing to a node in the DLL
        - `back(steps)`:
            - `self.current_page = self.current_page.prev` for the number of steps
        - `forward(steps)`:
            - `self.current_page = self.current_page.nxt` for the number of steps
        - `visit(url)`:
            - `self.history.remove_all_after_node(self.current_page)` <- clear forward history
            - `DLL.add_node(url)`
        """
    
        def __init__(self, homepage: str):
            self.history = DLL(homepage)
            self.current_page = self.history.head
    
        def visit(self, url: str):
            # clear forward history
            self.history.remove_all_after_node(self.current_page)
            # add url to history
            self.current_page = self.history.add_node(url)
    
        def back(self, steps: int):
            while self.current_page.prev and steps > 0:
                self.current_page = self.current_page.prev
                steps -= 1
    
            return self.current_page.val
    
        def forward(self, steps: int):
            # move forward by the steps
            # if greater than the size of the history, fallback to the last page
    
            # stop the loop at the end of the history (just before the tail)
            while self.current_page.nxt.nxt and steps > 0:
                self.current_page = self.current_page.nxt
                steps -= 1
    
            return self.current_page.val
    
    # Your BrowserHistory object will be instantiated and called as such:
    # obj = BrowserHistory(homepage)
    # obj.visit(url)
    # param_2 = obj.back(steps)
    # param_3 = obj.forward(steps)
    ```
    

- [Design A Leaderboard - LeetCode](https://leetcode.com/problems/design-a-leaderboard/)
    
    ![Screenshot 2021-11-09 at 12.53.09.png](_Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Screenshot_2021-11-09_at_12.53.09.png)
    
    ![Screenshot 2021-11-09 at 12.54.12.png](_Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Screenshot_2021-11-09_at_12.54.12.png)
    
    ![Screenshot 2021-11-09 at 12.53.55.png](_Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Screenshot_2021-11-09_at_12.53.55.png)
    
    ![Screenshot 2021-11-09 at 12.54.43.png](_Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Screenshot_2021-11-09_at_12.54.43.png)
    
    Code 2
    
    ```python
    from sortedcontainers import SortedDict
    
    class Leaderboard:
    
        def __init__(self):
            self.scores = {}
            self.sortedScores = SortedDict()
    
        def addScore(self, playerId: int, score: int) -> None:
    
            # The scores dictionary simply contains the mapping from the
            # playerId to their score. The sortedScores contain a BST with 
            # key as the score and value as the number of players that have
            # that score.     
            if playerId not in self.scores:
                self.scores[playerId] = score
                self.sortedScores[-score] = self.sortedScores.get(-score, 0) + 1
            else:
                preScore = self.scores[playerId]
                val = self.sortedScores.get(-preScore)
                if val == 1:
                    del self.sortedScores[-preScore]
                else:
                    self.sortedScores[-preScore] = val - 1    
                
                newScore = preScore + score;
                self.scores[playerId] = newScore
                self.sortedScores[-newScore] = self.sortedScores.get(-newScore, 0) + 1
            
        def top(self, K: int) -> int:
            count, total = 0, 0;
    
            for key, value in self.sortedScores.items():
                times = self.sortedScores.get(key)
                for _ in range(times): 
                    total += -key;
                    count += 1;
                    
                    # Found top-K scores, break.
                    if count == K:
                        break;
                    
                # Found top-K scores, break.
                if count == K:
                    break;
            
            return total;
    
        def reset(self, playerId: int) -> None:
            preScore = self.scores[playerId]
            if self.sortedScores[-preScore] == 1:
                del self.sortedScores[-preScore]
            else:
                self.sortedScores[-preScore] -= 1
            del self.scores[playerId];
    ```
    

---

- Read N Characters Given Read4
    
    ```python
    """ 
    157. Read N Characters Given Read4
    
    Given a file and assume that you can only read the file using a given method read4, 
    implement a method to read n characters.
    
    Method read4:
        The API read4 reads four consecutive characters from file, then writes those characters into the buffer array buf4.
        The return value is the number of actual characters read.
        Note that read4() has its own file pointer, much like FILE *fp in C.
    
    Definition of read4
        Parameter:  char[] buf4
        Returns:    int
    
    buf4[] is a destination, not a source. The results from read4 will be copied to buf4[].
    
    Below is a high-level example of how read4 works:
    
        File file("abcde"); // File is "abcde", initially file pointer (fp) points to 'a'
        char[] buf4 = new char[4]; // Create buffer with enough space to store characters
        read4(buf4); // read4 returns 4. Now buf4 = "abcd", fp points to 'e'
        read4(buf4); // read4 returns 1. Now buf4 = "e", fp points to end of file
        read4(buf4); // read4 returns 0. Now buf4 = "", fp points to end of file
     
    
    Method read:
        By using the read4 method, implement the method read that reads n characters from file and store it in the buffer array buf. 
        Consider that you cannot manipulate file directly.
        The return value is the number of actual characters read.
    
    Definition of read:
        Parameters:	char[] buf, int n
        Returns:	int
    
    buf[] is a destination, not a source. You will need to write the results to buf[].
    
    Note:
        Consider that you cannot manipulate the file directly. The file is only accessible for read4 but not for read.
        The read function will only be called once for each test case.
        You may assume the destination buffer array, buf, is guaranteed to have enough space for storing n characters.
     
    
    Example 1:
        Input: file = "abc", n = 4
        Output: 3
        Explanation: 
            After calling your read method, buf should contain "abc". We read a total of 3 characters from the file, so return 3.
        Note that "abc" is the file's content, not buf. buf is the destination buffer that you will have to write the results to.
    Example 2:
        Input: file = "abcde", n = 5
        Output: 5
        Explanation: 
            After calling your read method, buf should contain "abcde". We read a total of 5 characters from the file, so return 5.
    Example 3:
        Input: file = "abcdABCD1234", n = 12
        Output: 12
        Explanation: 
            After calling your read method, buf should contain "abcdABCD1234". We read a total of 12 characters from the file, so return 12.
    Example 4:
        Input: file = "leetcode", n = 5
        Output: 5
        Explanation: 
            After calling your read method, buf should contain "leetc". We read a total of 5 characters from the file, so return 5.
    """
    import math
    
    def read4(buf4): return -1
    
    """
    The read4 API is already defined for you.
    
        @param buf4, a list of characters
        @return an integer
        def read4(buf4):
    
    # Below is an example of how the read4 API can be called.
    file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
    buf4 = [' '] * 4 # Create buffer with enough space to store characters
    read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
    read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
    read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
    """
    
    class Solution:
        def read(self, buf, n):
            """
            :type buf: Destination buffer (List[str])
            :type n: Number of characters to read (int)
            :rtype: The number of actual characters read (int)
            """
    
            buf4 = [""] * 4
            idx = 0
            for _ in range(math.ceil(n/4)):
                # # read characters
                num_read = read4(buf4)
    
                max_read = num_read
                # ensure we do not read more than required
                # if (idx + num_read - 1) > (n - 1):  # -1 to use indices
                if idx + num_read > n:
                    max_read = n-idx
    
                # # add the read characters to buf
                for num in range(max_read):
                    buf[idx] = buf4[num]
                    idx += 1
    
            return idx
    ```
    
- Read N Characters Given Read4 II - Call multiple times
    
    ```python
    """ 
    Read N Characters Given Read4 II - Call multiple times:
    
    Given a file and assume that you can only read the file using a given method read4, 
    implement a method read to read n characters. Your method read may be called multiple times.
    
    Method read4:
        The API read4 reads four consecutive characters from file, then writes those characters into the buffer array buf4.
        The return value is the number of actual characters read.
        Note that read4() has its own file pointer, much like FILE *fp in C.
    
    Definition of read4:
        Parameter:  char[] buf4
        Returns:    int
    
    buf4[] is a destination, not a source. The results from read4 will be copied to buf4[].
    
    Below is a high-level example of how read4 works:
        File file("abcde"); // File is "abcde", initially file pointer (fp) points to 'a'
        char[] buf4 = new char[4]; // Create buffer with enough space to store characters
        read4(buf4); // read4 returns 4. Now buf4 = "abcd", fp points to 'e'
        read4(buf4); // read4 returns 1. Now buf4 = "e", fp points to end of file
        read4(buf4); // read4 returns 0. Now buf4 = "", fp points to end of file
     
    
    Method read:
        By using the read4 method, implement the method read that reads n characters from file and store it in the buffer array buf. Consider that you cannot manipulate file directly.
        The return value is the number of actual characters read.
    
    Definition of read:
        Parameters:	char[] buf, int n
        Returns:	int
    
    buf[] is a destination, not a source. You will need to write the results to buf[].
    
    Note:
        Consider that you cannot manipulate the file directly. The file is only accessible for read4 but not for read.
        The read function may be called multiple times.
        Please remember to RESET your class variables declared in Solution, as static/class variables are persisted across multiple test cases. Please see here for more details.
        You may assume the destination buffer array, buf, is guaranteed to have enough space for storing n characters.
        It is guaranteed that in a given test case the same buffer buf is called by read.
     
    
    Example 1:
        Input: file = "abc", queries = [1,2,1]
        Output: [1,2,0]
        Explanation: The test case represents the following scenario:
        File file("abc");
        Solution sol;
        sol.read(buf, 1); // After calling your read method, buf should contain "a". We read a total of 1 character from the file, so return 1.
        sol.read(buf, 2); // Now buf should contain "bc". We read a total of 2 characters from the file, so return 2.
        sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0.
        Assume buf is allocated and guaranteed to have enough space for storing all characters from the file.
    Example 2:
        Input: file = "abc", queries = [4,1]
        Output: [3,0]
        Explanation: The test case represents the following scenario:
        File file("abc");
        Solution sol;
        sol.read(buf, 4); // After calling your read method, buf should contain "abc". We read a total of 3 characters from the file, so return 3.
        sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0.
    
    https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times
    # https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/discuss/49607/The-missing-clarification-you-wish-the-question-provided
    # https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/discuss/49601/What-is-the-difference-between-call-once-and-call-multiple-times
    """
    from collections import deque
    
    # The read4 API is already defined for you.
    def read4(buf4): return -1
    
    class Solution:
        def __init__(self):
            self.read_items_queue = deque()
            self.buf4 = [""] * 4
    
        def read(self, buf, n):
    
            prev_read_count = 4
            idx = 0
            # # if we haven't read all the characters yet there are more to be read
            #   more to be read: have items in queue or did not reach end of file (read4)
            while idx < n and (self.read_items_queue or prev_read_count):
    
                # we have prev characters
                if self.read_items_queue:
                    buf[idx] = self.read_items_queue.popleft()
                    idx += 1
    
                # add more characters to the queue
                prev_read_count = read4(self.buf4)
                self.read_items_queue += self.buf4[:prev_read_count]
    
            return idx
    
    """ 
    
    """
    
    class Solution_:
        def __init__(self):
            self.queue = []
            self.buf4 = [""] * 4
    
        def read(self, buf, n):
    
            num_read = 4
            idx = 0
    
            while idx < n:
    
                # we have prev characters
                if self.queue:
                    buf[idx] = self.queue.pop(0)
                    idx += 1
    
                # the last time we read we found that we have no more characters
                elif num_read < 4:
                    return idx
    
                # add more characters to the queue
                else:
                    num_read = read4(self.buf4)
                    self.queue += self.buf4[:num_read]
    
            return idx
    ```
    

### Deck of cards

[Design Interview Question: Design a Deck of Cards [Logicmojo.com]](https://youtu.be/lDa8I7iA5FA)

[Deck of Cards | Object Oriented Designs](https://youtu.be/yENwNPu2Obo)

[Python OOP - Deck of Cards](https://youtu.be/t8YkjDH86Y4)

```python
# PROBLEM --------------------------------------------------------
""" 
Deck of Cards: 
Design the data structures for a generic deck of cards. 
Explain how you would subclass the data structures to implement blackjack.
"""
from enum import Enum
import random

# SOLUTION --------------------------------------------------------
""" 
# Gather requirements ---------------------------------------

First, we need to recognize that a "generic" deck of cards can mean many things. 
Generic could mean a standard deck of cards that can play a poker-like game, or it could even stretch to Uno or Baseball cards. 
It is important to ask your interviewer what she means by generic.
Let's assume that your interviewer clarifies that the deck is a standard 52-card set, like you might see used in a blackjack or poker game. 

The game might also have a player

# High level design ---------------------------------------

- Card: we have cards:
    - We have 4 groups (suit) of cards:
        - Clubs
        - Diamonds
        - Hearts
        - Spades
    - The cards also have a label (face value):
        - (2-10)
        - Jack
        - Queen
        - King
        - Ace
        # - Jokers
- Deck: We have a deck of cards that is comprised of all of the above groups of cards:
    - cards # will have a list of 54 cards
    - shuffle() => None
    - draw() => Card
- Player: We can have a player that has a hand of cards:
    - name: string
    - hand: have a list of cards
    - draw(deck) => None
    - show_hand() => None
    - discard() => Card

"""

# Constants & Enums ----------------------------------------------------

class Suit(Enum):
    # name = value
    CLUBS = "Clubs"
    DIAMONDS = "Diamonds"
    HEARTS = "Hearts"
    SPADES = "Spades"

class FaceValue(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

# Classes ----------------------------------------------------

class Card:
    def __init__(self, suit, face_value):
        self.suit = suit
        self.face_value = face_value

    def __str__(self):
        return f"{self.face_value.name} of {self.suit.name}"

    def get_value(self):
        return self.face_value.value

class Deck:
    def __init__(self):
        self.cards = []
        self._create_deck()

    def draw(self):
        """Return the top card"""
        return self.cards.pop()

    def shuffle(self, num=1):
        """Shuffle the deck"""
        length = len(self.cards)
        for _ in range(num):
            # This is the fisher yates shuffle algorithm
            for i in range(length-1, 0, -1):
                randi = random.randint(0, i)
                if i == randi:
                    continue
                self.cards[i], self.cards[randi] = self.cards[randi], self.cards[i]

    def show_cards(self):
        for card in self.cards:
            print(card)

    def _create_deck(self):
        """Generate 52 cards"""
        for suit in Suit:
            for face_value in FaceValue:
                self.cards.append(Card(suit, face_value))

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        """Pick card from the deck"""
        self.hand.append(deck.draw())

    def show_hand(self):
        for card in self.hand:
            print(card)

    def discard(self):
        return self.hand.pop()

# Test making a Deck
deck = Deck()
deck.shuffle()
deck.show_cards()

bob = Player("Bob")
print(bob.name)
bob.draw(deck)
bob.draw(deck)
bob.draw(deck)
bob.show_hand()
```

### **Movie Ticket Booking System**

[Movie Ticket Booking System || Object Oriented Design || Case Study - LeetCode Discuss](https://leetcode.com/discuss/general-discussion/1112242/Movie-Ticket-Booking-System-oror-Object-Oriented-Design-oror-Case-Study)

### Parking lot

[Parking Lot Design | Object Oriented Design Interview Question](https://youtu.be/tVRyb4HaHgw)

[Object Oriented Design Interview Question Design a Car Parking Lot](https://youtu.be/YRlRGi2pCRM)

[System Design Interview Question: DESIGN A PARKING LOT - asked at Google, Facebook](https://youtu.be/DSGsa0pu8-k)

```python
""" 
Parking Lot: Design a parking lot using object-oriented principles.

https://youtu.be/tVRyb4HaHgw
"""
from datetime import datetime
from typing import List
from abc import ABC, abstractmethod

""" 

# Gather requirements ---------------------------------------

The wording of this question is vague, just as it would be in an actual interview. 
- Can have 10000 - 3000 parking lots
- Will have 4 entries and 4 exits
    - will print ticket
- Parking spot is assigned at the gate
    - Should be the closest to the gate
- Will have a limit on capacity
- Diffrent parking spots
    - Handicap
    - Compact
    - Large
    - Motorcycle
- Will have hourly rates
- Can pay via Cash or Credit Card
- Will have monitoring system
- Should be able to be used on diffrent parking lot systems

# High level design ---------------------------------------

## ParkingSpot:
- id: int
- location: int[2]
- reserved: bool
- is_reserved: bool

    ### HandicapParkingSpot:
    ### CompactParkingSpot:
    ### LargeParkingSpot:
    ### MotorcycleParkingSpot:
- type: Enum(Handicap, Compact, Large, Motorcycle) not used as it will violate the open/closed principle - adding new types will require changes to the code

## ParkingTicket:
- id: int
- parking_spot: ParkingSpot (has type and id)
- issued_at: datetime

## RateCalculator:
- rate_per_hour: float

## ParkingSpotAssigner: # https://youtu.be/tVRyb4HaHgw?t=996
- assign_spot(Terminal): ParkingSpot 

## PaymentCalculator:
- calculate_payment(ParkingTicket): int

## PaymentProcessor:
    - process_payment(amount:float): None
    ### CashPaymentProcessor:
    ### CreditCardPaymentProcessor:

## Terminal:
- id: int
- location: int[2]
- get_id(): => int

    ### EntryTerminal:
    - closest_spots: ParkingSpot[] <-- will actually be a priority list/ mean heap
    - enter(Vehicle): ParkingTicket
        assign spot using ParkingSpotAssigner
        _create_ticket(ParkingSpot)
    - _create_ticket(ParkingSpot): ParkingTicket
    - remove_parking_spot_from_closest_spots(ParkingSpot): None
    - add_parking_spot_to_closest_spots(ParkingSpot): None
    ### ExitTerminal:
    - exit(ParkingTicket): bool
        calculate payment using PaymentCalculator
        charge payment using PaymentProcessor
        free ParkingSpot

## Monitor/Logger:
## ParkingLotSystem: <- will be singleton
- entry_terminals: EntryTerminals[]
- exit_terminals: ExitTerminals[]
- available_spots: ParkingSpot[]
- reserved_spots: ParkingSpot[]
- _create_parking_spots(n:int): None
- _create_terminals(number_of_entry_terminals: int, number_of_exit_terminals: int): None
- park_vehicle(terminal:EntryTerminal): ParkingTicket
- remove_vehicle(terminal:ExitTerminal): ParkingTicket
- get_entry_terminals(): EntryTerminal[]
- is_full(): bool

## Vehicle:? - no need to use it
-> not needed
-> is an actor
-> not needed as this is not a simulation

"""

# TODO: remove vehicle

# ParkingSpot

class ParkingSpot(ABC):
    def __init__(self, id, x_location, y_location):
        self.id = id
        self.reserved = False
        self.location = [x_location, y_location]

    def is_reserved(self):
        return self.reserved

    @abstractmethod
    def occupy_spot(self):
        pass

class HandicapParkingSpot(ParkingSpot):
    def __init_(self, id, x_location, y_location):
        return super().__init__(id, x_location, y_location)

    def occupy_spot(self):
        pass

class CompactParkingSpot(ParkingSpot):
    def __init_(self, id, x_location, y_location):
        return super().__init__(id, x_location, y_location)

    def occupy_spot(self):
        pass

class LargeParkingSpot(ParkingSpot):
    def __init_(self, id, x_location, y_location):
        return super().__init__(id, x_location, y_location)

    def occupy_spot(self):
        pass

class MotorcycleParkingSpot(ParkingSpot):
    def __init_(self, id, x_location, y_location):
        return super().__init__(id, x_location, y_location)

    def occupy_spot(self):
        pass

# ParkingTicket

class ParkingTicket:
    def __init__(self, id, parking_spot: 'ParkingSpot'):
        self.id = id
        self.parking_spot = parking_spot
        self.issued_at = datetime.now()

# RateCalculator

class RateCalculator:
    def __init__(self, rate_per_hour):
        self.rate_per_hour = rate_per_hour

    def calculate_rate(self, parking_ticket: 'ParkingTicket'):
        pass

# ParkingSpotAssigner

class ParkingSpotAssigner:
    def __init__(self):
        pass

    def assign_spot(self, terminal: 'Terminal'):
        pass

# PaymentCalculator

class PaymentCalculator:

    def calculate_payment(self, parking_ticket: 'ParkingTicket'):
        pass

# PaymentProcessor

class PaymentProcessor(ABC):
    def __init__(self, amount: float):
        self.amount = amount

    @abstractmethod
    def process_payment(self, amount: float):
        pass

class CashPaymentProcessor(PaymentProcessor):
    def __init__(self, amount: float):
        super().__init__(amount)

    def process_payment(self, amount: float):
        pass

class CreditCardPaymentProcessor(PaymentProcessor):
    def __init__(self, amount: float):
        super().__init__(amount)

    def process_payment(self, amount: float):
        pass

# Terminal

class Terminal(ABC):
    def __init__(self, id: int, location: List[int],):
        self.id = id
        self.location = location

    def get_id(self):
        return self.id

class EntryTerminal(Terminal):
    def __init__(self, id: int, location: List[int], parking_spots: 'List[ParkingSpot]'):
        super().__init__(id, location)
        self.closest_spots = []  # should be a priority queue

    def enter(self):
        pass

    def _create_ticket(self, parking_spot: 'ParkingSpot'):
        pass

    def remove_parking_spot_from_closest_spots(self, parking_spot: 'ParkingSpot'):
        pass

    def add_parking_spot_to_closest_spots(self, parking_spot: 'ParkingSpot'):
        pass

class ExitTerminal(Terminal):
    def __init__(self, id: int, location: List[int], parking_spots: 'List[ParkingSpot]'):
        super().__init__(id, location)

    def exit(self):
        pass

# Monitor/Logger

class Logger:
    pass

# ParkingLotSystem

class ParkingLotSystem:
    def __init__(self, number_of_parking_spots: int, number_of_entry_terminals: int, number_of_exit_terminals: int):
        self.available_spots = []
        self.reserved_spots = []
        self._create_parking_spots(number_of_parking_spots)
        self.entry_terminals = []
        self.exit_terminals = []
        self._create_terminals(number_of_entry_terminals,
                               number_of_exit_terminals)

    def park_vehicle(self, terminal: 'EntryTerminal'):
        pass

    def remove_vehicle(self, terminal: 'ExitTerminal'):
        pass

    def is_full(self):
        pass

    def get_entry_terminals(self):
        pass

    def _create_parking_spots(self, number_of_parking_spots: int):
        pass

    def _create_terminals(self, number_of_entry_terminals: int, number_of_exit_terminals: int):
        pass
```

### Design file system

```python
"""
# Gather requirements ---------------------------------------

- Have files
- Have folders
	- can contain files and folders
- Files and folders have
	- name
	- time_last_accessed
	- time_created
	- time_last_modified
	- path
	- delete()

- Can delete file & folder
- Can change name

# High level design ---------------------------------------

## FileAndFolderStructure
- name
- parent
- time_last_accessed
- time_created
- time_last_modified
- path(): str
- size(): float
- change_name(): str
- delete(): None
- get_time_last_accessed(): str
- get_time_created(): str
- get_time_last_modified(): str

	### File
	- file_size
	### Folder
	- children{,}
	- delete_child()
	- add_child(FileAndFolderStructure): bool
    - is_empty(): bool

"""

from abc import ABC, abstractmethod
from datetime import datetime

class FileAndFolderStructure(ABC):
    def __init__(self, name: str, parent: 'Folder|None'):
        self.name = name
        self.parent = parent
        self.time_last_accessed = datetime.now()
        self.time_created = datetime.now()
        self.time_last_modified = datetime.now()

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @property
    def path(self):
        if not self.parent:
            return ""  # root dir
        else:
            return self.parent.path + "/" + self.name

    def change_name(self, name):
        self.name = name
        return self.name

    def get_time_last_accessed(self):
        return self.time_last_accessed

    def get_time_created(self):
        return self.time_created

    def get_time_last_modified(self):
        return self.time_last_modified

class File(FileAndFolderStructure):

    def __init__(self, name: str, parent: 'Folder', file_size):
        super().__init__(name, parent)
        self.file_size = file_size

    def size(self):
        return self.file_size

    def delete(self):
        self.parent.delete_child(self)

class Folder(FileAndFolderStructure):
    def __init__(self, name: str, parent: 'Folder|None'):
        super().__init__(name, parent)
        self.children = set()

    def size(self):
        total_size = 0
        for child in self.children:
            total_size += child.size()
        return total_size

    def delete(self):
        for child in self.children:
            child.delete()
        if self.parent:
            self.parent.delete_child(self)

    def add_child(self, child: 'FileAndFolderStructure'):
        self.children.add(child)
        return True

    def delete_child(self, child: 'FileAndFolderStructure'):
        if child in self.children:
            self.children.remove(child)
            return True
        return False

    def is_empty(self):
        return len(self.children) == 0

root = Folder("root", None)

pictures = Folder("pictures", root)

paul_png = File("paul.png", pictures, 22)

print(root.path)  #
print(pictures.path)  # /pictures/paul.png
print(paul_png.name)  # paul.png
print(paul_png.path)  # /pictures/paul.png
```

### Design Unix File Search API / Linux Find Command

```python
# Design Unix File Search API / Linux Find Command
""" 
As for what I would expect (not necessarily all of these):
    - Obviously coming straight to the right design (encapsulating the Filtering logic into its own interface etc...), with an explanation on why this approach is good. I'm obviously open to alternate approaches as long as they are as flexible and elegant.
    - Implement boolean logic: AND/OR/NOT, here I want to see if the candidate understands object composition
    - Support for symlinks. Rather than seeing the implementation (which I don't really care about) I want to understand the tradeoffs of adding yet another parameter to the find method VS other options (eg. Constructor). Keep adding params to a method is usually bad.
    - How to handle the case where the result is really big (millions of files), and you may not be able to put all of them into a List.
"""
from abc import ABC, abstractmethod
from collections import deque
from typing import List

# File
# - no need to implement different files & directories as that will not be used in this system

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.children = []
        self.is_directory = False if '.' in name else True
        self.children = []
        self.extension = name.split(".")[1] if '.' in name else ""

    def __repr__(self):
        return "{"+self.name+"}"

# Filters

class Filter(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def apply(self, file):
        pass

class MinSizeFilter(Filter):
    def __init__(self, size):
        self.size = size

    def apply(self, file):
        return file.size > self.size

class ExtensionFilter(Filter):
    def __init__(self, extension):
        self.extension = extension

    def apply(self, file):
        return file.extension == self.extension

# LinuxFindCommand

class LinuxFind():
    def __init__(self):
        self.filters: List[Filter] = []

    def add_filter(self, given_filter):
        # validate given_filter is a filter
        if isinstance(given_filter, Filter):
            self.filters.append(given_filter)

    def apply_OR_filtering(self, root):
        found_files = []

        # bfs
        queue = deque()
        queue.append(root)
        while queue:
            # print(queue)
            curr_root = queue.popleft()
            if curr_root.is_directory:
                for child in curr_root.children:
                    queue.append(child)
            else:
                for filter in self.filters:
                    if filter.apply(curr_root):
                        found_files.append(curr_root)
                        print(curr_root)
                        break
        return found_files

    def apply_AND_filtering(self, root):
        found_files = []

        # bfs
        queue = deque()
        queue.append(root)
        while queue:
            curr_root = queue.popleft()
            if curr_root.is_directory:
                for child in curr_root.children:
                    queue.append(child)
            else:
                is_valid = True
                for filter in self.filters:
                    if not filter.apply(curr_root):
                        is_valid = False
                        break
                if is_valid:
                    found_files.append(curr_root)
                    print(curr_root)

        return found_files

f1 = File("root_300", 300)

f2 = File("fiction_100", 100)
f3 = File("action_100", 100)
f4 = File("comedy_100", 100)
f1.children = [f2, f3, f4]

f5 = File("StarTrek_4.txt", 4)
f6 = File("StarWars_10.xml", 10)
f7 = File("JusticeLeague_15.txt", 15)
f8 = File("Spock_1.jpg", 1)
f2.children = [f5, f6, f7, f8]

f9 = File("IronMan_9.txt", 9)
f10 = File("MissionImpossible_10.rar", 10)
f11 = File("TheLordOfRings_3.zip", 3)
f3.children = [f9, f10, f11]

f11 = File("BigBangTheory_4.txt", 4)
f12 = File("AmericanPie_6.mp3", 6)
f4.children = [f11, f12]

greater5_filter = MinSizeFilter(5)
txt_filter = ExtensionFilter("txt")

my_linux_find = LinuxFind()
my_linux_find.add_filter(greater5_filter)
my_linux_find.add_filter(txt_filter)

print(my_linux_find.apply_OR_filtering(f1))
print(my_linux_find.apply_AND_filtering(f1))
```

```java
package linux_find_command;

// https://www.programmersought.com/article/31817103996/

/*
As for what I would expect (not necessarily all of these):
    - Obviously coming straight to the right design (encapsulating the Filtering logic into its own interface etc...), with an explanation on why this approach is good. I'm obviously open to alternate approaches as long as they are as flexible and elegant.
    - Implement boolean logic: AND/OR/NOT, here I want to see if the candidate understands object composition
    - Support for symlinks. Rather than seeing the implementation (which I don't really care about) I want to understand the tradeoffs of adding yet another parameter to the find method VS other options (eg. Constructor). Keep adding params to a method is usually bad.
    - How to handle the case where the result is really big (millions of files), and you may not be able to put all of them into a List.
*/

// "static void main" must be defined in a public class.
public class LinuxFindCommand {
    public static void main(String[] args) {
      new LinuxFindCommand().test();
    }
    
    private void test() {
      SearchParams params = new SearchParams();
      params.extension = "xml";
      params.minSize = 2;
      params.maxSize = 100;
   
      File xmlFile = new File();
      xmlFile.setContent("aaa.xml".getBytes());
      xmlFile.name = "aaa.xml";
   
      File txtFile = new File();
      txtFile.setContent("bbb.txt".getBytes());
      txtFile.name = "bbb.txt";
   
      File jsonFile = new File();
      jsonFile.setContent("ccc.json".getBytes());
      jsonFile.name = "ccc.json";
   
      Directory dir1 = new Directory();
      dir1.addEntry(txtFile);
      dir1.addEntry(xmlFile);
   
      Directory dir0 = new Directory();
      dir0.addEntry(jsonFile);
      dir0.addEntry(dir1);
   
      FileSearcher searcher = new FileSearcher();
      System.out.println(searcher.search(dir0, params));
    }

    // Files
   
    public interface IEntry {
   
      String getName();
   
      void setName(String name);
   
      int getSize();
   
      boolean isDirectory();
    }

   
    private abstract class Entry implements IEntry {
      protected String name;
   
      @Override
      public String getName() {
        return name;
      }
   
      @Override
      public void setName(String name) {
        this.name = name;
      }
      
    }
   

    public class File extends Entry {
      private byte[] content;
   
      public String getExtension() {
        return name.substring(name.indexOf(".") + 1);
      }
   
      public void setContent(byte[] content) {
        this.content = content;
      }
   
      public byte[] getContent() {
        return content;
      }
   
      @Override
      public int getSize() {
        return content.length;
      }
   
      @Override
      public boolean isDirectory() {
        return false;
      }
      
      @Override
      public String toString() {
        return "File{" +
          "name='" + name + '\'' +
          '}';
      }
    }
   
    public class Directory extends Entry {
        private List<Entry> entries = new ArrayList<>();
   
      @Override
      public int getSize() {
        int size = 0;
        for (Entry entry  : entries) {
          size += entry.getSize();
        }
   
        return size;
      }
   
      @Override
      public boolean isDirectory() {
        return true;
      }
   
      public void addEntry(Entry entry) {
        this.entries.add(entry);
      }
    }

    //  Filters
   
    public class SearchParams {
      String extension;
      Integer minSize;
      Integer maxSize;
      String name;
    }
   
    public interface IFilter {
   
        boolean isValid(SearchParams params, File file);
   
    }
   
    public class ExtensionFilter implements IFilter {
   
      @Override
      public boolean isValid(SearchParams params, File file) {
        if (params.extension == null) {
          return true;
        }
   
        return file.getExtension().equals(params.extension);
      }
   
    }
   
    public class MinSizeFilter implements IFilter {
   
      @Override
      public boolean isValid(SearchParams params, File file) {
        if (params.minSize == null) {
          return true;
        }
   
        return file.getSize() >= params.minSize;
      }
   
    }
   
    public class MaxSizeFilter implements IFilter {
   
      @Override
      public boolean isValid(SearchParams params, File file) {
        if (params.maxSize == null) {
          return true;
        }
   
        return file.getSize() <= params.maxSize;
      }
   
    }
   
    public class NameFilter implements IFilter {
   
      @Override
      public boolean isValid(SearchParams params, File file) {
        if (params.name == null) {
        return true;
        }
   
        return file.getName().equals(params.name);
      }
   
    }
   
    public class FileFilter {
      private final List<IFilter> filters = new ArrayList<>();
   
      public FileFilter() {
        filters.add(new NameFilter());
        filters.add(new MaxSizeFilter());
        filters.add(new MinSizeFilter());
        filters.add(new ExtensionFilter());
      }
   
      public boolean isValid(SearchParams params, File file) {
        for (IFilter filter : filters) {
          if (!filter.isValid(params, file)) {
            return false;
          }
        }
   
        return true;
      }
   
    }

    // Searcher
   
    public class FileSearcher {
      private FileFilter filter = new FileFilter();
   
      public List<File> search(Directory dir, SearchParams params) {
        List<File> files = new ArrayList<>();
   
        Queue<Directory> queue = new LinkedList<>();
        queue.add(dir);
   
        while (!queue.isEmpty()) {
          Directory folder = queue.poll();
   
          for (IEntry entry : folder.entries) {
            if (entry.isDirectory()) {
            queue.add((Directory) entry);
            } else {
            File file = (File) entry;
            if (filter.isValid(params, file)) {
              files.add(file);
            }
            }
          }
        }
   
        return files;
        }
    }
      
  }
```

### Design elevator

```python
""" 
# Design an elevator
https://youtu.be/siqiJAJWUVg
https://thinksoftware.medium.com/elevator-system-design-a-tricky-technical-interview-question-116f396f2b1c
"""

"""
## Requirements collection ------------------------------------------------------------

- elevator system
    - can have around 200 floors
    - with 50 elevator cars
    - minimise wait time of system/passenger
    - high throughput
    - reduce power usage / cost
    - can have operational zones: like floor 20-30
        - we will assume that this system we are building will work for one specific zone only
            it can then be replicated for the other zones
- elevator cars
    - has three states: UP, DOWN & IDLE
    - can transfer passengers from one floor to another
    - can only open door whn idle
    - max_load
    - max_speed
- emergency alarms
- VIP
- monitoring systems

## Use cases  ------------------------------------------------------------------s

1. Calling the elevator
2. Move/Stop elevators
3. Directions
4. Floor
5. Emergency call
5. Emergency floor

## High level design ------------------------------------------------------------------

### Door
- is_open
- open()
- close()

### ElevatorCarMotion
- move(floor: int)
- stop()

### ElevatorCar
- door: Door

### Floor
- button_panel: ButttonPanel

### Button
- is_pressed()
- press()
    
    #### HallButton
    - press()
    #### ElevatorButton
    - press()

### ButttonPanel
- botton: HallButton

### Dispatcher https://www.youtube.com/watch?v=siqiJAJWUVg&t=1205s
=> can use first-come-first-serve with queue
    send nearest (idle) or (moving in same direction towards passenger) elevator to passenger
=> shortest seek time first
    - use pq or array of floors
    - find closest passengers
=> scan

### Monitor/Logger

### ElevatorSystem

### Passenger?
=> not needed
=> is an actor
=> not needed as this is not a simulation

"""
```

### Design hashtable

[Data Structures: Hash Tables](https://youtu.be/shs0KM3wKv8)

[Hash Tables - Beau teaches JavaScript](https://youtu.be/F95z5Wxd9ks)

```
- use a hashfunction to tranform key to an index in array
	-  hashfunction
		- convert string to interger?
- the array has a linked list at each index
	- each node can point back to the original list
	- wehn we run out of space in the array, we implement resizing

## Collision handling
- Chaining
	- store in linked list
```

Object-oriented programming (OOP) is a style of programming that focuses on using objects to design and build applications. Contrary to procedure-oriented programming where programs are designed as blocks of statements to manipulate data, OOP organises the program to **combine data and functionality** and wrap it inside something called an “Object”.

Basic concepts of OOP:

- **Objects:** Objects **represent a real-world entity** and the basic building block of OOP. For example, an Online Shopping System will have objects such as shopping cart, customer, product item, etc.
- **Class:** Class is the prototype or **blueprint of an object**. It is a template definition of the attributes and methods of an object. For example, in the Online Shopping System, the Customer object will have attributes like shipping address, credit card, etc., and methods for placing an order, cancelling an order, etc.

![Screenshot 2021-11-08 at 05.22.57.png](_Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Screenshot_2021-11-08_at_05.22.57.png)

The four principles of object-oriented programming are encapsulation, abstraction, inheritance, and polymorphism.

- **[Encapsulation](_Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d.md):** Encapsulation is the mechanism of binding the data together and **hiding it from the outside world**. Encapsulation is achieved when each object keeps its state private so that other objects don’t have direct access to its state. Instead, they can access this state only through a set of public functions.
- **[Abstraction](_Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d.md):** Abstraction can be thought of as the natural extension of encapsulation. It means **hiding all but the relevant data** about an object in order to reduce the complexity of the system. In a large system, objects talk to each other, which makes it difficult to maintain a large codebase; abstraction helps by hiding internal implementation details of objects and **only revealing operations that are relevant to other objects**.
- **[Inheritance](_Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d.md):** Inheritance is the mechanism of creating new classes from existing ones.
- **[Polymorphism](_Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d.md):** Polymorphism (from Greek, meaning “many forms”) is the ability of an object to take **different forms and thus, depending upon the context, to respond to the same message in different ways**. Take the example of a chess game; a chess piece can take many forms, like bishop, castle, or knight and all these pieces will respond differently to the ‘move’ message

# Theory

[GitHub - knightsj/object-oriented-design: 面向对象设计的设计原则和设计模式](https://github.com/knightsj/object-oriented-design)

## Constructors in Python

`__init__()` function. This special function gets called whenever a new object of that class is instantiated. This type of function is also called **constructor** in Object-Oriented Programming (OOP). We normally use it to initialise all the variables.

```python
class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def get_data(self):
        print(f'{self.real}+{self.imag}j')

# Create a new ComplexNumber object
num1 = ComplexNumber(2, 3)

# Call get_data() method
# Output: 2+3j
num1.get_data()

# Create another ComplexNumber object
# and create a new attribute 'attr'
num2 = ComplexNumber(5)
num2.attr = 10

# Output: (5, 0, 10)
print((num2.real, num2.imag, num2.attr))

# but c1 object doesn't have attribute 'attr'
# AttributeError: 'ComplexNumber' object has no attribute 'attr'
print(num1.attr)
```

**Output**

```
2+3j
(5, 0, 10)
Traceback (most recent call last):
  File "<string>", line 27, in <module>
    print(num1.attr)
AttributeError: 'ComplexNumber' object has no attribute 'attr'
```

In the above example, we defined a new class to represent complex numbers. It has two functions, `__init__()` to initialize the variables (defaults to zero) and `get_data()` to display the number properly.

An interesting thing to note in the above step is that attributes of an object can be created on the fly. We created a new attribute attr for object num2 and read it as well. But this does not create that attribute for object num1.

---

## Inheritance

Inheritance is a way of creating a new class for using details of an existing class without modifying it. The newly formed class is a derived class (or child class). Similarly, the existing class is a base class (or parent class).

We use the super() function inside the **init**() method. This allows us to run the **init**() method of the parent class inside the child class.

```python
# parent class
class Bird:
    
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__() # *************
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()
```

![Screenshot 2021-10-11 at 21.30.49.png](_Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Screenshot_2021-10-11_at_21.30.49.png)

```python
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

class Triangle(Polygon):
    def __init__(self):
        **super().__init__(self,3)**

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)
```

```python
>>> t = Triangle()

>>> t.inputSides()
Enter side 1 : 3
Enter side 2 : 5
Enter side 3 : 4

>>> t.dispSides()
Side 1 is 3.0
Side 2 is 5.0
Side 3 is 4.0

>>> t.findArea()
The area of the triangle is 6.00

```

---

### Method Overriding in Python

In the above example, notice that `__init__()` method was defined in both classes, Triangle as well in Polygon. When this happens, the method in the derived class overrides that in the base class. This is to say, `__init__()` in Triangle gets preference over the `__init__` in Polygon.

Generally, when overriding a base method, we tend to **extend the definition** rather than simply replace it. The same is being done by calling the method in the base class from the one in the derived class (calling `Polygon.__init__()` from `__init__()` in `Triangle`).

> A better option would be to use the built-in function `super()`. So, `super().__init__(3)` is equivalent to `Polygon.__init__(self,3)` and is preferred.
> 

### Composition vs Inheritance

[Composition vs Inheritance](_Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Composition%20vs%20Inheritance%209c1dc560a2724a8ea8a3797540ee10ef.csv)

## Encapsulation

**Encapsulation:** Encapsulation is the mechanism of binding the data together and **hiding it from the outside world**. Encapsulation is achieved when each object **keeps its state private** so that other objects don’t have direct access to its state. Instead, they can access this state only through a set of public functions.

Using OOP in Python, we can restrict access to methods and variables. This prevents data from direct modification which is called encapsulation. In Python, we denote private attributes using underscore as the prefix i.e single _ or double __.

```python
class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell() # Selling Price: 900

# change the price
c.__maxprice = 1000
c.sell() # Selling Price: 900

# using setter function
c.setMaxPrice(1000)
c.sell() # Selling Price: 1000
```

In the above program, we defined a Computer class.

We used `__init__()` method to store the maximum selling price of the `Computer`. We tried to modify the price. However, we can't change it because Python treats the `__maxprice` as private attributes. As shown, to change the value, we have to use a setter function i.e `setMaxPrice()` which takes price as a parameter.

## Abstraction

**Abstraction:** Abstraction can be thought of as the natural extension of encapsulation. It means **hiding all but the relevant data** about an object in order to reduce the complexity of the system. In a large system, objects talk to each other, which makes it difficult to maintain a large codebase; abstraction helps by hiding internal implementation details of objects and **only revealing operations that are relevant to other objects**.

### Abstract Classes

[Python Abstract Class](https://www.pythontutorial.net/python-oop/python-abstract-class/)

[Beginner's guide to abstract base class in Python](https://dev.to/dollardhingra/understanding-the-abstract-base-class-in-python-k7h)

In object-oriented programming, an abstract class is a [class](https://www.pythontutorial.net/python-oop/python-class/) that **cannot be instantiated**. However, you can create classes that inherit from an abstract class. Typically, you use an abstract class to create a **blueprint for other classes**.

Similarly, an **abstract method** is an method without an implementation. An abstract class may or may not include abstract methods.

Python doesn’t directly support abstract classes. But it does offer a [module](https://www.pythontutorial.net/python-basics/python-module/) that allows you to define abstract classes.

To define an abstract class, you use the `abc` (abstract base class) module.

The `abc` module provides you with the infrastructure for defining abstract base classes.

```python
from abc import ABC, abstractmethod

class AbstractClassName(ABC):
    @abstractmethod
    def abstract_method_name(self):
        pass
```

Example

```python
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @abstractmethod
    def get_salary(self):
        pass

class FulltimeEmployee(Employee):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary

    def get_salary(self):
        return self.salary

class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, worked_hours, rate):
        super().__init__(first_name, last_name)
        self.worked_hours = worked_hours
        self.rate = rate

    def get_salary(self):
        return self.worked_hours * self.rate
```

## Polymorphism *

Polymorphism (from Greek, meaning “many forms”) is the ability of an object to take **different forms and thus, depending upon the context, to respond to the same message in different ways**. Take the example of a chess game; a chess piece can take many forms, like bishop, castle, or knight and all these pieces will respond differently to the ‘move’ message

Polymorphism is an ability (in OOP) to **use a common interface for multiple forms (data types)**.

Suppose, we need to color a shape, there are multiple shape options (rectangle, square, circle). However we could use the same method to color any shape. This concept is called Polymorphism.

> Polymorphism means "many forms", it means to have different functions in different situation, just like functions keys on keyboard, same key but with different functions in different pages. B,C,D inherits from A and have same function but performs differently when is called.
> 

```python
class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)
```

## Class & Static attributes

![Screenshot 2021-10-17 at 18.02.19.png](_Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Screenshot_2021-10-17_at_18.02.19.png)

```python
class Parrot:

    # class attribute
    species = "bird"
    names = []

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.names.append(self.name)
        self.age = age

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.species))  # Blu is a bird
print("Woo is also a {}".format(woo.species))  # Woo is also a bird

# access the class attributes
print(Parrot.names)  # ['Blu', 'Woo']
print("Blu is a {}".format(blu.names))  # Blu is a ['Blu', 'Woo']
print("Woo is also a {}".format(woo.names))  # Woo is also a ['Blu', 'Woo']

# access the instance attributes
print("{} is {} years old".format(blu.name, blu.age)) # Blu is 10 years old
print("{} is {} years old".format(woo.name, woo.age)) # Woo is 15 years old
```

---

## Class & Static methods

[Python Tutorial - Static and Class Methods - techwithtim.net](https://www.techwithtim.net/tutorials/python-programming/classes-objects-in-python/static-and-class-methods/)

```python
class myClass:
    count = 0

    def __init__(self, x):
        self.x = x

    @staticmethod
    def staticMethod():
        return "i am a static method"
        # Notice staticMethod does not require the self parameter
        # use as function without access to items in the class eg: instance variables
        # eg: used in creating libraries like math, random, etc

    @classmethod
    def classMethod(cls):
        cls.count += 1
        return cls.count
        # The classMethod can access and modify class variables. It takes the class name as a required parameter

print(myClass.staticMethod())  # i am a static method
print(myClass.classMethod())  # 1
print(myClass.classMethod())  # 2
```

---

## Private and Public Classes

```python
class _Private:
    def __init__(self, name):
        self.name = name

class NotPrivate:
    def __init__(self, name):
        self.name = name
        # Even though we decalre something private we can still call and us it
        self.priv = _Private(name)

    def _dispaly(self):  # Private
        print("Hello")

    def display(self):  # Public
        print("Hi")
```

## Operator Overloading

### Overloading the numerical operators

[Python Operator Overloading](_Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Python%20Operator%20Overloading%200e8809af87164a039f103691140df730.csv)

```python
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

p1 = Point(1, 2)
p2 = Point(2, 3)

print(p1+p2) # (3,5)
```

What actually happens is that, when you use p1 + p2, Python calls `p1.**add**(p2)` which in turn is `Point.**add**(p1,p2)`. After this, the addition operation is carried out the way we specified.

### Overloading Comparison Operators

[Overloading Comparison Operators](_Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Overloading%20Comparison%20Operators%2081101d971d0e4dad92625b304e846520.csv)

```python
# overloading the less than operator
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __lt__(self, other):
        self_mag = (self.x ** 2) + (self.y ** 2)
        other_mag = (other.x ** 2) + (other.y ** 2)
        return self_mag < other_mag

p1 = Point(1,1)
p2 = Point(-2,-3)
p3 = Point(1,-1)

# use less than
print(p1<p2) # True
print(p2<p3) # False
print(p1<p3) # False
```

## Singleton

[Python Design Patterns - Singleton](https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_singleton.htm)

```python
class Singleton:
   __instance = None

   @staticmethod 
   def getInstance():
      """ Static access method. """
      if Singleton.__instance == None:
         Singleton()
      return Singleton.__instance

   def __init__(self):
      """ Virtually private constructor. """
      if Singleton.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         Singleton.__instance = self

s = Singleton()
print s

s = Singleton.getInstance()
print s

s = Singleton.getInstance()
print s
```

# Quick tips

### __hash__

Typically used in hashing. For example while storing a class in a dictionary(hashmap)

```python
from typing import List

class ContactNames:
    def __init__(self, names: List):
        # names is a list of strings
        self.names = names

    def __hash__(self):
        # https://www.programiz.com/python-programming/methods/built-in/hash
        # Conceptually we want to hash the set of names,
        # Since the set type is mutable, it cannot be hashed. Therefore, we use a frozenset. (https://www.notion.so/paulonteri/Hash-Tables-220d9f0e409044c58ec6c2b0e7fe0ab5#a33b73089b544532bddb600fff546306)
        # return hash(self.names) # -> TypeError: unhashable type: 'list'
        return hash(frozenset(self.names)) # we use the built-in hash() function

    def __eq__(self, other):
        return set(self.names) == set(other.names)

    def __str__(self):
        # only used for the testing below
        return " ".join(self.names)

# # Testing if it works
number_store = {}

paul = ContactNames(["Paul", "O"])
number_store[paul] = "999"

paul_similar = ContactNames(["Paul", "O"])

print(number_store[paul])  # 999
print(number_store[paul_similar])  # 999
print(number_store[ContactNames(["Paul", "O"])])  # 999
print(len(number_store))  # 1 -> only has paul

kim = ContactNames(["Kim", "Jackson", "Model"])
number_store[kim] = "444"

print(len(number_store))  # 2 -> only has paul & kim

for key in number_store:
    print(key, ": ", number_store[key])

"""
Additional notes:

The time complexity of computing the hash is O(n), where n is the number of strings in the contact names.
	Hash codes are often cached for performance, with the caveat that the cache must be cleared
	 if object fields that are referenced by the hash function are uPdated.
"""
```

## Use a class within itself

Use self

```python
class Tree:
    def __init__(self, name):
        self.children = []
        self.name = name

    def depthFirstSearch(self, array):
				 # using itself -> by passing down self
        self._depthFirstSearchHelper(array, self)
        return array

    def _depthFirstSearchHelper(self, array, root):
        if not root:
            return

        array.append(root.name)

        for child in root.children:
            self._depthFirstSearchHelper(array, child)
```

## Quick tip (Bad code vs Good code)

Bad code

```python
class Tree:
    def __init__(self, name):
        self.children = []
        self.name = name

    def depthFirstSearch(self, array):
        self._depthFirstSearchHelper(array, self)
        return array

    def _depthFirstSearchHelper(self, array, root):
        if not root:
            return

        array.append(root.name)

        for child in root.children:
            self._depthFirstSearchHelper(array, child)
```

Good code

```python
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def depthFirstSearch(self, array):
        self._depthFirstSearchHelper(array)
        return array

    def _depthFirstSearchHelper(self, array):
        array.append(self.name)
        
        for child in self.children:
            child._depthFirstSearchHelper(array)
```

## Comparing two classes __eq__  __greater__ __gt__

![Screenshot 2021-10-17 at 17.57.43.png](_Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Screenshot_2021-10-17_at_17.57.43.png)

### Examples:

- 'K' Closest Points to the Origin

## Creating a coordinates class

### Examples:

- 'K' Closest Points to the Origin (similar)

## nonlocal

[Python Global, Local and Nonlocal variables](https://www.programiz.com/python-programming/global-local-nonlocal-variables)

The `nonlocal` keyword is used to work with variables **inside nested functions**, where the variable should not belong to the inner function.

Use the keyword `nonlocal` to declare that the variable is not local.

```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]):
        preorder_pos = 0
        inorder_idxs = {val: idx for idx, val in enumerate(inorder)}

        def helper(preorder: List[int], inorder: List[int], inorder_left, inorder_right):
            nonlocal preorder_pos
```

## Enum

```python
>>> from enum import Enum
>>> class Suit(Enum):
...     CLUBS = "Clubs"
...     DIAMONDS = "Diamonds"
...     HEARTS = "Hearts"
...     SPADES = "Spades"
... 

>>> for i in Suit.__members__:
...     print(i)
... 
CLUBS
DIAMONDS
HEARTS
SPADES
>>>
```

## Python Operator Overloading

## TODO: Abstract Base Class *

[Abstract Base Class (abc) in Python - GeeksforGeeks](https://www.geeksforgeeks.org/abstract-base-class-abc-in-python/)

---

# Object Oriented Design

A class is an encapsulation of data and methods that operate on that data. Classes match the way we think about computation. They provide *encapsulation*, which reduces the conceptual burden of writing code, and enable code reuse, through the use of *inheritance* and *polymorphism*. However, naive use of object-oriented constructs can result in code that is hard to maintain. 

A **design pattern** is a general repeatable solution to a commonly occurring problem. It is not a complete design that can be coded up directly—rather, it is a description of how to solve a problem that arises in many different situations. In the context of object-oriented programming, design patterns address both reuse and maintainability. In essence, design patterns make some parts of a system vary independently from the other parts.

**Adnan’s Design Pattern course material**, available freely online, contains lecture notes, homeworks, and labs that may serve as a good resource on the material in this chapter.

## Design patterns

### 1. Template method vs Strategy

Explain the difference between the template method pattern and the strategy pattern with a concrete example. 

**Solution:**

Both the template method and strategy pattems are similar in that:

- both are behavioral pattems,
- both are used to make algorithms reusable,
- and both are general and very widely used.

However, they differ in the following key way:

- In the template method, a skeleton algorithm is provided in a superclass. Subclasses can override methods to specialize the algorithm.
- The strategy pattern is typically applied when a family of algorithms implements a common interface. These algorithms can then be selected by clients.

As a concrete example, consider a sorting algorithm like quicksort. TWo of the key steps in quicksort are pivot selection and partitioning. Quicksort is a good example of a template method - subclasses can implement their own pivot selection algorithm, e.g., using randomized median finding or selecting an element at random, and their own partitioning method, e.t.c

Since there may be multiple ways in which to sort elements, e.g., student objects may be compared by GPA, major, name, and combinations thereof, it's natural to make the comparison operation used by the sorting algorithm an argument to quicksort. One way to do this is to pass quicksort an object that implements a compare method. These objects constitute an example of the strategy pattem, as do the objects implementing pivot selection and partitioning.

There are some other smaller differences between the two pattems. For example, in the template method pattern, the superclass algorithm may have "hooks" - calls to placeholder methods that can be overridden by subclasses to provide additional functionality. Sometimes a hook is not implemented, thereby forcing the subclasses to implement that functionality; some times it offers a "no-operation" or some baseline functionality. There is no analog to a hook in a strategy pattern.

### 2. Observer pattern

The observer pattem defines a one-to-many dependency between objects so that when one object changes state all its dependents are notified and updated automatically.

The observed object must implement the following methods.

- Register an observer.
- Remove an observer.
- Notify all currently registered observers.

The observer object must implement the following method.

- Update the observer. (Update is sometimes refeffed to as notify.)

As a concrete example, consider a service that logs user requests, and keeps track of the 10 most visited pages. There may be multiple client applications that use this information, e.g., a leaderboard display, ad placement algorithms, recorunendation system, etc. Instead of having the clients poll the service, the service, which is the observed object, provides clients with register and remove capabilities. As soon as its state changes, the service enumerates through registered observers, calling each observer's update method.

Though most readily understood in the context of a single program, where the observed and observer are objects, the observer pattern is also applicable to distributed computing.

### 3. Push vs Pull Observer pattern

In the observer pattem, subjects push information to their observers. There is another way to update data - the observers may "pull" the information they need from the subject. Compare and contrast these two approaches.

Solution: Both push and pull observer designs are valid and have tradeoffr depending on the needs of the project. With the push design, the subject notifies the observer that its data is ready and includes the relevant information that the observer is subscribing to, whereas with the pull design, it is the observer's job to retrieve that information from the subject.
The pull design places a heavier load on the observers, but it also allows the observer to query the subject only as often as is needed. One important consideration is that by the time the observer retrieves the information from the subject, the data could have changed. This could be a positive or negative result depending on the application. The pull design places less responsibility on the subject for tracking exactly which information the observer needs, as long as the subject knows
when to notify the observer. This design also requires that the subject make its data publicly accessible by the observers. This design would likely work better when the observers are running with varied frequency and it suits them best to get the data they need on demand.
The push design leaves all of the information transfer in the subject's control. The subject calls update for each observer and passes the relevant information along with this call. This design seems more object-oriented, because the subject is pushing its own data out, rather than making its data accessible for the observers to pull. It is also somewhat simpler and safer in that the subject always knows when the data is being pushed out to observers, so you don't have to worry about an observer pulling data in the middle of an update to the data, which would require synchronization.

### 4. Sigletons and Flyweights

The singleton pattern ensures a class has only one instance, and provides a global point of access to it. The flyweight pattern minimizes memory use by sharing as much data as possible with other similar objects. It is a way to use objects in large numbers when a simple repeated representation would use an unacceptable amount of memory.

A common example of a singleton is a logger. There may be many clients who want to listen to
the logged data (console, hle, messaging service, etc.), so all code should log to a single place.

A common example of a flyweight is string inteming-a method of storing only one copy of
each distinct string value. Inteming strings makes some string processing tasks more time- or
space-efficient at the cost of requiring more time when the string is created or intemed. The distinct
values are usually stored in a hash table. Since multiple clients may refer to the same flyweight
object for safety flyweights should be immutable.

There is a superficial similarity between singleton and flyweight both keep a single copy of an
object. There are several key differences between the two:

o Flyweights are used to save memory. Singletons are used to ensure all clients see the same
object.

o A singleton is used where there is a single shared object, e.g., a database corurection, server
configurations, a logger, etc. A flyweight is used where there is a family of shared objects,
e.g., objects describing character fonts, or nodes shared across multiple binary search trees.

o Flyweight objects are invariable immutable. Singleton objects are usually not immutablll e.g,
requests can be added to the database connection object.

o The singleton pattem is a creational pattern, whereas the flyweight is a structural pattem.
In summary a singleton is like a global variable, whereas a flyweight is like a pointer to a canonical
representation.

Sometimes, but not always, a singleton object is used to meate flyweights---dients ask the
singleton for an object with specified fields, and the singleton checks its intemal pool of flyweights
to see if one exists. If such an object already exists, it returns that, otherwise it creates a new
flyweight, add it to its pool, and then retums it. (L:r essence the singleton serves as a gateway to a
static factory.)

### 5. Adapters

The adapter pattern allows the interface of an existing class to be used from another interface. It is often used to make existing classes work with others without modifying their source code.

There are two ways to build an adapter: via subclassing (the class adapter pattern) and composition (the object adapter pattern). In the class adapter pattem, the adapter inherits both the interface that is expected and the interface that is pre-existing. In the object adapter pattern, the adapter contains an instance of the class it wraps and the adapter makes calls to the instance of the wrapped object.

Here are some remarks on the class adapter pattem.
o The class adapter pattern allows re-use of implementation code in both the target and adaptee.

This is an advantage in that the adapter doesn't have to contain boilerplate pass-throughs or

cut-and-paste reimplementation of code in either the target or the adaptee.
o The class adapter pattem has the disadvantages of inheritance (changes in base class may
cause unforeseen misbehaviors in derived classes, etc.). The disadvantages of inheritance are
made worse by the use of two base classes, which also precludes its use in languages like Java

(prior to |ava 1.8) that do not support multiple inheritance.
o The class adapter can be used in place of either the target or the adaptee. This can be advantage

if there is a need for a two-way adapter. The ability to substitute the adapter for adaptee can
be a disadvantage otherwise as it dilutes the purpose of the adapter and may lead to incorrect
behavior if the adapter is used in an unexpected manner.

o The class adapter allows details of the behavior of the adaptee to be changed by overriding
the adaptee's methods. Class adapters, as members of the class hierarchy, are tied to specific
adaptee and target concrete classes.

As a concrete example of an object adapter, suppose we have legacy code that returns objects of
type stack. Newer code expects inputs of type deque, which is more general than stack (but does not
subclass stack). We could create a new type, stack-adapter, which implements the deque methods,
and can be used anywhere deque is required. The stack-adapter class has a field of type stack-this
is referred to as object composition. It implements the deque methods with code that uses methods
on the composed stack object. Deque methods that are not supported by the underlying stack throw
unsupported operation exceptions. Lr this scenario, the stack-adapter is an example of an object
adapter.

Here are some conunents on the object adapter pattem.
o The object adapter pattern is "purer" in its approach to the purpose of making the adaptee

behave like the target. By implementing the interface of the target only, the object adapter is

only useful as a target.
o Use of an interface for the target allows the adaptee to be used in place of any prospective

target that is referenced by clients using that interface.
o Use of composition for the adaptee similarly allows flexibility in the choice of the concrete

classes. If adaptee is a concrete class, any subclass of adaptee will work equally well within
the object adapter pattem, If adaptee is an interface, any concrete class implementing that
interface will work.

o A disadvantage is that if target is not based on an interface, target and all its clients may need to change to allow the object adapter to be substituted.

### 6. Creational patterns

Explain what each of these creational pattems is: builder, static factory, factory method, and abstract factory.
Solution: The idea behind the builder pattem is to build a complex object in phases. It avoids mutability and inconsistent state by using an mutable inner class that has a build method that retums the desired object, Its key benefits are that it breaks down the construction process/ and can give names to steps. Compared to a constructor, it deals far better with optional parameters and
when the parameter list is very long.

A static factory is a function for construction of objects. Its key benefits are as follow: the
function's niune c€u:r make what it's doing much clearer compared to a call to a constructor. The
function is not obliged to create a new object-in particulaq, it can retum a flyweight. It can also
return a subtype that's more optimized, e.g., it can choose to construct an object that uses an integer
in place of a Boolean array if the array size is not more than the integer word size.

A factory method defines interface for creating an object, but lets subclasses decide which class
to instantiate. The classic example is a maze game with two modes-one with regular rooms, and
one with magic rooms. The program below uses a template method, as described in Problem 22.1
on Page 333, to combine the logic common to the two versions of the game.

 

A drawback of the factory method pattern is that it makes subclassing challenging.
An abstract factory provides an interface for creating families of related objects without sPecify-
ing their concrete classes. For example, a class DocumentCreator could provide interfaces to create

anumberof products,suchascreateletterO andcreateResumeO. Concreteimplementationsof
this class could choose to irnplement these products in different ways, e.9., with modern or classic
fonts, right-flush or right-ragged layout, etc. Client code gets a DocumentCreator object and calls
its factory methods. Use of this pattem makes it possible to interchange concrete implementations
without changing the code that uses them, even at runtime. The price for this flexibility is more

planning and upfront coding, as well as and code that may be harder to understand, because of the
added indirections.

## SOLID

[Python Open-closed Principle](https://www.pythontutorial.net/python-oop/python-open-closed-principle/)

# **OO Analysis and Design**

OO Analysis and Design is a structured method for analyzing and designing a system by applying object-oriented concepts. This design process consists of an investigation into the objects constituting the system. It starts by first identifying the objects of the system and then figuring out the interactions between various objects.

The process of OO analysis and design can be described as:

1. **Identifying the objects in a system**
2. **Defining relationships between objects**
3. **Establishing the interface of each object and,**
4. **Making a design, which can be converted to executables using OO languages.**

We need a standard method/tool to document all this information; for this purpose we use `UML`. UML can be considered as the successor of object-oriented (OO) analysis and design. UML is powerful enough to represent all the concepts that exist in object-oriented analysis and design. UML diagrams are a representation of object-oriented concepts only.

### **Tips for OOD Interview**

**Clarify the scenario, write out user cases**

Use case is a description of sequences of events that, taken together, lead to a system doing something useful. Who is going to use it and how they are going to use it. The system may be very simple or very complicated.

Special system requirements such as multi-threading, read or write oriented.

**Define objects**

Map identity to class: one scenario for one class, each core object in this scenario for one class.

Consider the relationships among classes: certain class must have unique instance, one object has many other objects (composition), one object is another object (inheritance).

Identify attributes for each class: change noun to variable and action to methods.

Use design patterns such that it can be reused in multiple applications.

## UML

![Screenshot 2021-11-08 at 05.31.51.png](_Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Screenshot_2021-11-08_at_05.31.51.png)

UML stands for **Unified Modeling Language** and is used to model the Object-Oriented Analysis of a software system. UML is a way of visualizing and documenting a software system by using a collection of diagrams, which helps engineers, businesspeople, and system architects understand the behavior and structure of the system being designed.

Benefits of using UML:

1. Helps develop a quick understanding of a software system.
2. UML modeling helps in breaking a complex system into discrete pieces that can be easily understood.
3. UML’s graphical notations can be used to communicate design decisions.
4. Since UML is independent of any specific platform or language or technology, it is easier to abstract out concepts.
5. It becomes easier to hand the system over to a new team.

**Types of UML Diagrams:** The current UML standards call for 14 different kinds of diagrams. These diagrams are organized into two distinct groups: structural diagrams and behavioral or interaction diagrams. As the names suggest, some UML diagrams analyze and depict the structure of a system or process, whereas others describe the behavior of the system, its actors, and its building components. The different types are broken down as follows:

**Structural UML diagrams**

- Class diagram
- Object diagram
- Package diagram
- Component diagram
- Composite structure diagram
- Deployment diagram
- Profile diagram

**Behavioral UML diagrams**

- Use case diagram
- Activity diagram
- Sequence diagram
- State diagram
- Communication diagram
- Interaction overview diagram
- Timing diagram

In this course, we will be focusing on the following UML diagrams:

- **Use Case Diagram:** Used to describe a set of user scenarios, this diagram, illustrates the functionality provided by the system.
- **Class Diagram:** Used to describe structure and behavior in the use cases, this diagram provides a conceptual model of the system in terms of entities and their relationships.
- **Activity Diagram:** Used to model the functional flow-of-control between two or more class objects.
- **Sequence Diagram:** Used to describe interactions among classes in terms of an exchange of messages over time.

### **Use Case Diagrams**

Use case diagrams describe a ***set of actions*** (called ***use cases***) that a system should or can perform in collaboration with one or more external users of the system (called ***actors***). Each use case should provide some observable and valuable result to the actors.

1. Use Case Diagrams describe the high-level functional behavior of the system.
2. It answers what system does from the user point of view.
3. Use case answers ‘What will the system do?’ and at the same time tells us ‘What will the system NOT do?’.

A use case illustrates a unit of **functionality provided by the system**. The primary purpose of the use case diagram is to help development teams visualize the functional requirements of a system, including the relationship of “actors” to the essential processes, as well as the relationships among different use cases.

To illustrate a use case on a use case diagram, we draw an oval in the middle of the diagram and put the name of the use case in the center of the oval. To show an actor (indicating a system user) on a use-case diagram, we draw a stick figure to the left or right of the diagram.

![Screenshot 2021-11-08 at 05.35.29.png](_Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Screenshot_2021-11-08_at_05.35.29.png)

The different components of the use case diagram are:

- **System boundary:** A system boundary defines the scope and limits of the system. It is shown as a rectangle that spans all use cases of the system.
- **Actors:** An actor is an entity who performs specific actions. These roles are the actual business roles of the users in a given system. An actor interacts with a use case of the system. For example, in a banking system, the customer is one of the actors.
- **Use Case:** Every business functionality is a potential use case. The use case should list the discrete business functionality specified in the problem statement.
- **Include:** Include relationship represents an invocation of one use case by another use case. From a coding perspective, it is like one function being called by another function.
- **Extend:** This relationship signifies that the extended use case will work exactly like the base use case, except that some new steps will be inserted in the extended use case

### Class diagrams

Class diagram is the backbone of object-oriented modeling - it shows how different entities (people, things, and data) relate to each other. In other words, it shows the static structures of the system.

A class diagram describes the **attributes** and **operations** of a class and also the **constraints** imposed on the system. Class diagrams are widely used in the modeling of object-oriented systems because they are **the only UML diagrams that can be mapped directly to object-oriented languages**.

The purpose of the class diagram can be summarized as:

1. Analysis and design of the static view of an application
2. To describe the responsibilities of a system
3. To provide a base for component and deployment diagrams and,
4. Forward and reverse engineering.

A class is depicted in the class diagram as a rectangle with three horizontal sections, as shown in the figure below. 

The upper section shows the class’s name (Flight), 
the middle section contains the properties of the class, and 
the lower section contains the class’s operations (or “methods”).

![Screenshot 2021-11-08 at 05.40.28.png](_Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Screenshot_2021-11-08_at_05.40.28.png)

**These are the different types of relationships between classes:**

**Association:** If two classes in a model need to communicate with each other, there must be a link between them. This link can be represented by an association. Associations can be represented in a class diagram by a line between these classes with an arrow indicating the navigation direction.

- By default, associations are always assumed to be bi-directional; this means that both classes are aware of each other and their relationship. In the diagram below, the association between Pilot and FlightInstance is bi-directional, as both classes know each other.
- By contrast, in a uni-directional association, two classes are related - but only one class knows that the relationship exists. In the below example, only Flight class knows about Aircraft; hence it is a uni-directional association

**Multiplicity** Multiplicity indicates how many instances of a class participate in the relationship. It is a constraint that specifies the range of permitted cardinalities between two classes. For example, in the diagram below, one FlightInstance will have two Pilots, while a Pilot can have many FlightInstances. A ranged multiplicity can be expressed as “`0…*`” which means “zero to many" or as “`2…4`” which means “two to four”.

We can indicate the multiplicity of an association by adding multiplicity adornments to the line denoting the association. The below diagram, demonstrates that a FlightInstance has exactly two Pilots but a Pilot can have many FlightInstances.

![Screenshot 2021-11-08 at 05.42.30.png](_Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Screenshot_2021-11-08_at_05.42.30.png)

**Aggregation:** Aggregation is a special type of association used to model a “whole to its parts” relationship. In a basic aggregation relationship, the lifecycle of a PART class is independent of the WHOLE class’s lifecycle. In other words, aggregation implies a relationship where the child can exist independently of the parent. In the above diagram, Aircraft can exist without Airline.

**Composition:** The composition aggregation relationship is just another form of the aggregation relationship, but the child class’s instance lifecycle is dependent on the parent class’s instance lifecycle. In other words, Composition implies a relationship where the child cannot exist independent of the parent. In the above example, WeeklySchedule is composed in Flight which means when Flight lifecycle ends, WeeklySchedule automatically gets destroyed.

**Generalization:** Generalization is the mechanism for combining similar classes of objects into a single, more general class. Generalization identifies commonalities among a set of entities. In the above diagram, Crew, Pilot, and Admin, all are Person.

**Dependency:** A dependency relationship is a relationship in which one class, the client, uses or depends on another class, the supplier. In the above diagram, FlightReservation depends on Payment.

**Abstract class:** An abstract class is identified by specifying its name in *italics*. In the above diagram, both Person and Account classes are abstract classes.

![Screenshot 2021-11-08 at 05.46.37.png](_Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Screenshot_2021-11-08_at_05.46.37.png)

### **Sequence diagram**

![Screenshot 2021-11-08 at 05.48.58.png](_Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Screenshot_2021-11-08_at_05.48.58.png)

Sequence diagrams describe interactions among classes in terms of an exchange of messages over time and are used to explore the logic of complex operations, functions or procedures. In this diagram, the sequence of interactions between the objects is represented in a step-by-step manner.

Sequence diagrams show a detailed flow for a specific use case or even just part of a particular use case. They are almost self-explanatory; they show the calls between the different objects in their sequence and can explain, at a detailed level, different calls to various objects.

A sequence diagram has two dimensions: The vertical dimension shows the sequence of messages in the chronological order that they occur; the horizontal dimension shows the object instances to which the messages are sent.

A sequence diagram is straightforward to draw. Across the top of your diagram, identify the class instances (objects) by putting each class instance inside a box (see above figure). If a class instance sends a message to another class instance, draw a line with an open arrowhead pointing to the receiving class instance and place the name of the message above the line. Optionally, for important messages, you can draw a dotted line with an arrowhead pointing back to the originating class instance; label the returned value above the dotted line.

### **Activity Diagrams**

We use Activity Diagrams to illustrate the flow of control in a system. An activity diagram shows the flow of control for a system functionality; it emphasizes the condition of flow and the sequence in which it happens. We can also use an activity diagram to refer to the steps involved in the execution of a use case.

Activity diagrams illustrate the dynamic nature of a system by modeling the flow of control from activity to activity. An activity represents an operation on some class in the system that results in a change in the state of the system. Typically, activity diagrams are used to model workflow or business processes and internal operations.

Following is an activity diagram for a user performing online shopping:

Sample activity diagram for online shopping

![Sample activity diagram for online shopping](_Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Screenshot_2021-11-08_at_05.54.27.png)

Sample activity diagram for online shopping

**What is the difference between Activity diagram and Sequence diagram?**

**Activity diagram** captures the process flow. It is used for functional modeling. A functional model represents the flow of values from external inputs, through operations and internal data stores, to external outputs.**Sequence diagram** tracks the interaction between the objects. It is used for dynamic modeling, which is represented by tracking states, transitions between states, and the events that trigger these transitions.

---

# Design patterns

[Design Patterns and Refactoring](https://sourcemaking.com/design_patterns)

[The 3 Types of Design Patterns All Developers Should Know (with code examples of each)](https://www.freecodecamp.org/news/the-basic-design-patterns-all-developers-need-to-know/)

[The 7 Most Important Software Design Patterns](https://medium.com/educative/the-7-most-important-software-design-patterns-d60e546afb0e)

[5 Design Patterns Every Engineer Should Know](https://youtu.be/FLmBqI3IKMA)

Examples:

- Singleton
- Observer Pattern (Pub/Sub)
- Facade
- Bridge/Adapter Pattern
- Strategy Pattern

## **Creational Patterns**

## **Structural Patterns**

## **Behavioral Patterns**

---

# **Object Oriented Design Case Studies**

```python
""" 
- System requirements
- Use case diagrams
		- Actors
		- Use cases
		- Use case diagrams
- Class diagrams
		- Main classes
		- Class diagrams
- Activity diagrams
- Code

"""
```

[Amazon System Design Interview: Design Parking Garage](https://youtu.be/NtMvNh0WFVM)

## **Design a Library Management System**

[**Design a Library Management System**](_Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Design%20a%20Library%20Management%20System%20d6f0c5b09f314a80870d7c8f582de630.md)

- Solution

## **Design an ATM**

[**Design an ATM**](_Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Design%20an%20ATM%20f65942ad586d4fa087b87f4a17299605.md)

- Solution

## Design a parking lot

[**Design a Parking Lot**](_Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Design%20a%20Parking%20Lot%201fb87f1104eb4ae99f37d693aaaf7b06.md)

- Solution

xx