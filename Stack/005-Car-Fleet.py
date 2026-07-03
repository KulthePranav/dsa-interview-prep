"""
Problem: Car Fleet

LeetCode: 853
Difficulty: Medium

Pattern:
Monotonic Stack (Arrival Time)

Approach:
1. Pair each car's position and speed.
2. Sort cars from closest to the target to farthest.
3. Compute each car's arrival time.
4. Maintain a monotonic stack of fleet arrival times.
5. If the current car catches the fleet ahead,
   merge by removing the current arrival time.
6. The stack size is the number of fleets.

Alternative Solution:
Track only the last fleet's arrival time instead of using an explicit stack.

Example:

Target = 12

Position = [10,8,5,3,0]
Speed    = [2,4,1,3,1]

Output:
3

Time Complexity:
O(n log n)

Space Complexity:
O(n)

Alternative Complexity:
Time: O(n log n)
Space: O(1)

Key Learning:
Sort cars by position and compare arrival times.
If a car behind arrives earlier, it merges into the fleet ahead.
"""

from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []

        for p, s in sorted(pair, reverse=True):

            arrival_time = (target - p) / s
            stack.append(arrival_time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)


# ------------------------------------------------------------------
# Alternative Solution: Track Last Fleet Time
# ------------------------------------------------------------------

# class Solution:
#     def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
#
#         fleets = 0
#         last_time = 0
#
#         for p, s in sorted(zip(position, speed), reverse=True):
#
#             arrival_time = (target - p) / s
#
#             if arrival_time > last_time:
#                 fleets += 1
#                 last_time = arrival_time
#
#         return fleets
