"""
Problem: Valid Parentheses

LeetCode: 20
Difficulty: Easy

Pattern:
Stack

Approach:
1. Push opening brackets onto the stack.
2. When a closing bracket appears:
   - Check if the stack is empty.
   - Verify the top matches the corresponding opening bracket.
   - Pop the matched opening bracket.
3. At the end, the stack must be empty.

Alternative Solutions:
1. Use an opening bracket set.
2. Push expected closing brackets onto the stack.

Example:
s = "({[]})"

Output:
True

Time Complexity:
O(n)

Space Complexity:
O(n)

Key Learning:
Use a stack whenever matching nested structures that follow
Last In, First Out (LIFO).
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for bracket in s:

            if bracket in mapping:

                if not stack or stack[-1] != mapping[bracket]:
                    return False

                stack.pop()

            else:
                stack.append(bracket)

        return len(stack) == 0


# --------------------------------------------------------------------
# Alternative Solution 1: Opening Bracket Set
# --------------------------------------------------------------------

# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#
#         mapping = {
#             ')': '(',
#             ']': '[',
#             '}': '{'
#         }
#
#         opening = {'(', '[', '{'}
#
#         for bracket in s:
#
#             if bracket in opening:
#                 stack.append(bracket)
#
#             else:
#                 if not stack or stack[-1] != mapping[bracket]:
#                     return False
#
#                 stack.pop()
#
#         return len(stack) == 0


# --------------------------------------------------------------------
# Alternative Solution 2: Push Expected Closing Brackets
# --------------------------------------------------------------------

# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#
#         pairs = {
#             '(': ')',
#             '[': ']',
#             '{': '}'
#         }
#
#         for ch in s:
#
#             if ch in pairs:
#                 stack.append(pairs[ch])
#
#             else:
#                 if not stack or stack.pop() != ch:
#                     return False
#
#         return len(stack) == 0
