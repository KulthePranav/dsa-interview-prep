"""
Problem: Minimum Window Substring

LeetCode: 76
Difficulty: Hard

Pattern:
Variable Sliding Window + Frequency Count

Approach:
1. Count required character frequencies.
2. Expand the window.
3. Track satisfied characters.
4. When the window becomes valid, shrink it.
5. Keep the smallest valid window.

Example:
s = "ADOBECODEBANC"
t = "ABC"

Output:
"BANC"

Time Complexity:
O(n)

Space Complexity:
O(m)

Alternative Solution:
Brute Force

Alternative Complexity:

Brute Force:
Time: O(n³)
Space: O(m)

Key Learning:
Maintain required frequencies and shrink the window
whenever all required characters are present.
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        count_t = {}
        window = {}

        for ch in t:
            count_t[ch] = 1 + count_t.get(ch, 0)

        have = 0
        need = len(count_t)

        res = [-1, -1]
        res_len = float("inf")

        l = 0

        for r in range(len(s)):

            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in count_t and window[c] == count_t[c]:
                have += 1

            while have == need:

                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                window[s[l]] -= 1

                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1

                l += 1

        l, r = res

        return s[l:r + 1] if res_len != float("inf") else ""


# Alternative Solution: Brute Force

# from collections import Counter
#
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         target = Counter(t)
#         ans = ""
#
#         for i in range(len(s)):
#             for j in range(i, len(s)):
#                 window = Counter(s[i:j+1])
#
#                 valid = True
#
#                 for ch in target:
#                     if window[ch] < target[ch]:
#                         valid = False
#                         break
#
#                 if valid:
#                     if ans == "" or len(s[i:j+1]) < len(ans):
#                         ans = s[i:j+1]
#
#         return ans
