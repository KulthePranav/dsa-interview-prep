# Sliding Window

## 121. Best Time to Buy and Sell Stock

**Pattern:** Sliding Window

**Signal:**
- Need to compare two positions in order.
- Buy must happen before sell.
- Looking for maximum profit.

**Approach 1: Track Minimum Price (Optimal)**

1. Keep track of the minimum price seen so far.
2. For each price:
   - Calculate the profit if sold today.
   - Update the maximum profit.
3. Update the minimum price whenever a lower price is found.

**Template:**

```python
min_price = prices[0]
max_profit = 0

for price in prices:
    if price < min_price:
        min_price = price

    max_profit = max(max_profit, price - min_price)

return max_profit
```

## Alternative Solution: Sliding Window

Treat the buy day as the left pointer and the sell day as the right pointer.

If the selling price is lower than the buying price, move the buy pointer.

```python
left, right = 0, 1
max_profit = 0

while right < len(prices):

    if prices[left] < prices[right]:
        max_profit = max(max_profit, prices[right] - prices[left])
    else:
        left = right

    right += 1

return max_profit
```

### Visualization

```text
prices = [7,1,5,3,6,4]

Buy = 7
Sell = 1

Profit = -6

Move Buy

Buy = 1
Sell = 5

Profit = 4

Buy = 1
Sell = 6

Profit = 5
```

### Comparison

| Approach | Time | Space |
|-----------|------|--------|
| Track Minimum Price | O(n) | O(1) |
| Sliding Window | O(n) | O(1) |
| Brute Force | O(n²) | O(1) |

### Why This is a Sliding Window Problem

The window represents:

```text
Buy -------- Sell
 ^
left       right
```

If selling before buying is not profitable:

```text
Buy = 7
Sell = 1
```

Reset the window:

```text
Buy = 1
Sell = next day
```
**Time:** O(n)

**Space:** O(1)

**Key Learning:**
Maintain the lowest buying price seen so far (or a valid buy/sell window) to maximize profit in one pass.

---
