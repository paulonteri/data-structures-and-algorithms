# Object-Oriented Analysis and Design

[Grokking the Object Oriented Design Interview - Learn Interactively](https://www.educative.io/courses/grokking-the-object-oriented-design-interview)

[Python Object Oriented Programming](https://www.programiz.com/python-programming/object-oriented-programming)

# Introduction

## Examples

- LRU Cache
    
    [LRU Cache - Twitch Interview Question - Leetcode 146](https://youtu.be/7ABFKPK2hD4)
    
    ![Screenshot 2021-10-23 at 13.23.26.png](Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Screenshot_2021-10-23_at_13.23.26.png)
    
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
    
    ![Screenshot 2021-10-23 at 13.25.16.png](Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Screenshot_2021-10-23_at_13.25.16.png)
    
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
    
    ![Screenshot 2021-10-24 at 07.34.42.png](Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Screenshot_2021-10-24_at_07.34.42.png)
    
    ![Screenshot 2021-10-24 at 07.35.22.png](Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Screenshot_2021-10-24_at_07.35.22.png)
    
    ![Screenshot 2021-10-24 at 07.35.43.png](Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Screenshot_2021-10-24_at_07.35.43.png)
    
    ![Screenshot 2021-10-24 at 07.36.37.png](Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Screenshot_2021-10-24_at_07.36.37.png)
    
    [Summed-area table - Wikipedia](https://en.wikipedia.org/wiki/Summed-area_table)
    
    [Computer Vision - The Integral Image](https://computersciencesource.wordpress.com/2010/09/03/computer-vision-the-integral-image/)
    
    ![Screenshot 2021-10-24 at 07.38.21.png](Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Screenshot_2021-10-24_at_07.38.21.png)
    
    ![Screenshot 2021-10-24 at 07.38.34.png](Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Screenshot_2021-10-24_at_07.38.34.png)
    
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
    

Object-oriented programming (OOP) is a style of programming that focuses on using objects to design and build applications. Contrary to procedure-oriented programming where programs are designed as blocks of statements to manipulate data, OOP organizes the program to combine data and functionality and wrap it inside something called an “Object”.

The four principles of object-oriented programming are encapsulation, abstraction, inheritance, and polymorphism.

- **Encapsulation:** Encapsulation is the mechanism of binding the data together and hiding it from the outside world. Encapsulation is achieved when each object keeps its state private so that other objects don’t have direct access to its state. Instead, they can access this state only through a set of public functions.
- **Abstraction:** Abstraction can be thought of as the natural extension of encapsulation. It means hiding all but the relevant data about an object in order to reduce the complexity of the system. In a large system, objects talk to each other, which makes it difficult to maintain a large code base; abstraction helps by hiding internal implementation details of objects and only revealing operations that are relevant to other objects.
- **Inheritance:** Inheritance is the mechanism of creating new classes from existing ones.
- **Polymorphism:** Polymorphism (from Greek, meaning “many forms”) is the ability of an object to take different forms and thus, depending upon the context, to respond to the same message in different ways. Take the example of a chess game; a chess piece can take many forms, like bishop, castle, or knight and all these pieces will respond differently to the ‘move’ message

# Theory

## Constructors in Python

`__init__()` function. This special function gets called whenever a new object of that class is instantiated.

This type of function is also called **constructors** in Object Oriented Programming (OOP). We normally use it to initialize all the variables.

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

![Screenshot 2021-10-11 at 21.30.49.png](Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Screenshot_2021-10-11_at_21.30.49.png)

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
        super().__init__(self,3)

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

### Method Overriding in Python

In the above example, notice that `__init__()` method was defined in both classes, Triangle as well Polygon. When this happens, the method in the derived class overrides that in the base class. This is to say, `__init__()` in Triangle gets preference over the `__init__` in Polygon.

Generally when overriding a base method, we tend to extend the definition rather than simply replace it. The same is being done by calling the method in base class from the one in derived class (calling `Polygon.__init__()` from `__init__()` in `Triangle`).

A better option would be to use the built-in function `super()`. So, `super().__init__(3)` is equivalent to `Polygon.__init__(self,3)` and is preferred.

## Encapsulation

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

We used `__init__()` method to store the maximum selling price of `Computer`. We tried to modify the price. However, we can't change it because Python treats the `__maxprice` as private attributes.

As shown, to change the value, we have to use a setter function i.e `setMaxPrice()` which takes price as a parameter.

## Polymorphism *

Polymorphism is an ability (in OOP) to **use a common interface for multiple forms (data types)**.

Suppose, we need to color a shape, there are multiple shape options (rectangle, square, circle). However we could use the same method to color any shape. This concept is called Polymorphism.

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

![Screenshot 2021-10-17 at 18.02.19.png](Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Screenshot_2021-10-17_at_18.02.19.png)

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

[Python Operator Overloading](Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Python%20Operator%20Overloading%200e8809af87164a039f103691140df730.csv)

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

[Overloading Comparison Operators](Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Overloading%20Comparison%20Operators%2081101d971d0e4dad92625b304e846520.csv)

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

---

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

![Screenshot 2021-10-17 at 17.57.43.png](Object-Oriented%20Analysis%20and%20Design%201a01887a9271475da7b3cd3f4efc9e0d/Screenshot_2021-10-17_at_17.57.43.png)

### Examples:

- 'K' Closest Points to the Origin

## Creating a coordinates class

### Examples:

- 'K' Closest Points to the Origin (similar)

## nonlocal

```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]):
        preorder_pos = 0
        inorder_idxs = {val: idx for idx, val in enumerate(inorder)}

        def helper(preorder: List[int], inorder: List[int], inorder_left, inorder_right):
            nonlocal preorder_pos
```

# Python Operator Overloading