"""
Problem: Time Based Key-Value Store

LeetCode: 981
Difficulty: Medium

Pattern:
Hash Map + Binary Search

Approach:
1. Store values for each key in chronological order.
2. Append new (value, timestamp) pairs.
3. Use Binary Search to find the latest timestamp <= target.

Alternative Solution:
Use Python's bisect_right.

Time Complexity:
set() : O(1)
get() : O(log n)

Space Complexity:
O(n)

Key Learning:
Binary Search can efficiently retrieve historical records when timestamps are stored in sorted order.
"""

from typing import Dict, List


class TimeMap:

    def __init__(self):
        self.store: Dict[str, List[List]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key, [])

        left, right = 0, len(values) - 1
        result = ""

        while left <= right:
            mid = (left + right) // 2

            if values[mid][1] <= timestamp:
                result = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1

        return result


# ------------------------------------------------------------------
# Alternative Solution: bisect_right
# ------------------------------------------------------------------

# from bisect import bisect_right
#
# class TimeMap:
#
#     def __init__(self):
#         self.store = {}
#
#     def set(self, key, value, timestamp):
#         self.store.setdefault(key, []).append((timestamp, value))
#
#     def get(self, key, timestamp):
#         values = self.store.get(key, [])
#
#         idx = bisect_right(values, (timestamp, chr(127))) - 1
#
#         return values[idx][1] if idx >= 0 else ""
