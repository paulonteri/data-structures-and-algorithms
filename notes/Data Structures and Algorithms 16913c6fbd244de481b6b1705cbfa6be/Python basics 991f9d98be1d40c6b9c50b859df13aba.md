# Python basics

[20+ helpful Python syntax patterns for coding interviews](https://towardsdatascience.com/19-helpful-python-syntax-patterns-for-coding-interviews-3704c15b758f)

# Integers

Integers in python3 are unbounded

### Examples

- Happy Number

### Power

```python
x = -2

print(x**2) # 4
print(x*x) # 4
```

### Square root *

```python
import math

math.sqrt(49)
# 7
```

### Modulus(%) vs Floor(//)

**Modulus:** The modulus-function computes the remainder of a division, which is the "leftover" of an integral division.

**Floor:** The floor-function provides the lower-bound of an integral division. The upper-bound is computed by the ceil function. (Basically speaking, the floor-function cuts off all decimals).

```python
# modulus
print(324 % 10) # 4

# floor
print(324 // 10) # 32
```

### math.ceil() & math.floor()

```python
import math

math.ceil(2.17) # 3
math.floor(2.17) # 2
```

### Infinity (can be used for math.max)

```python
float("inf")
float("-inf")
```

---

# [.isalpha() .isnumeric() & .isalnum()](Strings,%20Arrays%20&%20Linked%20Lists%2081ca9e0553a0494cb8bb74c5c85b89c8.md)

# [chr() & ord()](Strings,%20Arrays%20&%20Linked%20Lists%2081ca9e0553a0494cb8bb74c5c85b89c8.md)

# Other

## Lambda functions

```python
>>> (lambda x, y: x + y)(2, 3)
5
>>> double = lambda x: x * 2
>>> double(4)
```

Example usage

```python
# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

print(new_list) # [2, 10, 8, 12, 16, 22, 6, 24]
```

---

## Sort

---

## Random

### random.random()

Return the next random floating point number in the range [0.0, 1.0]

```python
import random

>>> random.random()
0.6280590213451548
>>> random.random()
0.1623939995862359
>>> random.random()
0.6704949828925247
>>> random.random()
0.6838627536588555
```

### random.randrange(start,stop,step)

Return a randomly selected element from range(start, stop, step). This is equivalent to choice(range(start, stop, step)), but doesn’t actually build a range object.

```python
import random

>>> random.randrange(20)
7
>>> random.randrange(10,20,2)
16
>>> random.randrange(start=10,stop=20,step=2)
18
>>> random.randrange(start=10,stop=20,step=2)
14
>>> random.randrange(start=10,stop=20,step=2)
12
>>> random.randrange(start=10,stop=20,step=2)
14
>>> random.randrange(start=10,stop=20,step=2)
16
>>> random.randrange(start=10,stop=20,step=2)
18
>>> random.randrange(start=10,stop=20,step=2)
18
>>> random.randrange(start=10,stop=20,step=2)
18
>>> random.randrange(start=10,stop=20,step=2)
16
>>> random.randrange(start=10,stop=20,step=2)
16
>>> random.randrange(start=10,stop=20,step=2)
```

### random.randint(a,b)

Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1)

```python
import random

>>> random.randint(10,20)
19
>>> random.randint(10,20)
16
>>> random.randint(10,20)
15
>>> random.randint(10,20)
20
>>> random.randint(10,20)
11
>>> random.randint(10,20)
17
>>> random.randint(10,20)
20
>>> random.randint(10,20)
```

### random.choice(seq)

Return a random element from the non-empty sequence seq

```python
import random

>>> random.choice(['win', 'lose', 'draw'])
'lose'
>>> random.choice(['win', 'lose', 'draw'])
'win'
>>> random.choice(['win', 'lose', 'draw'])
'win'
>>> random.choice(['win', 'lose', 'draw'])
'win'
>>> random.choice(['win', 'lose', 'draw'])
'lose'
>>> random.choice(['win', 'lose', 'draw'])
'lose'
>>> random.choice(['win', 'lose', 'draw'])
'draw'
```

## [heapq](Heaps%20&%20Priority%20Queues%20bb4a8de1dbe54089854d8d03c833126c.md)

[Heaps & Priority Queues](Heaps%20&%20Priority%20Queues%20bb4a8de1dbe54089854d8d03c833126c.md)

## collections

### `collections.deque()` *

### `collections.defaultdict`

### `collections.OrderedDict`

## `sortedcontainers.SortedDict`