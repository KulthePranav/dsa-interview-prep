"""
Problem: Encode and Decode Strings

LeetCode: 271 (Premium)
Difficulty: Medium

Pattern:
Length Prefix Encoding

Approach:
Encode each string as:
    <length>#<string>

Example:
["neet", "code"]

Encoded:
"4#neet4#code"

During decoding:
1. Read digits until '#'
2. Convert digits to length
3. Read exactly 'length' characters
4. Repeat until the end of the string

Time Complexity:
Encode: O(n)
Decode: O(n)

Space Complexity:
O(n)

Key Learning:
Store metadata (length) before the actual data.
This avoids delimiter collision problems and guarantees
lossless serialization/deserialization.
"""

from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            res.append(s[j + 1 : j + 1 + length])

            i = j + 1 + length

        return res
