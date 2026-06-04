"""
Problem: Contains Duplicate

LeetCode: 217
Difficulty: Easy

Pattern:
Hash Set

Approach:
Iterate through the array while maintaining a hash set.
If a number is already present in the set, a duplicate exists.
Otherwise, add the number to the set.

Time Complexity:
O(n)

Space Complexity:
O(n)

Key Learning:
Hash sets provide O(1) average lookup and insertion.
Useful for duplicate detection problems.
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)

        return False

# Alternative one-liner:
# return len(set(nums)) != len(nums)
