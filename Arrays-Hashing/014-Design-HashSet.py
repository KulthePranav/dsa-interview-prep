"""
Problem: Design HashSet

LeetCode: 705
Difficulty: Easy

Pattern:
Hash Table (Separate Chaining)

Approach:
1. Create fixed-size buckets.
2. Map each key to a bucket using modulo hashing.
3. Store keys inside the bucket.
4. Handle collisions using Separate Chaining.

Alternative Solutions:
1. Boolean Array
2. List

Time Complexity:
Average:
    Add       O(1)
    Remove    O(1)
    Contains  O(1)

Worst Case:
    O(n)

Space Complexity:
O(n)

Key Learning:
Hash tables achieve average O(1) operations by distributing keys across buckets and resolving collisions with Separate Chaining.
"""


class MyHashSet:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        bucket = self.buckets[key % self.size]

        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        bucket = self.buckets[key % self.size]

        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        bucket = self.buckets[key % self.size]
        return key in bucket


# ------------------------------------------------------------------
# Alternative Solution 1 (Boolean Array)
# ------------------------------------------------------------------

# class MyHashSet:
#
#     def __init__(self):
#         self.hashset = [False] * 1000001
#
#     def add(self, key: int) -> None:
#         self.hashset[key] = True
#
#     def remove(self, key: int) -> None:
#         self.hashset[key] = False
#
#     def contains(self, key: int) -> bool:
#         return self.hashset[key]


# ------------------------------------------------------------------
# Alternative Solution 2 (List)
# ------------------------------------------------------------------

# class MyHashSet:
#
#     def __init__(self):
#         self.hashset = []
#
#     def add(self, key: int) -> None:
#         if key not in self.hashset:
#             self.hashset.append(key)
#
#     def remove(self, key: int) -> None:
#         if key in self.hashset:
#             self.hashset.remove(key)
#
#     def contains(self, key: int) -> bool:
#         return key in self.hashset
