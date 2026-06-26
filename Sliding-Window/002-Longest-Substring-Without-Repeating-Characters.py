"""
Problem: Longest Substring Without Repeating Characters

LeetCode: 3
Difficulty: Medium

Pattern:
Variable Sliding Window + Hash Set

Approach:
1. Maintain a sliding window with unique characters.
2. Expand the window by moving the right pointer.
3. If a duplicate is found, shrink the window from the left.
4. Track the maximum window size.

Alternative Solution:
Sliding Window + Hash Map (stores last seen indices).

Example:
s = "abcabcbb"

Longest substring:
"abc"

Length = 3

Time Complexity:
O(n)

Space Complexity:
O(min(n, m))

Alternative Complexity:
Hash Map:
Time: O(n)
Space: O(min(n, m))

Key Learning:
Use a Hash Set for uniqueness, or a Hash Map to jump directly past duplicate characters.
"""

from typing import Dict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in hash_set:
                hash_set.remove(s[l])
                l += 1

            hash_set.add(s[r])
            res = max(res, r - l + 1)

        return res


# Alternative Solution: Sliding Window + Hash Map

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         last_seen: Dict[str, int] = {}
#         l = 0
#         res = 0
#
#         for r, ch in enumerate(s):
#             if ch in last_seen:
#                 l = max(l, last_seen[ch] + 1)
#
#             last_seen[ch] = r
#             res = max(res, r - l + 1)
#
#         return res
