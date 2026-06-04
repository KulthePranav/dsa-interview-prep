"""
Problem: Valid Anagram

LeetCode: 242
Difficulty: Easy

Pattern:
Frequency Count / Hash Map

Time Complexity:
O(n)

Space Complexity:
O(1) for fixed alphabet
O(n) in general

Key Learning:
Compare character frequencies rather than sorting.
"""

from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_table = {}

        for char in s:
            count_table[char] = count_table.get(char, 0) + 1

        for char in t:
            if char not in count_table:
                return False

            count_table[char] -= 1

            if count_table[char] < 0:
                return False

        return True

# Alternative:
# return sorted(s) == sorted(t)
