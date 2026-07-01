"""
Problem: Min Stack

LeetCode: 155
Difficulty: Medium

Pattern:
Stack + Auxiliary Stack

Approach:
1. Maintain two stacks:
   - stack stores all values.
   - min_stack stores the minimum value up to each position.
2. On push:
   - Push the value onto stack.
   - Push min(current value, previous minimum) onto min_stack.
3. On pop:
   - Pop from both stacks.
4. The top of min_stack is always the current minimum.

Alternative Solution:
Store (value, current_min) tuples in a single stack.

Example:

push(5)
push(3)
push(7)

stack:
[5,3,7]

min_stack:
[5,3,3]

getMin() -> 3

Time Complexity:
Push    O(1)
Pop     O(1)
Top     O(1)
GetMin  O(1)

Space Complexity:
O(n)

Alternative Complexity:
Time: O(1)
Space: O(n)

Key Learning:
Maintain an auxiliary stack to store additional state for constant-time queries.
"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)

        if not self.min_stack:
            self.min_stack.append(value)
        else:
            self.min_stack.append(min(self.min_stack[-1], value))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# ------------------------------------------------------------------
# Alternative Solution: Single Stack of Tuples
# ------------------------------------------------------------------

# class MinStack:
#
#     def __init__(self):
#         self.stack = []
#
#     def push(self, value: int) -> None:
#         current_min = value
#
#         if self.stack:
#             current_min = min(value, self.stack[-1][1])
#
#         self.stack.append((value, current_min))
#
#     def pop(self) -> None:
#         self.stack.pop()
#
#     def top(self) -> int:
#         return self.stack[-1][0]
#
#     def getMin(self) -> int:
#         return self.stack[-1][1]
