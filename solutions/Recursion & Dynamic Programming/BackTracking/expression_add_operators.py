""" 
Expression Add Operators

Given a string num that contains only digits and an integer target, 
    return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num 
    so that the resultant expression evaluates to the target value.
Note that operands in the returned expressions should not contain leading zeros.

Example 1:
    Input: num = "123", target = 6
    Output: ["1*2*3","1+2+3"]
    Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.
Example 2:
    Input: num = "232", target = 8
    Output: ["2*3+2","2+3*2"]
    Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.
Example 3:
    Input: num = "105", target = 5
    Output: ["1*0+5","10-5"]
    Explanation: Both "1*0+5" and "10-5" evaluate to 5.
        Note that "1-05" is not a valid expression because the 5 has a leading zero.
Example 4:
    Input: num = "00", target = 0
    Output: ["0*0","0+0","0-0"]
    Explanation: "0*0", "0+0", and "0-0" all evaluate to 0.
        Note that "00" is not a valid expression because the 0 has a leading zero.
Example 5:
    Input: num = "3456237490", target = 9191
    Output: []
    Explanation: There are no expressions that can be created from "3456237490" to evaluate to 9191.

https://leetcode.com/problems/expression-add-operators
"""


""" 
https://www.notion.so/paulonteri/Recursion-DP-Backtracking-525dddcdd0874ed98372518724fc8753#83d1fce1c9944b78a65a2c973be09e46
"""


class Solution:
    def addOperators(self, num: str, target: int):
        answers = []

        def dfs(idx, prev_operand, prev_operation, total, string):
            """ 
            Important info:
                - `prev_operand` is used to recursively build operands. 
                    Eg: for 123, it will grow as follows 1 => 12 => 123  \n
                - `prev_operation`is used to store the results of the previous operation so that it can be undone in case we need to multiply \n
                - `total` is the result of the running calculation
            """
            if idx == len(num):
                if total == target and prev_operand == 0:
                    answers.append("".join(string[1:]))
                return

            # # Try out all possible operands --------------------------------------------------------------------------------------
            # Extending the current operand by one digit
            operand = (prev_operand * 10) + int(num[idx])
            str_op = str(operand)
            # To avoid cases where we have 1 + 05 or 1 * 05 since 05 won't be a valid operand. Hence this check
            if operand > 0:
                dfs(idx + 1, operand, prev_operation, total, string)

            # # Math -------------------------------------------------------------------------------------------------------------------
            # remember to reset the prev_operand to 0 (it is no longer needed, we will start a new one next time)

            # Can subtract or multiply only if there are some previous operands
            if string:
                # ---
                # Subtraction - negate operand (as prev_operation) so that we don't have to keep track of the signs
                string.append("-")
                string.append(str_op)
                dfs(idx+1, 0, -operand, total-operand, string)
                string.pop()
                string.pop()

                # ---
                # Multiplication - undo last operation and multiply
                operation = prev_operation * operand
                new_total = (total - prev_operation) + operation
                #
                string.append("*")
                string.append(str_op)
                dfs(idx+1, 0, operation, new_total, string)
                string.pop()
                string.pop()

            # ---
            # Addition - also used to handle index 0/starting out (no string)
            string.append("+")
            string.append(str_op)
            dfs(idx+1, 0, operand, total+operand, string)
            string.pop()
            string.pop()

        dfs(0, 0, 0, 0, [])
        return answers
