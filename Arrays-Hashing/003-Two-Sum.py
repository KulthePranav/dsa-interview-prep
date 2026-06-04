"""
Problem: Two Sum

LeetCode: 1
Difficulty: Easy

Pattern:
Hash Map

Approach:
Traverse the array while storing previously seen numbers and their indices in a hash map.

For each number:
1. Calculate its complement (target - current number).
2. Check if the complement already exists in the hash map.
3. If found, return the indices.
4. Otherwise, store the current number and its index.

Time Complexity:
O(n)

Space Complexity:
O(n)

Key Learning:
Hash Maps can reduce pair-search problems from O(n²) to O(n) by enabling O(1) lookups.
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in prev_map:
                return [prev_map[complement], i]

            prev_map[num] = i

        return []
