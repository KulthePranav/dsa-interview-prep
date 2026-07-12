"""
Problem: Longest Common Prefix

LeetCode: 14
Difficulty: Easy

Pattern:
Prefix Reduction

Approach:
1. Assume the first string is the common prefix.
2. Compare it with every other string.
3. Reduce the prefix until the current string starts with it.
4. Return the remaining prefix.

Alternative Solutions:
1. Character-by-character comparison using zip().
2. Sorting the strings and comparing the first and last.

Time Complexity:
O(n × m)

Space Complexity:
O(1)

where:
n = number of strings
m = length of the shortest string

Key Learning:
The common prefix can only decrease in length, never increase.
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        prefix = strs[0]

        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]

                if prefix == "":
                    return ""

        return prefix


# ------------------------------------------------------------------
# Alternative Solution 1 (Character-by-Character)
# ------------------------------------------------------------------

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ""
#
#         prefix = ""
#
#         for chars in zip(*strs):
#             if len(set(chars)) == 1:
#                 prefix += chars[0]
#             else:
#                 break
#
#         return prefix


# ------------------------------------------------------------------
# Alternative Solution 2 (Sorting)
# ------------------------------------------------------------------

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ""
#
#         strs.sort()
#
#         first = strs[0]
#         last = strs[-1]
#
#         i = 0
#         while i < len(first) and i < len(last) and first[i] == last[i]:
#             i += 1
#
#         return first[:i]
