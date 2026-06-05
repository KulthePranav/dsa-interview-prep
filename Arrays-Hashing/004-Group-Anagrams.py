"""
Problem: Group Anagrams

LeetCode: 49
Difficulty: Medium

Pattern:
Hash Map + Frequency Count

Approach:
1. Create a frequency count array of size 26 for each word.
2. Use the frequency array (converted to a tuple) as the hash map key.
3. Words with the same character frequencies belong to the same group.
4. Return all grouped values.

Time Complexity:
O(n * k)

n = number of strings
k = average length of string

Space Complexity:
O(n * k)

Key Learning:
When grouping strings based on character frequencies,
a frequency count tuple can be used as a unique hashable key.
"""

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for char in s:
                count[ord(char) - ord('a')] += 1

            res[tuple(count)].append(s)

        return list(res.values())


# 0(n * klogk)
# res = {}
# for s in strs:
#     key = tuple(sorted(s)) #type: tuple
#     #key = "".join(sorted(s)) #type: str
#     if key not in res:
#         res[key] = []
#     res[key].append(s)
        
# return list(res.values())
