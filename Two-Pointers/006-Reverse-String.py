"""
Problem: Reverse String

LeetCode: 344
Difficulty: Easy

Pattern:
Two Pointers (In-place Swapping)

Approach:
1. Initialize two pointers at both ends of the array.
2. Swap the characters.
3. Move pointers toward the center.
4. Continue until they meet.

Alternative Solutions:
1. Use list.reverse()
2. Use slicing (s[:] = s[::-1])

Time Complexity:
O(n)

Space Complexity:
O(1)

Alternative (Slicing):
Time: O(n)
Space: O(n)

Key Learning:
Two pointers are ideal for in-place reversal problems.
"""

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        l, r = 0, len(s) - 1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1


# ------------------------------------------------------------------
# Alternative Solution 1: Built-in reverse()
# ------------------------------------------------------------------

# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         s.reverse()


# ------------------------------------------------------------------
# Alternative Solution 2: Slicing
# ------------------------------------------------------------------

# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         s[:] = s[::-1]
