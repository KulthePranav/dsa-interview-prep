"""
Problem: Sliding Window Maximum

LeetCode: 239
Difficulty: Hard

Pattern:
Monotonic Deque

Approach:
1. Maintain a decreasing deque of indices.
2. Remove smaller elements from the back.
3. Remove elements outside the current window.
4. The front of the deque always stores the maximum.

Alternative Solution:
Brute Force

Example:
nums = [1,3,-1,-3,5,3,6,7]
k = 3

Output:
[3,3,5,5,6,7]

Time Complexity:
O(n)

Space Complexity:
O(k)

Alternative Complexity:

Brute Force:
Time: O(n × k)
Space: O(1)

Key Learning:
A monotonic deque keeps the maximum element
at the front of the window.
"""

from typing import List
import collections


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []

        q = collections.deque()  # Stores indices

        l = r = 0

        while r < len(nums):

            # Remove smaller values from the back
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            # Remove indices outside the window
            if l > q[0]:
                q.popleft()

            # Window is complete
            if r + 1 >= k:
                output.append(nums[q[0]])
                l += 1

            r += 1

        return output


# Alternative Solution: Brute Force

# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         result = []
#
#         for i in range(len(nums) - k + 1):
#             result.append(max(nums[i:i + k]))
#
#         return result
