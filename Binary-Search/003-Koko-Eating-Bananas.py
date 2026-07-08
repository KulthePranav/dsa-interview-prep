"""
Problem: Koko Eating Bananas

LeetCode: 875
Difficulty: Medium

Pattern:
Binary Search on Answer

Approach:
1. Search possible eating speeds from 1 to max(piles).
2. For each speed, calculate the total hours required.
3. If Koko can finish within h hours, try a smaller speed.
4. Otherwise, increase the speed.

Alternative Solution:
Use integer ceiling division instead of math.ceil().

Time Complexity:
O(n log m)

Space Complexity:
O(1)

where:
n = number of piles
m = maximum pile size

Key Learning:
Binary Search can be performed on the answer space when the feasibility is monotonic.
"""

import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        while left <= right:
            middle = (left + right) // 2
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / middle)

            if hours <= h:
                res = middle
                right = middle - 1
            else:
                left = middle + 1

        return res


# ------------------------------------------------------------------
# Alternative Solution: Integer Ceiling Division (Preferred)
# ------------------------------------------------------------------

# class Solution:
#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
#         left, right = 1, max(piles)
#         res = right
#
#         while left <= right:
#             mid = (left + right) // 2
#             hours = 0
#
#             for pile in piles:
#                 hours += (pile + mid - 1) // mid
#
#             if hours <= h:
#                 res = mid
#                 right = mid - 1
#             else:
#                 left = mid + 1
#
#         return res
