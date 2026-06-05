"""
Problem: Top K Frequent Elements

LeetCode: 347
Difficulty: Medium

Pattern:
Bucket Sort + Frequency Count

Approach:
1. Count occurrences of each number.
2. Create buckets where index = frequency.
3. Place each number into its corresponding frequency bucket.
4. Traverse buckets from highest frequency to lowest.
5. Collect k elements.

Time Complexity:
O(n)

Space Complexity:
O(n)

Key Learning:
Bucket Sort can be used when frequencies are bounded by n.
Avoids O(n log n) sorting.
"""

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1

        for n, c in count.items():
            freq[c].append(n)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)

                if len(res) == k:
                    return res
