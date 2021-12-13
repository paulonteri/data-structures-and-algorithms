# Hashtables & Hashsets

[Hash Tables](https://emre.me/data-structures/hash-tables/)

A data structure that provides fast insertion, deletion, and lookup of key/value pairs.

Under the hood, a hash table uses a **dynamic array** of **linked lists** to efficiently store key/value pairs. 
When inserting a key/value pair, a hash function first maps the key, which is typically a string (or any data that can be hashed, depending on the implementation of the hash table), to an integer value and, by extension, to an index in the underlying dynamic array. Then, the value associated with the key is added to the linked list stored at that index in the dynamic array, and a reference to the key is also stored with the value

**Iteration**

Iteration over a key-value collection yields the keys. 
To iterate over the key-value pairs, iterate over `.items()`; 
to iterate over values use `.values()`;
the `.keys()` method returns an iterator to the keys.

**Check for keys**

```python
days_set = {"Mon", "Tue", "Wed"}
print("Mon" in days_set) # True
print("Sun" in days_set) # False

days_dict = {"Mon": 1, "Tue": 2, "Wed": 3}
print("Mon" in days_dict) # True
print("Sun" in days_dict) # False
```

**Deleting items**

```python
this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

this_dict.pop("model")

foo = {42,41}
foo.remove(42)
# foo.remove(42) -> **throws error**
foo.discard(41)
foo.discard(41) # -> **no error .discard()**
```

### Examples

- Invalid Transactions **
    - Record all transactions done at a particular time. Recording the person and the location.Example:
        
        ```latex
        {time: {person: {location}, person2: {location1, location2}}, time: {person: {location}}}
        ```
        
        ```latex
        ['alice,20,800,mtv', 'bob,50,1200,mtv', 'bob,20,100,beijing']
        
        {
        20: {'alice': {'mtv'}, 'bob': {'beijing'}},
        50: {'bob': {'mtv'}}
        }
        ```
        
    - For each transaction, check if the amount is invalid - and add it to the invalid transactions if so.
    - For each transaction, go through invalid times (+-60), check if a transaction by the same person happened in a different city - and add it to the invalid transactions if so.
    
    ```python
    from collections import defaultdict
    
    """ 
    https://www.notion.so/paulonteri/Hashtables-Hashsets-220d9f0e409044c58ec6c2b0e7fe0ab5#cf22995975274881a28b544b0fce4716
    """
    
    class Solution(object):
        def invalidTransactions(self, transactions):
            """ 
            - Record all transactions done at a particular time. Recording the person and the location. Example:
                `['alice,20,800,mtv','bob,50,1200,mtv','bob,20,100,beijing']` :\n
                ` 
                {   
                20: {'alice': {'mtv'}, 'bob': {'beijing'}}, 
                50: {'bob': {'mtv'}}
                } 
                ` \n
                `{time: {person: {location}, person2: {location1, location2}}, time: {person: {location}}}`
            - For each transaction, check if the amount is invalid - and add it to the invalid transactions if so.
            - For each transaction, go through invalid times (+-60), check if a transaction by the same person happened
                in a different city - and add it to the invalid transactions if so.
            """
            invalid = []
    
            # Record all transactions done at a particular time
            #   including the person and the location.
            transaction_time = defaultdict(dict)
            for transaction in transactions:
                name, str_time, amount, city = transaction.split(",")
                time = int(str_time)
    
                if name not in transaction_time[time]:
                    transaction_time[time][name] = {city, }
                else:
                    transaction_time[time][name].add(city)
    
            for transaction in transactions:
                name, str_time, amount, city = transaction.split(",")
                time = int(str_time)
    
                # # check amount
                if int(amount) > 1000:
                    invalid.append(transaction)
                    continue
    
                # # check if person did transaction within 60 minutes in a different city
                for inv_time in range(time-60, time+61):
                    if inv_time not in transaction_time:
                        continue
                    if name not in transaction_time[inv_time]:
                        continue
    
                    trans_by_name_at_time = transaction_time[inv_time][name]
    
                    # check if transactions were done in a different city
                    if city not in trans_by_name_at_time or len(trans_by_name_at_time) > 1:
                        invalid.append(transaction)
                        break
    
            return invalid
    ```
    
- Longest Substring with K Distinct Characters
- Dot Product of Two Sparse Vectors
    
    ```python
    """ 
    Dot Product of Two Sparse Vectors:
    
    Given two sparse vectors, compute their dot product.
    Implement class SparseVector:
    SparseVector(nums) Initializes the object with the vector nums
    dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
    A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.
    
    Follow up: What if only one of the vectors is sparse?
    
    Example 1:
        Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
        Output: 8
        Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
        v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
    Example 2:
        Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
        Output: 0
        Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
        v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0
    Example 3:
        Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
        Output: 6
    
    https://leetcode.com/problems/dot-product-of-two-sparse-vectors
    """
    
    class SparseVector:
        def __init__(self, nums):
            self.non_zero = {}
            for idx, num in enumerate(nums):
                if num != 0:
                    self.non_zero[idx] = num
    
        # Return the dotProduct of two sparse vectors
        def dotProduct(self, vec: 'SparseVector'):
            total = 0
            for idx in self.non_zero:
                if idx in vec.non_zero:
                    total += self.non_zero[idx] * vec.non_zero[idx]
    
            return total
    
    # Your SparseVector object will be instantiated and called as such:
    # v1 = SparseVector(nums1)
    # v2 = SparseVector(nums2)
    # ans = v1.dotProduct(v2)
    ```
    

- Random Pick Index *
    
    ```python
    """ 
    398. Random Pick Index
    
    Given an integer array nums with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.
    Implement the Solution class:
        Solution(int[] nums) Initializes the object with the array nums.
        int pick(int target) Picks a random index i from nums where nums[i] == target. 
            If there are multiple valid i's, then each index should have an equal probability of returning.
     
    
    Example 1:
        Input
            ["Solution", "pick", "pick", "pick"]
            [[[1, 2, 3, 3, 3]], [3], [1], [3]]
        Output
            [null, 4, 0, 2]
        Explanation
            Solution solution = new Solution([1, 2, 3, 3, 3]);
            solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
            solution.pick(1); // It should return 0. Since in the array only nums[0] is equal to 1.
            solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
    
    https://leetcode.com/problems/random-pick-index
    """
    
    from typing import List
    import collections
    import random
    
    class Solution:
    
        def __init__(self, nums):
            self.store = collections.defaultdict(list)
            for idx, num in enumerate(nums):
                self.store[num].append(idx)
    
        def pick(self, target: int):
            indices = self.store[target]
            return indices[random.randint(0, len(indices)-1)]
    
    # Your Solution object will be instantiated and called as such:
    # obj = Solution(nums)
    # param_1 = obj.pick(target)
    
    # Other solution https://leetcode.com/problems/random-pick-index/discuss/88153/Python-reservoir-sampling-solution.
    
    class Solution:
    
        def __init__(self, nums: List[int]):
            self.nums = nums
    
        def pick(self, target: int):
            """ 
            Reservoir sampling
            - at every valid index, try to see whether the current index can be picked
            """
            count = 0
            idx = 0
            for i in range(len(self.nums)):
                if self.nums[i] == target:
                    count += 1
                    if random.randint(0, count - 1) == 0:
                        idx = i
            return idx
    ```
    

---

### How to store an class in a hashtable

```python
# it can also work without the __hash__ function lol
class Node:
    def __init__(self, x):
        self.val = int(x)

x = Node(1)
y = Node(2)
z = Node(2)

store = {x: 1}
store[y] = 2
store[z] = 2

print(store.keys())
# dict_keys([<__main__.Node object at 0x7fe0482a5f50>, <__main__.Node object at 0x7fe0482a5fd0>, <__main__.Node object at 0x7fe0482a8050>])
```

### Sorting by keys/value

```python
store = {'Zebra':2, 'Apple':3, 'Honey Badger':1 }

print(sorted(store)) # ['Apple', 'Honey Badger', 'Zebra']
print(sorted(store, reverse=True)) # ['Zebra', 'Honey Badger', 'Apple']
print(sorted(store, key=lambda x: store[x])) # ['Honey Badger', 'Zebra', 'Apple']
```

## hashtable vs hashset vs hashmap python

HashTable == HashMap == Dictionary

Hashset == Set

## You can compare hashtables

```python
>>> x = {'a': 1, 'e': 1, 'b': 1}
>>> y = {'e': 1, 'a': 1, 'b': 1}
>>> x == y
True
```

### Examples:

---

# Hash table libraries

There are multiple hash table-based data structures commonly used in `set`, `dict`, `collections.defaultdict`, `collections.OrderedDict` and `collections.Counter`.

The difference between `set` and the other three is that is set simply stores keys, whereas the others store key-value pairs. All have the property that they do not allow for duplicate keys.

## `collections.defaultdict`

In a `dict`, accessing value associated with a key that is not present leads to a KeyError exception. However, a `collections.defaultdict` returns the default value of the type that was specified when the collection was instantiated.

```python
from collections import defaultdict

list_dict = defaultdict(list)
print(list_dict['key']) # []
list_dict['key'].append(1) # adding constant 1 to the list
print(list_dict['key']) # [1] -> list containing the constant [1]

int_dict = defaultdict(int)
print(int_dict['key2']) # 0
int_dict['key2'] += 1 
print(int_dict['key2']) # 1

ice_cream = defaultdict(lambda: 'Vanilla')
ice_cream['Sarah'] = 'Chunky Monkey'
ice_cream['Abdul'] = 'Butter Pecan'
print(ice_cream['Sarah']) # Chunky Monkey
print(ice_cream['Joe']) # Vanilla
print(ice_cream.values()) # dict_values(['Chunky Monkey', 'Butter Pecan', 'Vanilla'])

# Works like normal dict
for key in list_dict:
    print(key, list_dict[key])
```

when it comes to build hash's hash's hash kind of jobs, [`defaultdict` is really handy](https://leetcode.com/problems/invalid-transactions/discuss/1570056/Using-HashTableHashMap-or-Comments-added).

The behavior of `defaultdict` can be easily mimicked using `dict.setdefault` instead of `d[key]` in every call. 

In other words, the code:

```python
from collections import defaultdict

d = defaultdict(list)

print(d['key'])                        # empty list []
d['key'].append(1)                     # adding constant 1 to the list
print(d['key'])                        # list containing the constant [1]
```

is equivalent to:

```python
d = dict()

print(d.setdefault('key', list()))     # empty list []
d.setdefault('key', list()).append(1)  # adding constant 1 to the list
print(d.setdefault('key', list()))     # list containing the constant [1]
```

- Invalid Transactions **
    - Record all transactions done at a particular time. Recording the person and the location.Example:
        
        ```latex
        {time: {person: {location}, person2: {location1, location2}}, time: {person: {location}}}
        ```
        
        ```latex
        ['alice,20,800,mtv', 'bob,50,1200,mtv', 'bob,20,100,beijing']
        
        {
        20: {'alice': {'mtv'}, 'bob': {'beijing'}},
        50: {'bob': {'mtv'}}
        }
        ```
        
    - For each transaction, check if the amount is invalid - and add it to the invalid transactions if so.
    - For each transaction, go through invalid times (+-60), check if a transaction by the same person happened in a different city - and add it to the invalid transactions if so.
    
    ```python
    from collections import defaultdict
    
    """ 
    https://www.notion.so/paulonteri/Hashtables-Hashsets-220d9f0e409044c58ec6c2b0e7fe0ab5#cf22995975274881a28b544b0fce4716
    """
    
    class Solution(object):
        def invalidTransactions(self, transactions):
            """ 
            - Record all transactions done at a particular time. Recording the person and the location. Example:
                `['alice,20,800,mtv','bob,50,1200,mtv','bob,20,100,beijing']` :\n
                ` 
                {   
                20: {'alice': {'mtv'}, 'bob': {'beijing'}}, 
                50: {'bob': {'mtv'}}
                } 
                ` \n
                `{time: {person: {location}, person2: {location1, location2}}, time: {person: {location}}}`
            - For each transaction, check if the amount is invalid - and add it to the invalid transactions if so.
            - For each transaction, go through invalid times (+-60), check if a transaction by the same person happened
                in a different city - and add it to the invalid transactions if so.
            """
            invalid = []
    
            # Record all transactions done at a particular time
            #   including the person and the location.
            transaction_time = defaultdict(dict)
            for transaction in transactions:
                name, str_time, amount, city = transaction.split(",")
                time = int(str_time)
    
                if name not in transaction_time[time]:
                    transaction_time[time][name] = {city, }
                else:
                    transaction_time[time][name].add(city)
    
            for transaction in transactions:
                name, str_time, amount, city = transaction.split(",")
                time = int(str_time)
    
                # # check amount
                if int(amount) > 1000:
                    invalid.append(transaction)
                    continue
    
                # # check if person did transaction within 60 minutes in a different city
                for inv_time in range(time-60, time+61):
                    if inv_time not in transaction_time:
                        continue
                    if name not in transaction_time[inv_time]:
                        continue
    
                    trans_by_name_at_time = transaction_time[inv_time][name]
    
                    # check if transactions were done in a different city
                    if city not in trans_by_name_at_time or len(trans_by_name_at_time) > 1:
                        invalid.append(transaction)
                        break
    
            return invalid
    ```
    

## `collections.OrderedDict`

An **OrderedDict** is a dictionary subclass that remembers the order that keys were first inserted. The only difference between **`dict()`** and `collections.OrderedDict()` is that:

OrderedDict **preserves the order** in which the keys are inserted. A regular dict doesn’t track the insertion order, and iterating it gives the values in an arbitrary order. By contrast, the order the items are inserted is remembered by OrderedDict.

<aside>
💡 `collections.OrderedDict()` can be used as a `stack` with the help of `.popitem()` and a queue with `.popitem(last=False)`

</aside>

```python
from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

print(od.keys()) # odict_keys(['a', 'b', 'c', 'd'])
od.popitem(last=True)
print(od.keys()) # odict_keys(['a', 'b', 'c'])
```

## `sortedcontainers.SortedDict`

## `set`

A set is an unordered collection of items. Every set element is unique (no duplicates) and must be immutable (cannot be changed).

However, a set itself is mutable. We can add or remove items from it.

Sets can also be used to perform mathematical set operations like union, intersection, symmetric difference, etc.

A set is a collection that is both **unordered** and **unindexed**.

***Simple operations***

The `remove()` method raises an error when the specified element doesn’t exist in the given set, however, the `discard()` method doesn’t raise any error if the specified element is not present in the set and the set remains unchanged.

### Examples

```python
foo = set()

foo.add(42)
foo.remove(42)
# foo.remove(42) -> **throws error**
foo.add(41)
foo.discard(41)
foo.discard(41) # -> **no error**
foo.add(43)
foo.add(43)
foo.add(44)
print(foo)  # {43, 44}

bar = {1, 2, 2, 2, 3, 3} 
print(bar) # {1, 2, 3}

# empty set
print(set())
# from string
print(set('Python'))  # {'n', 'P', 'o', 't', 'h', 'y'}
# from list
print(set(['a', 'e', 'i', 'o', 'u']))  # {'a', 'o', 'e', 'i', 'u'}
# from set
print(set({'a', 'e', 'i', 'o', 'u'}))  # {'u', 'i', 'a', 'o', 'e'}
# from dictionary
# {'u', 'i', 'a', 'o', 'e'}
print(set({'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}))
# from frozen set
frozen_set = frozenset(('a', 'e', 'i', 'o', 'u'))  # {'u', 'i', 'a', 'o', 'e'}
print(set(frozen_set))
```

***Advanced operations***

**Union of Sets**

The union operation on two sets produces a new set containing all the distinct elements from both the sets. In the below example the element “Wed” is present in both the sets.

```python
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA|DaysB
print(AllDays) # set(['Wed', 'Fri', 'Tue', 'Mon', 'Thu', 'Sat'])
```

**Intersection of Sets**

The intersection operation on two sets produces a new set containing only the common elements from both the sets. In the below example the element “Wed” is present in both the sets.

```python
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA & DaysB
print(AllDays) # set(['Wed'])
```

**Difference of Sets**

The difference operation on two sets produces a new set containing only the elements from the first set and none from the second set. In the below example the element “Wed” is present in both the sets so it will not be found in the result set.

```python
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA - DaysB
print(AllDays) # set(['Mon', 'Tue'])
```

**Compare Sets**

We can check if a given set is a subset or superset of another set. The result is True or False depending on the elements present in the sets.

```python
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
print(DaysA <= DaysB) # True
print(DaysB >= DaysA) # True
```

## `collections.Counter`

A `collections.Counter` is used for counting the number of occurrences of keys, with a number of setlike operations.
Missing keys will return a count of 0.

```python
import collections

list1 = ['x', 'y', 'z', 'x', 'x', 'x', 'y', 'z']
x = collections.Counter(list1)
print(x)  # Counter({'x': 4, 'y': 2, 'z': 2})
x['a'] -= 1
print(x['a']) # -1

foo = collections.Counter(a=3, b=1)
bar = collections.Counter(a=1, b=2)

# add two counters together
print(foo+bar)  # Counter({'a': 4, 'b': 3})
# subract -> ignores negative
print(foo - bar)  # Counter({'a': 2})
# intersection:  min(foo[x], bar[x]),
print(foo & bar)  # Counter({'a': 1, 'b': 1})
# union: max(foo[x], bar[x]),
print(foo | bar)  # ({'a': 3, 'b': 2})
```

```python
"""
>>> c
Counter({'5': 2, '3': 2, '.': 1, 'e': 1, '9': 1})

>>> c['E']
0

>>> 'E' in c
False

"""
```