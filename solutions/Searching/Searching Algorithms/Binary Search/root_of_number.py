""" 
Root of Number:

Many times, we need to re-implement basic functions without using any standard library functions already implemented. 
For example, when designing a chip that requires very little memory space.
In this question we’ll implement a function root that calculates the n’th root of a number. 
The function takes a nonnegative number x and a positive integer n, 
and returns the positive n’th root of x within an error of 0.001 (i.e. suppose the real root is y, then the error is: |y-root(x,n)| and must satisfy |y-root(x,n)| < 0.001).
Don’t be intimidated by the question. While there are many algorithms to calculate roots that require prior knowledge in numerical analysis, 
there is also an elementary method which doesn’t require more than guessing-and-checking. Try to think more in terms of the latter.
Make sure your algorithm is efficient, and analyze its time and space complexities.

Examples:

    input:  x = 7, n = 3
    output: 1.913

    input:  x = 9, n = 2
    output: 3
"""


"""
----------------- PROBLEM ----------------- :

calculates the n’th root of a number
takes in nonnegative number x and a positive integer n, and returns the positive n’th root of x within an error of 0.001


suppose the real root is y, then the error is: |y-root(x,n)| and must satisfy |y-root(x,n)| < 0.001).


----------------- EXAMPLES ----------------- :

x = 7, n = 3
1.913

x = 9, n = 2
3

x = 8, n = 3
2

x = 4, n = 2
2

x = 3, n = 2
1.732

r^n = x

0.001 - 8
 for each of them ^n
 
 
----------------- BRUTE FORCE ----------------- :
Time complexity : O(1000x) -> O(x)
Space complexity: O(1)


x = 4, n = 2

(0.001, 0.002,.... 1 => 1000) * 4  


x = 8, n = 3

(0.001, 0.002,.... 1 => 1000) * 8





----------------- OPTIMAL ----------------- :

x = 4, n = 2


left    right  mid
0.001 - 4.000  2




x = 8, n = 3

left    right  mid
0.001 - 8.000  4
0.001 - 4.000  2




x = 3, n = 2
left    right  mid
0.001 - 3.000  1.5
1.5   - 3.00   1.5+0.75 = 2.25  
1.5   - 2.25   

---

x = 1.1, n = 2
1.04

left    right  mid   mid^n
0       1.1    0.55  0.3


---

x = 9.1, n = 2
3.01


---
Special case:

x = 0.9, n = 2
0.949


x = 0.5, n = 2
0.707

left    right  mid   mid^n
0.5     1      .75   .5625





break condition:
 - abs(mid^n - x) < 0.001 

"""


def root(x, n):
    left = 0
    right = x
    # special condition
    if x < 1:
        left = x
        right = 1

    while left < right:
        mid = (left+right)/2
        mid_power_n = mid ** n

        # found answer
        if abs(mid_power_n - x) < 0.001:
            return round(mid, 3)

        # is smaller
        elif mid_power_n < x:
            left = mid

        # is larger
        else:
            right = mid


print(root(7, 3))
print(root(3, 2))
print(root(160, 3))
print(root(0.9, 2))
print(root(0.5, 3))
