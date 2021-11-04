""" 
Exclusive Time of Functions:

On a single-threaded CPU, we execute a program containing n functions. 
Each function has a unique ID between 0 and n-1.
Function calls are stored in a call stack: when a function call starts, its ID is pushed onto the stack, and when a function call ends, its ID is popped off the stack. 
The function whose ID is at the top of the stack is the current function being executed. 
Each time a function starts or ends, we write a log with the ID, whether it started or ended, and the timestamp.
You are given a list logs, where logs[i] represents the ith log message formatted as a string "{function_id}:{"start" | "end"}:{timestamp}". 
For example, "0:start:3" means a function call with function ID 0 started at the beginning of timestamp 3, and "1:end:2" means a function call with function ID 1 ended at the end of timestamp 2. 
Note that a function can be called multiple times, possibly recursively.
A function's exclusive time is the sum of execution times for all function calls in the program. 
For example, if a function is called twice, one call executing for 2 time units and another call executing for 1 time unit, the exclusive time is 2 + 1 = 3.
Return the exclusive time of each function in an array, where the value at the ith index represents the exclusive time for the function with ID i.

https://leetcode.com/problems/exclusive-time-of-functions/
"""


import collections
'''
*** Fill array with current running job ***
O(n+m) space | where m is the duration

Input: 
    n = 2, 
    logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
Output: 
    [7,1]
    [0, 1,  2, 3, 4,  5,  6,  0]
    [0, 0,  0, 0, 0,  0,  1,  0]
Explanation:
Function 0 starts at the beginning of time 0, executes for 2 units of time, and recursively calls itself.
Function 0 (recursive call) starts at the beginning of time 2 and executes for 4 units of time.
Function 0 (initial call) resumes execution then immediately calls function 1.
Function 1 starts at the beginning of time 6, executes 1 units of time, and ends at the end of time 6.
Function 0 resumes execution at the beginning of time 6 and executes for 2 units of time.
So function 0 spends 2 + 4 + 1 = 7 units of total time executing, and function 1 spends 1 unit of total time executing.


n = 2, logs = ["0:start:0","0:start:2","0:end:5","1:start:7","1:end:7","0:end:8"]

---
prev_job = []
curr_job = 0

past_process
[0, 1, 2, 3, 4, 5, 6, 7, 8]
[]

---

"0:start:2"
fill past_process with curr_job till idx 1
add curr_job to prev_job
change curr_job to 0

prev_job = [0]
curr_job = 0

past_process
[0,  1, 2, 3, 4, 5, 6, 7, 8]
[0,  ]

---

"0:end:5"
fill past_process with curr_job till idx 5
replace curr_job with prev_job.pop()

prev_job = []
curr_job = 0

past_process
[0,  1, 2, 3, 4, 5,  6, 7, 8]
[0,  0, 0, 0, 0, 0,  ]

---

"1:start:7"
fill past_process with curr_job till idx 6
add curr_job to prev_job
change curr_job to 1

prev_job = [0]
curr_job = 1

past_process
[0,  1, 2, 3, 4, 5,  6,  7, 8]
[0,  0, 0, 0, 0, 0,  0,  ]

---

"1:end:7"
fill past_process with curr_job till idx 7
replace curr_job with prev_job.pop()

prev_job = []
curr_job = 0

past_process
[0,  1, 2, 3, 4, 5,  6,  7,  8]
[0,  0, 0, 0, 0, 0,  0,  1,  ]

---

"0:end:8"
fill past_process with curr_job till idx 8
replace curr_job with prev_job.pop()

prev_job = []
curr_job = None

past_process
[0,  1, 2, 3, 4, 5,  6,  7,  8]
[0,  0, 0, 0, 0, 0,  0,  1,  0]


n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]

[0, 1,  2, 3, 4,  5, 6]
[0, 0,  1, 1, 1,  0]
--------------------------
O(n) space
without the space

def time:
    
    result = [0] * len(n)
    
    stack = []
    last_job = 0
    for log in logs:
        if start:
            time
            job
            for _ in range((time-last_log)+1):
                prev_job = stack[-1]
                result[prev_job] += 1
                
            stack.append(job)
                
            
        
        elif end:

'''


"""
--------------------------------------------------------------------------------

"""


class SolutionBF:
    def get_job_info(self, job_str):
        job, kind, time = job_str.split(":")
        return int(job), int(time), kind

    def exclusiveTime(self, n: int, logs):
        task_history = []

        stack = []
        next_placement = 0
        for log in logs:
            job, time, kind = self.get_job_info(log)

            if kind == "start":
                # place last job
                for _ in range((time-next_placement)):
                    prev_job = stack[-1]
                    task_history.append(prev_job)

                # place current job
                task_history.append(job)
                next_placement = time+1

                stack.append(job)

            elif kind == "end":
                # place last job == current job
                prev_job = stack.pop()
                for _ in range((time-next_placement)+1):
                    task_history.append(prev_job)
                next_placement = time+1

        task_counter = collections.Counter(task_history)
        result = [0] * n
        for key in task_counter:
            result[key] = task_counter[key]
        return result


"""
--------------------------------------------------------------------------------

"""


class Solution_:
    def get_job_info(self, job_str):
        job, kind, time = job_str.split(":")
        return int(job), int(time), kind

    def exclusiveTime(self, n: int, logs):
        result = [0] * n

        stack = []
        next_placement = 0
        for log in logs:
            job, time, kind = self.get_job_info(log)

            if kind == "start":
                # place last job
                for _ in range((time-next_placement)):
                    prev_job = stack[-1]
                    result[prev_job] += 1

                # place current job
                result[job] += 1
                next_placement = time+1

                # move to top of stack
                stack.append(job)

            elif kind == "end":
                # place last job == current job
                prev_job = stack.pop()
                for _ in range((time-next_placement)+1):
                    result[prev_job] += 1
                next_placement = time+1

        return result


"""
--------------------------------------------------------------------------------

"""


class Solution:
    def get_job_info(self, job_str):
        job, kind, time = job_str.split(":")
        return int(job), int(time), kind

    def exclusiveTime(self, n: int, logs):
        result = [0] * n

        stack = []
        next_placement = 0
        for log in logs:
            job, time, kind = self.get_job_info(log)

            if kind == "start":
                # place last job
                if stack:
                    prev_job = stack[-1]
                    result[prev_job] += time-next_placement

                # place current job
                result[job] += 1
                next_placement = time+1

                # move to top of stack
                stack.append(job)

            elif kind == "end":
                # place last job == current job
                stack.pop()
                result[job] += time-next_placement+1
                next_placement = time+1

        return result
