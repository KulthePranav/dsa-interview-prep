"""
Problem: Evaluate Reverse Polish Notation

LeetCode: 150
Difficulty: Medium

Pattern:
Stack

Approach:
1. Traverse all tokens.
2. Push numbers onto the stack.
3. When an operator appears:
   - Pop two operands.
   - Apply the operation.
   - Push the result.
4. The remaining element is the answer.

Alternative Solution:
Use if-elif statements instead of an operator dictionary.

Example:

Input:
["2","1","+","3","*"]

Output:
9

Time Complexity:
O(n)

Space Complexity:
O(n)

Alternative Complexity:
Time: O(n)
Space: O(n)

Key Learning:
A stack naturally evaluates postfix expressions because the most recent operands are used first.
"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operation_dict = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)  # Truncate toward zero
        }

        stack = []

        for token in tokens:

            if token.lstrip("-").isdigit():
                stack.append(int(token))

            else:
                b = stack.pop()
                a = stack.pop()

                result = operation_dict[token](a, b)
                stack.append(result)

        return stack[0]


# ------------------------------------------------------------------
# Alternative Solution: if-elif
# ------------------------------------------------------------------

# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#
#         stack = []
#         operators = {"+", "-", "*", "/"}
#
#         for token in tokens:
#
#             if token not in operators:
#                 stack.append(int(token))
#
#             else:
#                 b = stack.pop()
#                 a = stack.pop()
#
#                 if token == "+":
#                     stack.append(a + b)
#
#                 elif token == "-":
#                     stack.append(a - b)
#
#                 elif token == "*":
#                     stack.append(a * b)
#
#                 else:
#                     stack.append(int(a / b))
#
#         return stack[0]
