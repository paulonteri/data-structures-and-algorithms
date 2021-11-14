# _Object-Oriented Analysis and Design

[Grokking the Object Oriented Design Interview - Learn Interactively](https://www.educative.io/courses/grokking-the-object-oriented-design-interview)

[Python Object Oriented Programming](https://www.programiz.com/python-programming/object-oriented-programming)

[GitHub - tssovi/grokking-the-object-oriented-design-interview](https://github.com/tssovi/grokking-the-object-oriented-design-interview)

# Introduction

## Examples

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
    

Object-oriented programming (OOP) is a style of programming that focuses on using objects to design and build applications. Contrary to procedure-oriented programming where programs are designed as blocks of statements to manipulate data, OOP organises the program to **combine data and functionality** and wrap it inside something called an “Object”.

Basic concepts of OOP:

- **Objects:** Objects **represent a real-world entity** and the basic building block of OOP. For example, an Online Shopping System will have objects such as shopping cart, customer, product item, etc.
- **Class:** Class is the prototype or **blueprint of an object**. It is a template definition of the attributes and methods of an object. For example, in the Online Shopping System, the Customer object will have attributes like shipping address, credit card, etc., and methods for placing an order, cancelling an order, etc.

![Screenshot 2021-11-08 at 05.22.57.png](_Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Screenshot_2021-11-08_at_05.22.57.png)

The four principles of object-oriented programming are encapsulation, abstraction, inheritance, and polymorphism.

- **[Encapsulation]():** Encapsulation is the mechanism of binding the data together and **hiding it from the outside world**. Encapsulation is achieved when each object keeps its state private so that other objects don’t have direct access to its state. Instead, they can access this state only through a set of public functions.
- **[Abstraction]():** Abstraction can be thought of as the natural extension of encapsulation. It means **hiding all but the relevant data** about an object in order to reduce the complexity of the system. In a large system, objects talk to each other, which makes it difficult to maintain a large codebase; abstraction helps by hiding internal implementation details of objects and **only revealing operations that are relevant to other objects**.
- **[Inheritance]():** Inheritance is the mechanism of creating new classes from existing ones.
- **[Polymorphism]():** Polymorphism (from Greek, meaning “many forms”) is the ability of an object to take **different forms and thus, depending upon the context, to respond to the same message in different ways**. Take the example of a chess game; a chess piece can take many forms, like bishop, castle, or knight and all these pieces will respond differently to the ‘move’ message

# Theory

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

The `nonlocal` keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function.

Use the keyword `nonlocal` to declare that the variable is not local.

```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]):
        preorder_pos = 0
        inorder_idxs = {val: idx for idx, val in enumerate(inorder)}

        def helper(preorder: List[int], inorder: List[int], inorder_left, inorder_right):
            nonlocal preorder_pos
```

## Python Operator Overloading

## TODO: Abstract Base Class *

[Abstract Base Class (abc) in Python - GeeksforGeeks](https://www.geeksforgeeks.org/abstract-base-class-abc-in-python/)

---

# **OO Analysis and Design**

OO Analysis and Design is a structured method for analyzing and designing a system by applying object-oriented concepts. This design process consists of an investigation into the objects constituting the system. It starts by first identifying the objects of the system and then figuring out the interactions between various objects.

The process of OO analysis and design can be described as:

1. **Identifying the objects in a system**
2. **Defining relationships between objects**
3. **Establishing the interface of each object and,**
4. **Making a design, which can be converted to executables using OO languages.**

We need a standard method/tool to document all this information; for this purpose we use `UML`. UML can be considered as the successor of object-oriented (OO) analysis and design. UML is powerful enough to represent all the concepts that exist in object-oriented analysis and design. UML diagrams are a representation of object-oriented concepts only.

## UML

![Screenshot 2021-11-08 at 05.31.51.png](_Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Screenshot_2021-11-08_at_05.31.51.png)

UML stands for Unified Modeling Language and is used to model the Object-Oriented Analysis of a software system. UML is a way of visualizing and documenting a software system by using a collection of diagrams, which helps engineers, businesspeople, and system architects understand the behavior and structure of the system being designed.

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