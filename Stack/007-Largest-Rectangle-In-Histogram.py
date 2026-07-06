"""
Problem: Largest Rectangle in Histogram

LeetCode: 84
Difficulty: Hard

Pattern:
Monotonic Increasing Stack

Approach:
1. Maintain an increasing stack of (start_index, height).
2. When a shorter bar is encountered, pop taller bars.
3. Compute the maximum area for each popped bar.
4. Carry the earliest valid start index to the current bar.
5. Process any remaining bars after traversal.

Alternative Solution:
Compute Previous Smaller Element (PSE) and Next Smaller Element (NSE).

Time Complexity:
O(n)

Space Complexity:
O(n)

Key Learning:
A monotonic increasing stack efficiently finds the widest rectangle for every bar by determining its left and right boundaries.
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # (start_index, height)

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index

            stack.append((start, h))

        for index, height in stack:
            max_area = max(max_area, height * (len(heights) - index))

        return max_area


# ------------------------------------------------------------------
# Alternative Solution: Previous Smaller + Next Smaller
# ------------------------------------------------------------------

# 1. Find Previous Smaller Element (PSE) for every bar.
# 2. Find Next Smaller Element (NSE) for every bar.
# 3. Width = NSE - PSE - 1
# 4. Area = Height × Width
#
# Time: O(n)
# Space: O(n)
