"""
Problem: Two Sum II - Input Array Is Sorted

LeetCode: 167
Difficulty: Medium

Pattern:
Two Pointers

Approach:
1. Place one pointer at the beginning and one at the end.
2. Calculate the current sum.
3. If sum equals target, return the 1-indexed positions.
4. If sum is too small, move the left pointer right.
5. If sum is too large, move the right pointer left.

Alternative Solution:
Use a Hash Map to store previously seen numbers and check for complements.

Example:
numbers = [2, 7, 11, 15]
target = 9

2 + 15 = 17 > 9
Move right pointer

2 + 11 = 13 > 9
Move right pointer

2 + 7 = 9
Answer = [1, 2]

Time Complexity:
O(n)

Space Complexity:
O(1)

Alternative Complexity:
Hash Map:
Time: O(n)
Space: O(n)

Key Learning:
When the array is sorted and a pair condition is required,
Two Pointers is often more optimal than a Hash Map.
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            current_sum = numbers[l] + numbers[r]

            if current_sum == target:
                return [l + 1, r + 1]

            elif current_sum < target:
                l += 1

            else:
                r -= 1

        return []


# Alternative Solution (Hash Map)

# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         seen = {}
#
#         for i, num in enumerate(numbers):
#             complement = target - num
#
#             if complement in seen:
#                 return [seen[complement] + 1, i + 1]
#
#             seen[num] = i
#
#         return []
