## 136. Single Number

**Pattern:** Bit Manipulation (XOR)

**Signal:**
- Every number appears twice except one.
- Need constant extra space.
- Duplicate values cancel each other.

### Why XOR?

XOR has these important properties:

```python
a ^ a = 0
```

```python
a ^ 0 = a
```

```python
a ^ b ^ a = b
```

Since XOR is associative and commutative, duplicate numbers eliminate each other.

### Example

```text
nums = [4,1,2,1,2]
```

```
0 ^ 4 = 4
4 ^ 1 = 5
5 ^ 2 = 7
7 ^ 1 = 6
6 ^ 2 = 4
```

Answer:

```text
4
```

### Approach

1. Initialize answer as `0`.
2. XOR every number with the current answer.
3. Duplicate numbers become `0`.
4. The remaining value is the unique number.

### Template

```python
ans = 0

for n in nums:
    ans ^= n

return ans
```
### Alternative Solution (Hash Set)

```python
hashset = set()

for n in nums:

    if n in hashset:
        hashset.remove(n)

    else:
        hashset.add(n)

return hashset.pop()
```

The set contains only the number that appears once.

### Comparison

| Approach | Time | Space |
|-----------|------|--------|
| XOR | O(n) | O(1) |
| Hash Set | O(n) | O(n) |

### Pattern Recognition

```text
Every element appears twice?

↓

Need unique element?

↓

Need O(1) space?

↓

Use XOR
```

**Time:** O(n)

**Space:** O(1)

**Key Learning:**
Whenever duplicate values cancel each other and only one unique value remains, XOR is often the optimal solution.

---

## 191. Number of 1 Bits

**Pattern:** Bit Manipulation (Brian Kernighan's Algorithm)

**Signal:**
- Need to count set bits.
- Binary representation matters.
- Optimize beyond checking every bit.

### Brute Force Idea

Check every bit individually.

```python
count = 0

while n:

    count += n % 2

    n //= 2
```

Time:

```text
O(number of bits)
```

### Better Observation

Consider:

```text
n = 12

Binary

1100
```

Subtract one:

```text
1011
```

Now AND them:

```text
1100
1011
----
1000
```

The **rightmost set bit disappears**.

### Brian Kernighan's Algorithm

```python
n = n & (n - 1)
```

This removes exactly one `1` bit.

Repeat until:

```python
n == 0
```

The number of iterations equals the number of set bits.

### Example

```
13

1101
```

Iteration 1

```
1101
1100
----
1100
```

Iteration 2

```
1100
1011
----
1000
```

Iteration 3

```
1000
0111
----
0000
```

Answer:

```
3
```

### Approach

1. Initialize count as 0.
2. While `n` is non-zero:
   - Increment count.
   - Remove the rightmost set bit.
3. Return count.

### Template

```python
count = 0

while n:
    count += 1
    n = n & (n - 1)

return count
```

### Alternative Solution (Brute Force)

```python
count = 0

while n:

    if n % 2 == 1:
        count += 1

    n //= 2

return count
```

### Comparison

| Approach | Time | Space |
|-----------|------|--------|
| Brian Kernighan | O(k) | O(1) |
| Check Every Bit | O(32) or O(number of bits) | O(1) |

`k = number of set bits`


### Pattern Recognition

```text
Need number of 1s?

↓

Bit manipulation?

↓

Use n & (n - 1)
```

**Time:** O(k)

**Space:** O(1)

**Key Learning:**
Each `n & (n - 1)` removes one set bit, making the algorithm proportional to the number of `1`s rather than the total number of bits.

---

## 338. Counting Bits

**Pattern:** Dynamic Programming + Bit Manipulation

**Signal:**
- Need the count of set bits for every number.
- Results for smaller numbers can be reused.
- Looking for better than O(n log n).

### Brute Force Idea

For every number:

1. Count set bits using Brian Kernighan's Algorithm.
2. Store the answer.

```python
output = []

for num in range(n + 1):

    count = 0

    while num:
        count += 1
        num &= (num - 1)

    output.append(count)
```

Time:

```
O(n log n)
```

## Better Observation

Look at the answers:

| Number | Binary | Set Bits |
|--------:|:------:|---------:|
| 0 | 000 | 0 |
| 1 | 001 | 1 |
| 2 | 010 | 1 |
| 3 | 011 | 2 |
| 4 | 100 | 1 |
| 5 | 101 | 2 |
| 6 | 110 | 2 |
| 7 | 111 | 3 |
| 8 |1000 | 1 |

Notice:

```
4 = 100

5 = 100 + 001

6 = 100 + 010

7 = 100 + 011
```

The leading `1` contributes one set bit.

Everything after it has already been computed.

Therefore:

```
bits(6)

=

1 + bits(2)
```

# Offset Technique (Counting Bits)

## What is Offset?

The **offset** is the largest power of 2 less than or equal to the current number.

Example:

| i | Offset |
|---|--------|
| 1 | 1 |
| 2 | 2 |
| 3 | 2 |
| 4 | 4 |
| 5 | 4 |
| 6 | 4 |
| 7 | 4 |
| 8 | 8 |

---

## DP Formula

```python
dp[i] = 1 + dp[i - offset]
```

The leading `1` (power of 2) contributes one set bit, and `dp[i - offset]` has already been computed.

---

## Updating Offset

Whenever `i` reaches the next power of 2:

```python
if offset * 2 == i:
    offset = i
```

---

## Example

```
i = 6

offset = 4

6 = 4 + 2

dp[6] = 1 + dp[2]
```

### Approach

1. Initialize DP array.
2. Keep track of the current power of two.
3. Compute answers using previously computed values.

### Template

```python
dp = [0] * (n + 1)

offset = 1

for i in range(1, n + 1):

    if offset * 2 == i:
        offset = i

    dp[i] = 1 + dp[i - offset]

return dp
```

### Alternative Solution (Brian Kernighan)

```python
output = []

for num in range(n + 1):

    count = 0

    while num:
        count += 1
        num &= (num - 1)

    output.append(count)

return output
```

### Comparison

| Approach | Time | Space |
|-----------|------|--------|
| DP + Offset | O(n) | O(n) |
| Brian Kernighan | O(n log n) | O(n) |


### Pattern Recognition

```
Need answers for every number?

↓

Can previous answers help?

↓

DP

↓

Power of 2 involved?

↓

Use Offset
```

**Time:** O(n)

**Space:** O(n)

**Key Learning:**
Numbers between two consecutive powers of 2 share the same pattern. The current answer equals one (for the leading set bit) plus the answer for the remaining part.

---
