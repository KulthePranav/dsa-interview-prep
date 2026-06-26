"""
Problem: Best Time to Buy and Sell Stock

LeetCode: 121
Difficulty: Easy

Pattern:
Sliding Window

Approach:
Track the minimum price seen so far.
For each day, calculate the profit if sold today.
Update the maximum profit.

Example:
prices = [7,1,5,3,6,4]

Buy at 1
Sell at 6

Profit = 5

Time Complexity:
O(n)

Space Complexity:
O(1)

Alternative Solution:
Sliding Window using two pointers.

Alternative Complexity:
Sliding Window
Time: O(n)
Space: O(1)

Key Learning:
Track the minimum buying price while scanning,
or use a sliding window to maintain buy and sell days.
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price

            max_profit = max(max_profit, price - min_price)

        return max_profit


# Alternative Solution: Sliding Window

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         left, right = 0, 1
#         max_profit = 0
#
#         while right < len(prices):
#             if prices[left] < prices[right]:
#                 max_profit = max(
#                     max_profit,
#                     prices[right] - prices[left]
#                 )
#             else:
#                 left = right
#
#             right += 1
#
#         return max_profit
