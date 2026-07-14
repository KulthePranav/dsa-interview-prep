"""
Problem: Merge Strings Alternately

LeetCode: 1768
Difficulty: Easy

Pattern:
Two Pointers / Parallel Traversal

Approach:
1. Traverse both strings simultaneously.
2. Append one character from each string alternately.
3. Continue until both strings are exhausted.
4. Join the character list into the final string.

Alternative Solution:
Two explicit pointers with a while loop.

Time Complexity:
O(n + m)

Space Complexity:
O(n + m)

where:
    n = len(word1)
    m = len(word2)

Key Learning:
Parallel traversal is useful when processing two sequences together. Build strings using a list and `"".join()` for efficiency.
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)

        result = []

        for i in range(max(n, m)):
            if i < n:
                result.append(word1[i])

            if i < m:
                result.append(word2[i])

        return "".join(result)


# ------------------------------------------------------------------
# Alternative Solution (Two Pointers)
# ------------------------------------------------------------------

# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         i = j = 0
#         result = []
#
#         while i < len(word1) or j < len(word2):
#
#             if i < len(word1):
#                 result.append(word1[i])
#                 i += 1
#
#             if j < len(word2):
#                 result.append(word2[j])
#                 j += 1
#
#         return "".join(result)
