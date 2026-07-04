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
