"""
Problem: Single Number

LeetCode: 136
Difficulty: Easy

Pattern:
Bit Manipulation (XOR)

Approach:
1. Initialize answer as 0.
2. XOR every element with the current answer.
3. Duplicate values cancel out.
4. The remaining value is the single number.

Alternative Solution:
Use a hash set to add/remove duplicate elements.

Example:

Input:
[4,1,2,1,2]

Output:
4

Time Complexity:
O(n)

Space Complexity:
O(1)

Alternative Complexity:
Hash Set
Time: O(n)
Space: O(n)

Key Learning:
XOR eliminates duplicate values because:
a ^ a = 0
a ^ 0 = a
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        ans = 0

        for n in nums:
            ans ^= n

        return ans


# ------------------------------------------------------------------
# Alternative Solution: Hash Set
# ------------------------------------------------------------------

# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#
#         hashset = set()
#
#         for n in nums:
#
#             if n in hashset:
#                 hashset.remove(n)
#
#             else:
#                 hashset.add(n)
#
#         return hashset.pop()
