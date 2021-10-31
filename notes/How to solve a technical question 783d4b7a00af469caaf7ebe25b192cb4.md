# How to solve a technical question

[How to Master The Coding Interview!](https://youtu.be/A4Wui7qB2ow)

[7 Steps for Structuring Your Response in a Technical Interview for Software Engineering](https://youtu.be/jMLxrV-6d4M)

[Whiteboard Coding Interviews: A 6 Step Process to Solve Any Problem | Fullstack Academy](https://www.fullstackacademy.com/blog/whiteboard-coding-interviews-a-6-step-process-to-solve-any-problem)

[Welcome To The Coding Interview - You Suck](https://docs.google.com/document/d/1eKirumpmwDWTtKCJKn2HuoQ2NavEfR41whmTyaQcio4/edit#)

[During the Coding Interview | Tech Interview Handbook](https://techinterviewhandbook.org/during-coding-interview/)

[Coding Signals | Tech Interview Handbook](https://techinterviewhandbook.org/coding-signals/)

[Cheatsheet | Tech Interview Handbook](https://techinterviewhandbook.org/cheatsheet/)

[How to: Work at Google - Example Coding/Engineering Interview](https://youtu.be/XKu_SEDAykw)

[Google Colaboratory](https://colab.research.google.com/drive/1qaGNKxex7XvVA2ysbd1U1JMFi7C7ZzSN)

## General guidelines

smile & be confident

win in the beginning

The interviewer is trying to view you as a **colleague**

As your interviewer... "**Does that make sense?**"

What Companies Look For in University roles: Problem-Solving Abilities + Involvement + Passion = Promise 

# Solving problem

```python
"""
Restate problem
Examples
Analyse problem & find Approach (more examples & solutions. (BF -> Optimal)
Tests
Code
"""
```

It's **super important that you don't jump into code before actually having a clear picture of your algorithm** in mind.

Then the goal was to start from an ***example***, figure out the ***algorithm to solve the problem***, add the solution to the solution section, keep ***iterating until you find the most optimal solution***, have the interviewer on board with your algorithm, write ***test cases*** and ***THEN start coding followed by thorough testing***. 

Writing **test cases before writing the code is something that people in the industry really appreciate**. I had quite a lot of interviewers compliment me when I went to the board and wrote test cases before the function prototype. Moreover, when you are done with the code the **worst mistake you can make is to say you are done without actually dry running all your test cases**.

---

You should probably be spending the same amount of time analysing the problem as you do writing the code.

---

Speak out your thoughts and logic. Start writing the code only after you have discussed the approach with the interviewer.

---

```python
"""
-------------------- RESTATE PROBLEM ------------------------------------
- note key parts
- assumptions
- ask questions
- ask for examples/to repeat that -> to give you time to process
	- ask for a second example can give you even more time plus the inteviewer will slow it down

-------------------- EXAMPLES --------------------------------------------
- ***write your own simple example*** *****
- base example
- input => output

-------------------- ANALYSIS, SOLUTIONS & PSEUDOCODE --------------------------------------------
* Use a BFS approach to find solutions. Do not go too deep / get fixated too much on one
* Spot patterns and buy time

- more examples
		- simple
		- base example
		- edge cases
- solve simplest cases
- think on paper 
- diagram problem
- test against a set of examples in order to find a common pattern or algorithm
- **write down the steps/pseudocode to *free up your thinking* ******

----- BRUTE FORCE / STRAIGHTFORWARD
- 9/10 optimal comes from the brute force

----- OPTIMAL
- look for:
		Bottlenecks
		Unecessary work & Unused info
		Duplicated work
If stuck, say:
 "
   These are the things I have,
   This is what I'm trying to get but I'm missing a little connector
   Is my logic flowing? Is is my logic breaking somewhere?
 "

----- PSEUDOCODE
- list of steps

-------------------- TESTS --------------------------------------------
- can use examples
- simple to difficult tests
- each test should be indipendent / have a solid reason

-------------------- CODE ----------------------------------------------------

"""
```

```python
"""
R
-------------------- EXAMPLES --------------------------------------------
- ***write your own simple example*** *****

-------------------- ANALYSIS, SOLUTIONS & PSEUDOCODE --------------------------------------------

----- BRUTE FORCE

----- OPTIMAL

----- PSEUDOCODE

-------------------- TESTS --------------------------------------------

-------------------- CODE ----------------------------------------------------
"""
```

---

## 1. Restate & Understand the problem

[https://youtu.be/A4Wui7qB2ow?t=1062](https://youtu.be/A4Wui7qB2ow?t=1062)

Thank the interviewer for the question/ for reading the question.

make a comment like "I noticed that this is a string problem, I've been practicing strings for two weeks. Awesome! Let's go"

Read the question back to the interviewer trying to understand it

Always understand the problem first. **Ask counter questions** like can the array contain negative numbers? is the graph acyclic? (just make sure things are as expected, do not assume anything). This is one of the important factors, don’t jump into solving the problem.

Parse the problem and break it into its bare components

ask for examples/to repeat that/explain the question -> to give you time to process
ask for a second example can give you even more time plus the inteviewer will slow it down

---

## 2. Examples (Write Out Examples)

[https://youtu.be/S30F-xf5Rb8?t=155](https://youtu.be/S30F-xf5Rb8?t=155)

This often works hand-in-hand with Analysing problem 

input/parameters ⇒ output

### a. Generate simple examples first

Generate simple examples

### b. Generate examples similar to the base example

Working through the base example

### c. Try to generate some with edge cases

### d. Start to diagram or draw out the problem / think on paper ([discussed next]())

---

## 3. Analyse problem & find Approach (more examples & solutions. (BF -> Optimal)

[https://youtu.be/jMLxrV-6d4M?t=195](https://youtu.be/jMLxrV-6d4M?t=195)

Ask lot's of questions

Discuss your approach. Discuss different approaches. Start with naive. Consider both time and space complexity.

You can be **10-15 minutes** discussing.

**Teamwork.**

Win your interviewer at the beginning make them think you are confident and smart.

Catch edge cases where they'll impact your core algorithm.

While you are thinking about the solution, you need to be verbose. you can always take some time to think and speak. But don’t be completely silent.

It is okay to take time here rather than during coding.

Optimise parts of your algorithm

![Untitled](How%20to%20solve%20a%20technical%20question%20783d4b7a00af469caaf7ebe25b192cb4/Untitled.png)

How?

Use a BFS approach to find solutions

Do not go too deep / get fixated too much on one

Goals

**Convey that you are planning** before going into the code

- If your interviewer gives you a hint ensure you incorporate it into your solution
- Talk about the advantages and disadvantages of your solutions and the space-time complexity

Less thinking while coding

Why?

Spot patterns and buy time

- If you are not able to formalise your ideas in **plain English** then you will **not be able to code**
- Hoping into your coding too early is how errors pop up

Conclusion

- ensure they know, that you know, what you are doing

### a. Diagram or draw out the problem / Think on paper

Analyze the problem thoroughly, understand and clear ambiguity plus ask the necessary questions

Input, output, observations

Communicate with your interviewer about your thought process and listen for any potential feedback or hints from them

Test against a set of examples in order to find a common pattern or algorithm

### b. Simplify & Generalise (Find common and general cases)

Solve a simpler version

Find common and general case

### c. Come up with brute force

9/10 optimal comes from the brute force

Consider different solutions and their space-time complexity

**Note:** Sometimes brute force is the most optimal

The goal is to solve the problem **without concern for efficiency**.

### d. Optimise / Come up with an optimal solution

[https://youtu.be/A4Wui7qB2ow?t=763](https://youtu.be/A4Wui7qB2ow?t=763)

```python
"""
- look for:
		Bottlenecks
		Unecessary work & Unused info
		Duplicated work
"""
```

Notice patterns

Use better data structures

if you can do both / ask whether you should optimise for time or space.

**You will be asked to optimise your solution no matter what**. If you think you can create the most optimal solution as your initial answer, go for it. If not, just create some solution that will work and mention that you plan on optimising it later (if you have time).

Choose the best solution you can implement in the time given

Discuss and explain in-depth exactly what you are going to do & Convince the interviewer your solution is correct before you start coding

"teach" them your solution

Once you and the interviewer agree that this is the most optimal approach to solve the problem. and you prove it by dry running on some examples (and some examples which will have corner cases). Only after that, you’ll be asked to write code. 

So make sure you learn to explain your thought process and prove that solution is optimal (with what time complexity) before jumping into coding. Make it a habit in your general practice as well.

If stuck, say:
 "
   These are the things I have,
   This is what I'm trying to get but I'm missing a little connector
   Is my logic flowing? Is is my logic breaking somewhere?
 "

### d. Pseudocode

Pseudocode an answer before writing it. This can be your **list of steps** in your algorithm as well as the requirements your algorithm must meet in order to be successful. I personally write a list that I can check off as I go through it, that way I don't forget what I was going to do. With that, some interviewers may accept pseudocode as your answer.

---

## 4. Tests before coding

using the examples

can really impress the interviewer

### a. Each test should be independent / have a solid reason

### b. Simple to difficult tests

---

## 5. Code

Translate your solution to code while explaining each step as you go (ensure it does seem like you are merely reciting a memorized solution)

3-4 lines then explain code

Can take 7-10 min

### Breadth-first coding

[The Macadamian Files: Breadth-First Coding](http://thefiles.macadamian.com/2008/10/breadth-first-coding.html)

[Cracking the Coding Interview - Fullstack Academy Speaker Series](https://youtu.be/Eg5-tdAwclo)

Separate the non-essential/annoying/time-consuming parts into separate functions.

### Test code

Test code

---

---

# Skills

## Communication

## Problem-solving

## Coding

## Culture fit

---

---

# More tips

## Google grading rubric

Google's Grading Rubric:

- Problem-solving and analytical abilities (1 point)
- Data structures and Algorithms (1 point)
- Coding (1 point)
    1. Ability to translate algorithms into code
    2. Ability to write bug-free code
    3. Ability to write formal code (not pseudocode)
    4. Ability to write elegant code
- Communications skills (1 point)
    1. How well can you "teach" them your solution?
    2. Also known as "Would I want to work with this person?"

## Checklist

- [] Asked Clarifying questions
- [] Talked about the approach
    - [] Working through the base example
    - [] pseudocode
    - [] Tradeoffs
    - [] Talking through edge cases
    - [] Test Cases
    - [] Big-O
- [] Coding / Comfortable with language
- [] Communication

## More guides

[How%20to%20solve%20a%20technical%20question%20783d4b7a00af469caaf7ebe25b192cb4/cracking_the_coding_skills_-_v6.pdf](How%20to%20solve%20a%20technical%20question%20783d4b7a00af469caaf7ebe25b192cb4/cracking_the_coding_skills_-_v6.pdf)

![How%20to%20solve%20a%20technical%20question%20783d4b7a00af469caaf7ebe25b192cb4/Screenshot_2021-07-19_at_22.42.05.png](How%20to%20solve%20a%20technical%20question%20783d4b7a00af469caaf7ebe25b192cb4/Screenshot_2021-07-19_at_22.42.05.png)

[https://youtu.be/ckW4cUqui_w](https://youtu.be/ckW4cUqui_w)

[leetcode god 2.pdf](How%20to%20solve%20a%20technical%20question%20783d4b7a00af469caaf7ebe25b192cb4/leetcode_god_2.pdf)

Where I need to be

1) If you can think of 2-3 solutions where 1 of them is the naive solution. 
2) You know what questions to ask to get to the optimal solution and if those questions are answered, you can give an optimal solution.
3) You can do achieve an 80% success rate on the first try of a leetcode attempt.

[https://www.youtube.com/watch?v=DIR_rxusO8Q&list=TLPQMTYwNzIwMjH8oFHlVytKlw&index=3](https://www.youtube.com/watch?v=DIR_rxusO8Q&list=TLPQMTYwNzIwMjH8oFHlVytKlw&index=3)

Should probably be spending the same amount of time analysing the problem as you do writing the code.

Major tips:

- [https://github.com/jwasham/coding-interview-university#dont-feel-you-arent-smart-enough](https://github.com/jwasham/coding-interview-university#dont-feel-you-arent-smart-enough)
- [Skill Assessment Tests - 5 Steps to Make them EASY (Vervoe, Hackerrank, Pymetrics)](https://youtu.be/KhCt0Rjejbw)
- [How to Get Unstuck in Technical Interviews](https://blog.pramp.com/how-to-get-unstuck-in-technical-interviews-93d4632ef996)

Here’s an **[example coding interview](https://www.youtube.com/watch?v=XKu_SEDAykw)**

[https://youtu.be/-QxUp8MwbWw](https://youtu.be/-QxUp8MwbWw)

Interview tips from a Software Engineer with 13 years of experience

[https://youtu.be/NJsANA8bB7w](https://youtu.be/NJsANA8bB7w)

### How to Ace a Technical Interview talk.

Would you wish to start out your career in tech or work wish to learn how to effectively prepare for your next technical interview?
Our guests were Ruth Ferland who works with Microsoft as an Application Development Manager, Anthony Nandaa, Clement Habinshuti and Pius Njoka who work as software Engineers at Microsoft. They share her tips from a recruiter's perspective, the interviewing process and help you nail your next interview. 🙃

[https://youtu.be/IL582cpLFTg](https://youtu.be/IL582cpLFTg)

.

[How%20to%20solve%20a%20technical%20question%20783d4b7a00af469caaf7ebe25b192cb4/How_to_Ace_a_Technical_Interview.pdf](How%20to%20solve%20a%20technical%20question%20783d4b7a00af469caaf7ebe25b192cb4/How_to_Ace_a_Technical_Interview.pdf)

[Mock Interview Feedback](https://www.notion.so/Mock-Interview-Feedback-273a530773c9447399669f8e1c9bb030)

[Issues faced while solving problems ](https://www.notion.so/Issues-faced-while-solving-problems-c7898be9664e45a9a8c4bb3934a488fc)