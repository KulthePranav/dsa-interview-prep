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

## 424. Longest Repeating Character Replacement

**Pattern:** Variable Sliding Window + Frequency Count

**Signal:**
- Need the longest valid substring.
- Can replace at most `k` characters.
- Window expands and shrinks dynamically.

### Observation

For a window to be valid:

```text
Window Size - Frequency of Most Common Character <= k
```

The characters that are **not** the most frequent need to be replaced.

### Formula

```python
(window_size) - max_frequency <= k
```

or

```python
(r - l + 1) - max_freq <= k
```

### Approach

1. Expand the window by moving the right pointer.
2. Count character frequencies.
3. Track the highest frequency in the current window.
4. If replacements needed exceed `k`, shrink the window.
5. Track the maximum valid window length.

### Template

```python
l = 0
count = {}
res = 0
max_freq = 0

for r in range(len(s)):

    count[s[r]] = 1 + count.get(s[r], 0)

    max_freq = max(max_freq, count[s[r]])

    while (r - l + 1) - max_freq > k:
        count[s[l]] -= 1
        l += 1

    res = max(res, r - l + 1)

return res
```
### Why Do We Track `max_freq`?

Suppose:

```text
Window = AABABBA

A → 4
B → 3

max_freq = 4
```

Only the other characters need replacement.

```
Needed replacements
=
Window Size - max_freq
```

If:

```text
Needed replacements > k
```

Shrink the window.

### Why Don't We Decrease `max_freq`?

Notice that `max_freq` only increases.

Even if the most frequent character leaves the window, we **do not recalculate** it.

This is still correct because:

- A stale `max_freq` may delay shrinking the window.
- It never causes us to miss the optimal answer.
- Recomputing `max_freq` every time would increase complexity.

### Visualization

```text
s = "AABABBA"
k = 1

Window = AABA

Count:
A = 3
B = 1

Window Size = 4

Replacements Needed

4 - 3 = 1

Valid Window
```

### Alternative Solution

Recompute the maximum frequency every time the window shrinks.

```python
max_freq = max(count.values())
```

This is simpler to understand but less efficient because it scans the frequency map repeatedly.

### Comparison

| Approach | Time | Space |
|-----------|------|--------|
| Sliding Window + Running Max Frequency | O(n) | O(1) |
| Recompute Max Frequency | O(26 × n) ≈ O(n) | O(1) |

**Time:** O(n)

**Space:** O(1)

**Key Learning:**
When a window is valid based on the frequency of its most common element, keep a running maximum frequency instead of recomputing it every time.

---

## 567. Permutation in String

**Pattern:** Fixed Sliding Window + Frequency Count

**Signal:**
- Need to check every substring of length `len(s1)`.
- Order doesn't matter.
- Looking for any permutation.

### Observation

If two strings are permutations of each other, their character frequencies are identical.

Instead of sorting every substring:

```python
sorted(window) == sorted(s1)
```

maintain frequency arrays.

### Approach

1. Build the frequency array for `s1`.
2. Build the frequency array for the first window of `s2`.
3. Compare both arrays.
4. Slide the window:
   - Add the incoming character.
   - Remove the outgoing character.
5. Compare again.

### Template

```python
l1 = len(s1)
l2 = len(s2)

if l1 > l2:
    return False

s1_freq = [0] * 26
s2_freq = [0] * 26

for i in range(l1):
    s1_freq[ord(s1[i]) - ord('a')] += 1
    s2_freq[ord(s2[i]) - ord('a')] += 1

if s1_freq == s2_freq:
    return True

for i in range(l1, l2):
    s2_freq[ord(s2[i]) - ord('a')] += 1
    s2_freq[ord(s2[i - l1]) - ord('a')] -= 1

    if s1_freq == s2_freq:
        return True

return False
```

### Visualization

```text
s1 = "ab"

Target

a:1
b:1

s2 = "eidbaooo"

Window = "ei"

↓

Window = "id"

↓

Window = "db"

↓

Window = "ba"

Match Found ✓
```


### Alternative Solution

Use `collections.Counter`.

```python
from collections import Counter

target = Counter(s1)

for every window:
    if Counter(window) == target:
        return True
```

Simple, but rebuilding the counter for each window is less efficient.


### Comparison

| Approach | Time | Space |
|-----------|------|--------|
| Sliding Window + Frequency Array | O(n) | O(1) |
| Sliding Window + Counter | O(26 × n) ≈ O(n) | O(1) |
| Sort Every Window | O(n × k log k) | O(k) |


### Why Fixed Sliding Window?

Every candidate substring has the same size.

```text
Window Size = len(s1)
```

Only the window position changes.

Unlike Variable Sliding Window, the window length never changes.

**Time:** O(n)

**Space:** O(1)

**Key Learning:**
Whenever all candidate substrings have the same length, think **Fixed Sliding Window**. Frequency arrays are ideal for lowercase English letters.

---

## 76. Minimum Window Substring

**Pattern:** Variable Sliding Window + Frequency Count

**Signal:**
- Need the minimum valid substring.
- Window contains required characters.
- Window size changes dynamically.

### Observation

A window is valid when it contains every character from `t` with at least the required frequency.

Maintain:

- `count_t` → Required frequencies
- `window` → Current window frequencies
- `have` → Number of satisfied characters
- `need` → Total unique characters required

When:

```python
have == need
```

the window is valid.

### Approach

1. Count character frequencies in `t`.
2. Expand the window by moving the right pointer.
3. Update window frequencies.
4. Once all required characters are present:
   - Update the minimum answer.
   - Shrink the window from the left.
5. Repeat until the end of the string.

### Template

```python
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
```

### Visualization

```text
s = "ADOBECODEBANC"
t = "ABC"

Expand →

ADOBEC

Valid

Shrink →

DOBEC

Invalid

Expand →

DOBECODEBA

Valid

Shrink →

BANC

Smallest Valid Window
```

### Understanding `have` and `need`

Suppose:

```text
t = "AABC"
```

Required frequencies:

```text
A → 2
B → 1
C → 1
```

Then:

```python
need = 3
```

because there are **3 unique characters**.

A character contributes to `have` only when its required frequency is fully met.

Example:

```text
Window

A → 2 ✓
B → 1 ✓
C → 0 ✗

have = 2
need = 3
```
### Alternative Solution

Brute Force:

Generate every substring and check whether it contains all required characters.

Time:

```text
O(n³)
```

### Comparison

| Approach | Time | Space |
|-----------|------|--------|
| Sliding Window | O(n) | O(m) |
| Brute Force | O(n³) | O(m) |

*m = number of unique characters in `t`.*

### Pattern Recognition

```text
Need smallest valid substring?

↓

Variable Sliding Window

↓

Maintain frequencies

↓

Expand

↓

When valid → Shrink
```

**Time:** O(n)

**Space:** O(m)

**Key Learning:**
For minimum/maximum substring problems with character constraints, use a Variable Sliding Window with frequency counting and a validity check (`have == need`).

---
