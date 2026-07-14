"""
Problem: Valid Palindrome II

LeetCode: 680
Difficulty: Easy

Pattern:
Two Pointers + Greedy

Approach:
1. Use two pointers from both ends.
2. Move inward while characters match.
3. On the first mismatch:
   - Skip the left character.
   - Skip the right character.
4. If either remaining substring is a palindrome, return True.

Alternative Solution:
Recursive DFS with a deletion flag.

Time Complexity:
O(n)

Space Complexity:
O(1)

Key Learning:
After the first mismatch, only two choices exist:
remove the left character or remove the right character.
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:

        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return (
                    is_palindrome(l + 1, r) or
                    is_palindrome(l, r - 1)
                )

            l += 1
            r -= 1

        return True


# ------------------------------------------------------------------
# Alternative Solution (Recursive)
# ------------------------------------------------------------------

# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#
#         def dfs(l, r, deleted):
#             while l < r:
#                 if s[l] != s[r]:
#                     if deleted:
#                         return False
#
#                     return (
#                         dfs(l + 1, r, True) or
#                         dfs(l, r - 1, True)
#                     )
#
#                 l += 1
#                 r -= 1
#
#             return True
#
#         return dfs(0, len(s) - 1, False)
