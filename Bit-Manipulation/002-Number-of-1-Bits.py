"""
Problem: Number of 1 Bits

LeetCode: 191
Difficulty: Easy

Pattern:
Bit Manipulation (Brian Kernighan's Algorithm)

Approach:
1. Initialize count = 0.
2. While n is not zero:
   - Increment count.
   - Remove the rightmost set bit using:
       n = n & (n - 1)
3. Return count.

Alternative Solution:
Check every bit using division/modulo.

Example:

Input:
13

Binary:
1101

Output:
3

Time Complexity:
O(k), where k is the number of set bits.

Space Complexity:
O(1)

Alternative Complexity:
Time: O(number of bits)
Space: O(1)

Key Learning:
n & (n - 1) removes the rightmost set bit.
"""

class Solution:
    def hammingWeight(self, n: int) -> int:

        count = 0

        while n:
            count += 1
            n = n & (n - 1)

        return count


# ------------------------------------------------------------------
# Alternative Solution: Check Every Bit
# ------------------------------------------------------------------

# class Solution:
#     def hammingWeight(self, n: int) -> int:
#
#         count = 0
#
#         while n:
#
#             if n % 2 == 1:
#                 count += 1
#
#             n //= 2
#
#         return count
