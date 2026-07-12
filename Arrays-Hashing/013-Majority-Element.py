"""
Problem: Majority Element

LeetCode: 169
Difficulty: Easy

Pattern:
Boyer-Moore Voting Algorithm

Approach:
1. Maintain a candidate and a counter.
2. If the counter becomes zero, choose the current element as the new candidate.
3. Increment the counter if the current element equals the candidate.
4. Otherwise, decrement the counter.
5. The remaining candidate is the majority element.

Alternative Solutions:
1. Hash Map
2. Sorting
3. Brute Force using count()

Time Complexity:
O(n)

Space Complexity:
O(1)

Key Learning:
Different elements cancel each other out in pairs. Since the majority element appears more than n/2 times, it will always remain.
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate


# ------------------------------------------------------------------
# Alternative Solution 1 (Hash Map)
# ------------------------------------------------------------------

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         count = {}
#
#         for num in nums:
#             count[num] = count.get(num, 0) + 1
#
#             if count[num] > len(nums) // 2:
#                 return num


# ------------------------------------------------------------------
# Alternative Solution 2 (Sorting)
# ------------------------------------------------------------------

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         nums.sort()
#         return nums[len(nums) // 2]


# ------------------------------------------------------------------
# Alternative Solution 3 (Brute Force)
# ------------------------------------------------------------------

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         majority = len(nums) // 2
#
#         for num in set(nums):
#             if nums.count(num) > majority:
#                 return num
