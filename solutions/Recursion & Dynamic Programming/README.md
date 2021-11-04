# Dynamic Programming & Memoization

Although people make a big deal about how scary dynamic programming problems are, there's really no need to be afraid of them.
In fact, once you get the hang of them, these can actually be very easy problems.

***Dynamic programming*** is mostly just a matter of taking a recursive algorithm and **finding the overlapping subproblems** (that is, the repeated calls).
You then **cache** those results for future recursive calls.

Alternatively, you can study the pattern of the recursive calls and implement something iterative. You still "cache" previous work.

    A note on terminology: 
    Some people call top-down dynamic programming "memoization" and only use "dynamic programming" to refer to bottom-up work.
    We do not make such a distinction here. We call both dynamic programming.

One of the simplest examples of dynamic programming is computing the nth Fibonacci number.
A good way to approach such a problem is often to implement it as a normal recursive solution, and then add the caching part.

---

## Additional (maybe useful) info

Recursive solutions, by definition, are built off of solutions to subproblems. Many times, this will mean simply to compute f ( n) by adding something, removing something, or otherwise changing the solution for f ( n-1). In other cases, you might solve the problem for the first half of the data set, then the second half, and then merge those results.

### Ways of dividing a problem into subproblems

There are many ways you might divide a problem into subproblems. Three of the most common approaches to develop an algorithm are bottom-up, top-down, and half-and-half.

#### Bottom-Up Approach

The bottom-up approach is often the most intuitive. We start with knowing how to solve the problem for a simple case, like a list with only one element. Then we figure out how to solve the problem for two elements, then for three elements, and so on. The key here is to think about how you can build the solution for one case off of the previous case (or multiple previous cases).

#### Top-Down Approach

The top-down approach can be more complex since it's less concrete. But sometimes, it's the best way to think about the problem.
In these problems, we think about how we can divide the problem for case N into subproblems. Be careful of overlap between the cases.

#### Half-and-Half Approach

In addition to top-down and bottom-up approaches, it's often effective to divide the data set in half.
For example, binary search works with a "half-and-half" approach. When we look for an element in a sorted array, we first figure out which half of the array contains the value. Then we recurse and search for it in that half.
Merge sort is also a "half-and-half" approach. We sort each half of the array and then merge together the sorted halves.

---

A lot of the problems involving recursion can be found in the Arrays and Trees sections
