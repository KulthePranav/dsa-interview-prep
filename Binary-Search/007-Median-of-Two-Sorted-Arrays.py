"""
Problem: Median of Two Sorted Arrays

LeetCode: 4
Difficulty: Hard

Pattern:
Binary Search on Partition

Approach:
1. Always binary search the smaller array.
2. Partition both arrays into left and right halves.
3. Ensure:
   max(left) <= min(right)
4. Compute the median based on the total number of elements.

Alternative Solution:
Merge both arrays, sort them, and return the median.

Time Complexity:
O(log(min(m,n)))

Space Complexity:
O(1)

Key Learning:
Instead of merging two sorted arrays, binary search the partition point of the smaller array.
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        A, B = nums1, nums2

        total = len(A) + len(B)
        half = total // 2

        left, right = 0, len(A)

        while True:

            i = (left + right) // 2
            j = half - i

            Aleft = A[i - 1] if i > 0 else float("-inf")
            Aright = A[i] if i < len(A) else float("inf")

            Bleft = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j] if j < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:

                if total % 2:
                    return min(Aright, Bright)

                return (
                    max(Aleft, Bleft)
                    + min(Aright, Bright)
                ) / 2

            elif Aleft > Bright:
                right = i - 1

            else:
                left = i + 1


# ------------------------------------------------------------------
# Alternative Solution (Brute Force)
# ------------------------------------------------------------------

# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#
#         merged = sorted(nums1 + nums2)
#
#         mid = len(merged) // 2
#
#         if len(merged) % 2 == 0:
#             return (merged[mid - 1] + merged[mid]) / 2
#
#         return merged[mid]
