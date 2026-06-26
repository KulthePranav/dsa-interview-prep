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

## 3. Longest Substring Without Repeating Characters

**Pattern:** Variable Sliding Window + Hash Set

**Signal:**
- Need the longest substring.
- Characters must be unique.
- Window size changes dynamically.

**Approach:**
1. Use two pointers (`l` and `r`) to represent the current window.
2. Expand the window by moving `r`.
3. If a duplicate character is found:
   - Remove characters from the left.
   - Continue until the window becomes valid.
4. Update the maximum window size.

**Template:**

```python
hash_set = set()
l = 0
res = 0

for r in range(len(s)):
    while s[r] in hash_set:
        hash_set.remove(s[l])
        l += 1

    hash_set.add(s[r])
    res = max(res, r - l + 1)

return res
```

### Visualization

```text
s = "abcabcbb"

Window: "abc"
Length = 3

Next character = 'a'

Duplicate found

Remove:
'a'

Window:
"bc"

Add:
'a'

Window:
"bca"

Continue...
```
### Alternative Solution: Hash Map

Instead of removing one character at a time, store the last seen index.

```python
last_seen = {}
l = 0
res = 0

for r, ch in enumerate(s):

    if ch in last_seen:
        l = max(l, last_seen[ch] + 1)

    last_seen[ch] = r
    res = max(res, r - l + 1)

return res
```

### Comparison

| Approach | Time | Space |
|-----------|------|--------|
| Sliding Window + Hash Set | O(n) | O(min(n, m)) |
| Sliding Window + Hash Map | O(n) | O(min(n, m)) |
| Brute Force | O(n³) | O(1) |

*m = size of the character set.*

### Why Variable Sliding Window?

The window size changes depending on whether it contains duplicate characters.

```text
abc

↓

abca

↓

Duplicate

↓

bca
```

Unlike a fixed-size window, this window expands and shrinks dynamically.

**Time:** O(n)

**Space:** O(min(n, m))

**Key Learning:**
Whenever the problem asks for the longest or shortest contiguous substring under a constraint, think **Variable Sliding Window**.

---
