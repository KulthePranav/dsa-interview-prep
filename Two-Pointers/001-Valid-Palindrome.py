"""
Problem: Valid Palindrome

LeetCode: 125
Difficulty: Easy

Pattern:
Two Pointers

Approach:
1. Use two pointers:
   - Left starts from the beginning.
   - Right starts from the end.
2. Skip non-alphanumeric characters.
3. Compare characters case-insensitively.
4. If a mismatch is found, return False.
5. Continue until the pointers meet.

Alternative Solution:
1. Build a new string containing only lowercase alphanumeric characters.
2. Compare the cleaned string with its reverse.

Example:
Input:
"A man, a plan, a canal: Panama"

Processed:
"amanaplanacanalpanama"

Output:
True

Time Complexity:
O(n)

Space Complexity:
O(1)

Alternative Solution Complexity:
Time: O(n)
Space: O(n)

Pros of Alternative:
- Easier to understand
- Less code

Pros of Current Approach:
- Optimal space complexity
- More interview-friendly

Key Learning:
Two pointers are useful when comparing elements from both ends
of a sequence and can often reduce space complexity.
"""

from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.is_al_num(s[l]):
                l += 1

            while r > l and not self.is_al_num(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l, r = l + 1, r - 1

        return True

    def is_al_num(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )


# Alternative Solution

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         cleaned = ""
#
#         for c in s:
#             if c.isalnum():
#                 cleaned += c.lower()
#
#         return cleaned == cleaned[::-1]
