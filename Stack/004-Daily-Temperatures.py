"""
Problem: Daily Temperatures

LeetCode: 739
Difficulty: Medium

Pattern:
Monotonic Stack (Next Greater Element)

Approach:
1. Maintain a stack of unresolved indices.
2. While the current temperature is greater than the temperature
   at the top index of the stack:
   - Pop the index.
   - Compute the waiting days.
3. Push the current index.
4. Remaining indices have no warmer day.

Example:

Input:
[73,74,75,71,69,72,76,73]

Output:
[1,1,4,2,1,1,0,0]

Time Complexity:
O(n)

Space Complexity:
O(n)

Alternative Solution:
Brute Force

Alternative Complexity:

Brute Force:
Time: O(n²)
Space: O(1)

Key Learning:
Store indices instead of values so you can calculate the distance
between the current day and the previous unresolved day.
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []

        answer = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):

            while stack and temp > temperatures[stack[-1]]:

                index = stack.pop()

                answer[index] = i - index

            stack.append(i)

        return answer


# ------------------------------------------------------------------
# Alternative Solution: Brute Force
# ------------------------------------------------------------------

# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#
#         n = len(temperatures)
#         answer = [0] * n
#
#         for i in range(n):
#
#             for j in range(i + 1, n):
#
#                 if temperatures[j] > temperatures[i]:
#                     answer[i] = j - i
#                     break
#
#         return answer
