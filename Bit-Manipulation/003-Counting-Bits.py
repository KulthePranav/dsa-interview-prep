"""
Problem: Counting Bits

LeetCode: 338
Difficulty: Easy

Pattern:
Dynamic Programming + Bit Manipulation

Approach:
1. Maintain a DP array where dp[i] stores the number of set bits in i.
2. Track the largest power of 2 (offset) less than or equal to i.
3. The leading bit contributes one set bit.
4. Reuse the answer for the remaining value.

Formula:
dp[i] = 1 + dp[i - offset]

Alternative Solution:
Use Brian Kernighan's Algorithm for every number.

Time Complexity:
DP: O(n)
Brian Kernighan: O(n log n)

Space Complexity:
O(n)

Key Learning:
Reuse previously computed results by identifying the nearest power of 2.
"""

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:

        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):

            if offset * 2 == i:
                offset = i

            dp[i] = 1 + dp[i - offset]

        return dp


# ------------------------------------------------------------------
# Alternative Solution: Brian Kernighan's Algorithm
# ------------------------------------------------------------------

# class Solution:
#     def countBits(self, n: int) -> List[int]:
#
#         output = []
#
#         for num in range(n + 1):
#
#             count = 0
#
#             while num:
#                 count += 1
#                 num &= (num - 1)
#
#             output.append(count)
#
#         return output
