"""
Problem: Search a 2D Matrix

LeetCode: 74
Difficulty: Medium

Pattern:
Binary Search (Two Binary Searches)

Approach:
1. Binary Search to find the candidate row.
2. Binary Search within that row.

Alternative Solution:
Treat the matrix as a single sorted array.

Time Complexity:
O(log m + log n)

Space Complexity:
O(1)

Key Learning:
A globally sorted matrix can be searched either by two Binary Searches or by flattening it conceptually into a 1D sorted array.
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            m = (l + r) // 2

            if matrix[m][0] <= target <= matrix[m][-1]:

                left, right = 0, len(matrix[m]) - 1

                while left <= right:
                    middle = (left + right) // 2

                    if matrix[m][middle] == target:
                        return True

                    elif target < matrix[m][middle]:
                        right = middle - 1

                    else:
                        left = middle + 1

                return False

            elif target < matrix[m][0]:
                r = m - 1

            else:
                l = m + 1

        return False


# ------------------------------------------------------------------
# Alternative Solution: Treat Matrix as 1D Array
# ------------------------------------------------------------------

# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#
#         rows = len(matrix)
#         cols = len(matrix[0])
#
#         left, right = 0, rows * cols - 1
#
#         while left <= right:
#
#             mid = (left + right) // 2
#
#             row = mid // cols
#             col = mid % cols
#
#             if matrix[row][col] == target:
#                 return True
#
#             elif target < matrix[row][col]:
#                 right = mid - 1
#
#             else:
#                 left = mid + 1
#
#         return False
