"""
Problem: Reverse Bits

LeetCode: 190
Difficulty: Easy

Pattern:
Bit Manipulation (Bit Shifting)

Approach:
1. Iterate through all 32 bits.
2. Extract the current bit.
3. Place it in the mirrored position.
4. Build the reversed number using OR.

Alternative Solution:
Shift the result left while reading bits from right to left.

Example:

Input:
00000010100101000001111010011100

Output:
00111001011110000010100101000000

Time Complexity:
O(32) ≈ O(1)

Space Complexity:
O(1)

Key Learning:
Use right shift to extract bits and left shift to place them in reversed positions.
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res |= bit << (31 - i)

        return res


# ------------------------------------------------------------------
# Alternative Solution: Shift Result
# ------------------------------------------------------------------

# class Solution:
#     def reverseBits(self, n: int) -> int:
#
#         res = 0
#
#         for _ in range(32):
#             res = (res << 1) | (n & 1)
#             n >>= 1
#
#         return res
