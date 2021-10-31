# Data Structures and Algorithms

![Data%20Structures%20and%20Algorithms%20feab1cb55ae74c6f842a741c790a6f6c/Screenshot_2021-07-21_at_14.30.56.png](Data%20Structures%20and%20Algorithms%20feab1cb55ae74c6f842a741c790a6f6c/Screenshot_2021-07-21_at_14.30.56.png)

[Introduction | Tech Interview Handbook](https://techinterviewhandbook.org/algorithms/algorithms-introduction/)

[Coding Interview Prep](https://lei-d.gitbook.io/leetcode/)

[Comprehensive Data Structure and Algorithm Study Guide - LeetCode Discuss](https://leetcode.com/discuss/general-discussion/494279/comprehensive-data-structure-and-algorithm-study-guide)

[Posts by Category](https://emre.me/categories/#coding-patterns)

[Data Structure Visualization](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html)

[Introduction](https://labuladong.gitbook.io/algo-en/)

[How To Find a Solution](https://www.topcoder.com/thrive/articles/How%20To%20Find%20a%20Solution)

[Python Functions](https://www.programiz.com/python-programming/function)

Data structures and Algorithms (patterns):

- Binary search: BS can be used in so many different situations!
- Leap year, GCD, LCM, isPrime, prime finding, prime factorization
- Bit manipulation
- Reservoir sampling
- 2 pointer strategy and sliding window
- cumulative sum, prefix sum (1d, 2d, 3d)
- Sorting: selection sort, quick sort, quick select, insertion sort (with binary search optimization), merge sort, heap sort, radix sort, counting sort, bucket sort
- String strategies: rabin-karp, KMP, Boyer-Moore
- Graph: Dijkstra, Bellman-Ford, Union find, Kruskal, Prim, Floyd-Warshall, Tarjan, DFS, BFS, Ford Fulkerson & Edmond (Min cut max flow), Hamiltonion path (with bitmasking), Eulerian cycle, Topological sorting
- DFS: backtracking
- Monotonically increasing stack, queue, etc.
- DP: Top-down using recursion and memoization, Bottom up using iteration and tabulation
- Classic DP patterns: LCS, LIS, LIS (strictly increasing), Equal sum partition
- BIT: binary indexed tree/sedgwick tree
- Interval trees
- Tree: inorder, preorder, postorder traversal: iterative and recursive, morris traversal to do those 3 in O(1) space
- Binary search trees (BSTs), heaps, splay trees, red-black trees, skip list, avl tree

### Tools:

- Grokking the coding interview
- [AgoExpert](https://youtu.be/3OmEx-JRI74) ?

### Tips:

- [Non-Technical Tip: Offers from Google and Amazon](https://leetcode.com/discuss/general-discussion/897688/lay-up-questions-non-technical-tip)
- [What To Do If You're Stuck In A Coding Interview](https://youtu.be/WLBcmyNaeKc)
- [Software Engineering Job Tips From A Google Recruiter](https://youtu.be/Yfs4kCG-nNA) - How to contact recruiter? etc.
- [How to network recruiters on LinkedIn](https://www.recruitinginyogapants.com/2019/09/how-to-network-with-recruiters-on.html)
- [How To Ace The Google Coding Interview](https://youtu.be/-QxUp8MwbWw) - Complete Guide
- [14 Patterns to Ace Any Coding Interview Question](https://hackernoon.com/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed)
- [The Ultimate Strategy to Preparing for a Coding Interview](https://medium.com/better-programming/the-ultimate-strategy-to-preparing-for-the-coding-interview-ee9f7eb439f3)
- [Important and Useful links from all over the LeetCode](https://leetcode.com/discuss/general-discussion/665604/important-and-useful-links-from-all-over-the-leetcode)
- [From 0 to clearing Uber/Apple/Amazon/LinkedIn/Google](https://leetcode.com/discuss/career/216554/from-0-to-clearing-uberappleamazonlinkedingoogle)
- [Twitter Engineer shares 5 tips on how to ace...](https://thenextweb.com/syndication/2020/11/03/twitter-engineer-shares-5-tips-on-how-to-ace-coding-interviews/)
- [Algorithm of an algorithm](https://medium.com/outco/the-algorithm-of-an-algorithm-28043fe47b51)
- [How to Get Unstuck in Technical Interviews](https://blog.pramp.com/how-to-get-unstuck-in-technical-interviews-93d4632ef996)
- [MOHSIN ALI](http://www.mohsinali.net/)
- [Technical Interviews: the 8 Most Common Mistakes Programmers Make](https://blog.pramp.com/top-8-mistakes-in-technical-interviews-according-to-data-27d2572bda1f)

[https://www.topcoder.com/thrive/articles/Greedy is Good](https://www.topcoder.com/thrive/articles/Greedy%20is%20Good)

[https://www.topcoder.com/thrive/articles/An Introduction to Recursion Part Two](https://www.topcoder.com/thrive/articles/An%20Introduction%20to%20Recursion%20Part%20Two)

Data structures in 5 min: 

[https://www.youtube.com/playlist?list=PLlipSLnrfrUlclWAcvmyxcn6R7tzwALhM](https://www.youtube.com/playlist?list=PLlipSLnrfrUlclWAcvmyxcn6R7tzwALhM)

### **Quick Notes:**

- **Stack (LIFO):**
    
    ```python
    myStack = []
    
    myStack.append('a')
    myStack.append('b')
    myStack.append('c')
    
    print(myStack)
    # ['a', 'b', 'c']
    
    # # pop() -> removes the last element
    # # works exactly like stack
    
    print(myStack.pop())
    # 'c'
    print(myStack.pop())
    # 'b'
    print(myStack.pop())
    # 'a'
    ```
    
- **Queue (FIFO):**
    
    ```python
    queue = []
    
    queue.append('a') 
    queue.append('b') 
    queue.append('c')
    
    print(queue)
    # ['a', 'b', 'c']
    
    # # pop(0) -> removes the first element
    # # works exactly like queue
    
    print(queue.pop(0)) 
    # 'a'
    print(queue.pop(0)) 
    # 'b'
    print(queue.pop(0))
    # 'c'
    ```
    

- **Heap & Priority Queue**:
    
    A Heap is a tree-based data structure in which all the nodes of the tree are in a specific order (*Max Heap & Min Heap*). Heaps are commonly used to implement priority queues. They’re the most popular concrete data structure for implementing the priority queue abstract data structure.
    
    Priority queues are commonly used for optimizing task execution, in which the goal is to work on the task with the highest priority and supports three operations:
    
    1. *is_empty:* checks whether the queue is empty.
    2. *add_element:* adds an element to the queue.
    3. *pop_element:* pops the element with the highest priority.
    
    The python `heapq` uses the smallest element has the highest priority. i.e [1,2,3,4,5,6]: in thet order.
    
    ```python
    import heapq
    
    # create heap from list
    a = [3, 5, 1, 2, 6, 8, 7]
    heapq.heapify(a)
    print(a)
    # [1, 2, 3, 5, 6, 8, 7]
    
    ```
    
    .
    
    ```python
    import heapq
    
    #####
    #####
    # # MIN HEAP IMPLEMENTATION
    heap =  [2, 5, 3, 7, 6, 8, 15, 10, 17, 11]
    heapq.heappush(heap, 4)
    
    print(heap)
    # [2, 4, 3, 7, 5, 8, 15, 10, 17, 11, 6]
    
    print(heapq.heappop(heap))
    # 2
    print(heapq.heappop(heap))
    # 3
    print(heapq.heappop(heap))
    # 4
    
    #####
    #####
    # # MAX HEAP IMPLEMENTATION 
    
    print(heap)
    # [5, 7, 6, 10, 11, 8, 15, 17]
    
    # not available
    # heapq._heappush_max(heap, 2)
    
    heapq._heapify_max(heap)
    print(heap)
    # [17, 11, 15, 10, 5, 8, 6, 7]
    
    print(heapq._heappop_max(heap))
    # 17
    print(heapq._heappop_max(heap))
    # 15
    print(heapq._heappop_max(heap))
    # 11
    ```
    
- [Tree traversals](https://medium.com/leetcode-patterns/leetcode-pattern-0-iterative-traversals-on-trees-d373568eb0ec):
    - Preorder → **n**lr (root, left, right)
    - Inorder → n**l**r (left, root, right): can use *stack*
    - Postorder → nl**r**
    - level order traversal: can be done using queue
    - DFS → diving as deep as possible before coming back to take a dive again: can use stack
    - `stack` for DFS, imagine a vertical flow: seen earliest will be come for later
    - `queue` for BFS, horizontal flow
- **Array Enumerate:**
    - index, value
    - 0, "apple"
- Types of binary trees:
    
    ![Data%20Structures%20and%20Algorithms%20feab1cb55ae74c6f842a741c790a6f6c/Screenshot_2021-01-09_at_13.16.25.png](Data%20Structures%20and%20Algorithms%20feab1cb55ae74c6f842a741c790a6f6c/Screenshot_2021-01-09_at_13.16.25.png)
    
    - ***Complete***: All levels are filled up except for the last one that is filled up from left to right - all levels are filled apart from maybe the **last level** of which it is **filled from left to right**.
    - ***Full***: Every node has either **0 or two children**.
    - ***Perfect***: Every node has two children and the **leafs are at the same level**.
    

![Data%20Structures%20and%20Algorithms%20feab1cb55ae74c6f842a741c790a6f6c/Screenshot_2020-10-21_at_12.12.28.png](Data%20Structures%20and%20Algorithms%20feab1cb55ae74c6f842a741c790a6f6c/Screenshot_2020-10-21_at_12.12.28.png)

- Heap, specifically min heap:
    - Is a complete binary tree
    - All nodes are smaller than or equal to the parent
    - Get index `i`'s (current node) child nodes indexes: `2i + 1` , `2i + 2`
    - Parent node: `math.floor((i - 1) / 2)`
- OOP/OOD:
    1. ***Handle Ambiguity*** - most of such questions are **intentionally vague** in order to test whether you will **make assumptions** or **ask clarifying questions**. Try going through the "Six Ws": who, what, where, when, how & why 
    2. Define the ***core objects***.
    3. ***Analyse relationships*** - analyse relationships between objects: Which objects are members of other objects? Which objects inherit from others? Are they One to Many or Many to Many relationships?
    4. ***Investigate Actions*** - consider the key actions the objects will take and how they relate to each other.

# How to approach problems

# More reading

[Interview Cake Slides](https://docs.google.com/presentation/d/1UznxAiUTh9uUPG8bLL1_q1LNPuRChrpOd3IwzFmUA1Y/edit?usp=drivesdk)

# Study guide

- [ ]  Complexity analysis & big O
- [ ]  python
- [ ]  OOP
- [x]  hash tables
- [x]  strings & arrays
- [x]  recursion & DP
- [x]  stacks & queues
- [x]  trees
- [x]  sorting
- [x]  searching
- [ ]  heaps
- [ ]  greedy algorithms
- [x]  tries
- [ ]  patterns
    - [x]  sliding window
    - [x]  hare & tortoise
    - [x]  two pointers
    - [x]  cyclic sort
    - [x]  topological sort
    - [x]  subsets & permutations
    - [x]  merge intervals
    - [x]  k-way merge
    - [x]  two heaps
    - [x]  top k elements
    - [x]  knapsack
    - [x]  bitwise xor
    - [x]  suffix trees
    - [ ]  other

# Pages:

[Python basics](Data%20Structures%20and%20Algorithms%20feab1cb55ae74c6f842a741c790a6f6c/Python%20basics%20991f9d98be1d40c6b9c50b859df13aba.md)

[**Complexity Analysis &** Big O](Data%20Structures%20and%20Algorithms%20feab1cb55ae74c6f842a741c790a6f6c/Complexity%20Analysis%20&%20Big%20O%20ded85f7996b548c7953055302969348c.md)

[Object-Oriented Analysis and Design](Data%20Structures%20and%20Algorithms%20feab1cb55ae74c6f842a741c790a6f6c/Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d.md)

[Hashtables & Hashsets](Data%20Structures%20and%20Algorithms%20feab1cb55ae74c6f842a741c790a6f6c/Hashtables%20&%20Hashsets%20220d9f0e409044c58ec6c2b0e7fe0ab5.md)

[Strings, Arrays & Linked Lists](Data%20Structures%20and%20Algorithms%20feab1cb55ae74c6f842a741c790a6f6c/Strings,%20Arrays%20&%20Linked%20Lists%2081ca9e0553a0494cb8bb74c5c85b89c8.md)

[Recursion, DP & Backtracking](Data%20Structures%20and%20Algorithms%20feab1cb55ae74c6f842a741c790a6f6c/Recursion,%20DP%20&%20Backtracking%20525dddcdd0874ed98372518724fc8753.md)

[Stacks & Queues](Data%20Structures%20and%20Algorithms%20feab1cb55ae74c6f842a741c790a6f6c/Stacks%20&%20Queues%20c7d2cad790be4a61bac42c8718e031fd.md)

[Trees & Graphs](Data%20Structures%20and%20Algorithms%20feab1cb55ae74c6f842a741c790a6f6c/Trees%20&%20Graphs%20edc3401e06c044f29a2d714d20ffe185.md)

[Sorting](Data%20Structures%20and%20Algorithms%20feab1cb55ae74c6f842a741c790a6f6c/Sorting%20c597de5051f1415793ddcf72086aa93d.md)

[Searching](Data%20Structures%20and%20Algorithms%20feab1cb55ae74c6f842a741c790a6f6c/Searching%20733ff84c808c4c9cb5c40787b2df7b98.md)

[Heaps & Priority Queues](Data%20Structures%20and%20Algorithms%20feab1cb55ae74c6f842a741c790a6f6c/Heaps%20&%20Priority%20Queues%20bb4a8de1dbe54089854d8d03c833126c.md)

[Greedy Algorithms](Data%20Structures%20and%20Algorithms%20feab1cb55ae74c6f842a741c790a6f6c/Greedy%20Algorithms%20b9b0a6dd66c94e7db2cbbd9f2d6b50af.md)

[Trie (Keyword Tree)](Data%20Structures%20and%20Algorithms%20feab1cb55ae74c6f842a741c790a6f6c/Trie%20(Keyword%20Tree)%20995fecf3f7ca418b88b528597f88fbfa.md)

[Math Tricks](Data%20Structures%20and%20Algorithms%20feab1cb55ae74c6f842a741c790a6f6c/Math%20Tricks%208c99fd21a1d343f7bee1eaf0467ea362.md)

[Patterns for Coding Questions](Data%20Structures%20and%20Algorithms%20feab1cb55ae74c6f842a741c790a6f6c/Patterns%20for%20Coding%20Questions%20e3f5361611c147ebb2fb3eff37a743fd.md)

[One of those](Data%20Structures%20and%20Algorithms%20feab1cb55ae74c6f842a741c790a6f6c/One%20of%20those%205919e7e3ca2645f692d371354177d774.md)