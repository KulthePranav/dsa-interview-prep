"""
Problem: Longest Repeating Character Replacement

LeetCode: 424
Difficulty: Medium

Pattern:
Variable Sliding Window + Frequency Count

Approach:
1. Expand the window.
2. Count character frequencies.
3. Track the maximum character frequency.
4. Shrink the window if replacements needed exceed k.
5. Track the maximum valid window size.

Alternative Solution:
Recompute the maximum frequency whenever the window shrinks.

Example:
s = "AABABBA"
k = 1

Longest valid substring length = 4

Time Complexity:
O(n)

Space Complexity:
O(1)

Alternative Complexity:
Time: O(26 × n) ≈ O(n)
Space: O(1)

Key Learning:
Keep a running maximum frequency to determine
whether the current window can be made uniform
with at most k replacements.
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        res = 0
        max_freq = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            max_freq = max(max_freq, count[s[r]])

            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res


# Alternative Solution: Recompute Maximum Frequency

# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         l = 0
#         count = {}
#         res = 0
#
#         for r in range(len(s)):
#             count[s[r]] = 1 + count.get(s[r], 0)
#
#             while (r - l + 1) - max(count.values()) > k:
#                 count[s[l]] -= 1
#
#                 if count[s[l]] == 0:
#                     del count[s[l]]
#
#                 l += 1
#
#             res = max(res, r - l + 1)
#
#         return res
