"""
Problem: Design HashMap

LeetCode: 706
Difficulty: Easy

Pattern:
Hash Table (Separate Chaining)

Approach:
1. Create fixed-size buckets.
2. Map each key to a bucket using modulo hashing.
3. Store (key, value) pairs inside each bucket.
4. Update the value if the key already exists.
5. Handle collisions using Separate Chaining.

Alternative Solutions:
1. Large Array
2. List of (key, value) pairs

Time Complexity:
Average:
    Put      O(1)
    Get      O(1)
    Remove   O(1)

Worst Case:
    O(n)

Space Complexity:
O(n)

Key Learning:
HashMaps store key-value pairs inside buckets. Separate Chaining efficiently resolves collisions while maintaining average O(1) operations.
"""


class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        bucket = self.buckets[key % self.size]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    def get(self, key: int) -> int:
        bucket = self.buckets[key % self.size]

        for k, v in bucket:
            if k == key:
                return v

        return -1

    def remove(self, key: int) -> None:
        bucket = self.buckets[key % self.size]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return


# ------------------------------------------------------------------
# Alternative Solution 1 (Large Array)
# ------------------------------------------------------------------

# class MyHashMap:
#
#     def __init__(self):
#         self.map = [-1] * 1000001
#
#     def put(self, key: int, value: int) -> None:
#         self.map[key] = value
#
#     def get(self, key: int) -> int:
#         return self.map[key]
#
#     def remove(self, key: int) -> None:
#         self.map[key] = -1


# ------------------------------------------------------------------
# Alternative Solution 2 (List of Key-Value Pairs)
# ------------------------------------------------------------------

# class MyHashMap:
#
#     def __init__(self):
#         self.map = []
#
#     def put(self, key: int, value: int) -> None:
#         for i, (k, v) in enumerate(self.map):
#             if k == key:
#                 self.map[i] = (key, value)
#                 return
#
#         self.map.append((key, value))
#
#     def get(self, key: int) -> int:
#         for k, v in self.map:
#             if k == key:
#                 return v
#
#         return -1
#
#     def remove(self, key: int) -> None:
#         for i, (k, v) in enumerate(self.map):
#             if k == key:
#                 self.map.pop(i)
#                 return
