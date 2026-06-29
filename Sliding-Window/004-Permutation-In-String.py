"""
Problem: Permutation in String

LeetCode: 567
Difficulty: Medium

Pattern:
Fixed Sliding Window + Frequency Count

Approach:
1. Build frequency arrays for s1 and the first window of s2.
2. Compare the arrays.
3. Slide the window by adding one character and removing one character.
4. Compare the frequency arrays after each shift.

Example:
s1 = "ab"
s2 = "eidbaooo"

Window:
"ba"

Permutation found.

Time Complexity:
O(n)

Space Complexity:
O(1)

Alternative Solution:
Use collections.Counter for frequency counting.

Alternative Complexity:

Counter:
Time: O(26 × n) ≈ O(n)
Space: O(1)

Key Learning:
For fixed-size substring problems, use a Fixed Sliding Window with frequency counting.
"""

from typing import List


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)

        if l1 > l2:
            return False

        s1_freq = [0] * 26
        s2_freq = [0] * 26

        for i in range(l1):
            s1_freq[ord(s1[i]) - ord("a")] += 1
            s2_freq[ord(s2[i]) - ord("a")] += 1

        if s1_freq == s2_freq:
            return True

        for i in range(l1, l2):
            s2_freq[ord(s2[i]) - ord("a")] += 1
            s2_freq[ord(s2[i - l1]) - ord("a")] -= 1

            if s1_freq == s2_freq:
                return True

        return False


# Alternative Solution: Counter

# from collections import Counter
#
# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         l1 = len(s1)
#
#         if l1 > len(s2):
#             return False
#
#         target = Counter(s1)
#
#         for i in range(len(s2) - l1 + 1):
#             if Counter(s2[i:i + l1]) == target:
#                 return True
#
#         return False
