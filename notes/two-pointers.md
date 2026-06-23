# Two Pointers

## 125. Valid Palindrome

**Pattern:** Two Pointers

**Signal:**
- Need to compare elements from both ends.
- Palindrome or symmetry-related problem.
- Looking for O(1) extra space.

**Approach:**
1. Place one pointer at the beginning and one at the end.
2. Skip non-alphanumeric characters.
3. Compare lowercase versions of both characters.
4. If they differ, return `False`.
5. Move pointers inward and continue.

**Template:**

```python
l, r = 0, len(s) - 1

while l < r:
    if s[l] != s[r]:
        return False

    l += 1
    r -= 1
```

**Actual Logic:**

```python
while l < r:
    while l < r and not is_al_num(s[l]):
        l += 1

    while l < r and not is_al_num(s[r]):
        r -= 1

    if s[l].lower() != s[r].lower():
        return False

    l += 1
    r -= 1
```

**Alternative Solution:**

```python
cleaned = ""

for c in s:
    if c.isalnum():
        cleaned += c.lower()

return cleaned == cleaned[::-1]
```

### Comparison

| Approach | Time | Space |
|-----------|------|--------|
| Two Pointers | O(n) | O(1) |
| Clean + Reverse | O(n) | O(n) |

**Why Two Pointers?**
- No extra string creation.
- Better space complexity.
- Common interview pattern.

**Time:** O(n)

**Space:** O(1)

**Key Learning:**
Two pointers are ideal when comparing elements from both ends of a string or array.

---

## 167. Two Sum II - Input Array Is Sorted

**Pattern:** Two Pointers

**Signal:**
- Input array is sorted.
- Need to find a pair that sums to a target.
- Only one valid answer exists.

**Approach:**
1. Place one pointer at the beginning and one at the end.
2. Calculate the current sum.
3. If sum equals target, return the indices.
4. If sum is too small, move left pointer right.
5. If sum is too large, move right pointer left.

**Template:**

```python
l, r = 0, len(numbers) - 1

while l < r:
    current_sum = numbers[l] + numbers[r]

    if current_sum == target:
        return [l + 1, r + 1]

    elif current_sum < target:
        l += 1

    else:
        r -= 1
```

**Alternative Solution: Hash Map**

```python
seen = {}

for i, num in enumerate(numbers):
    complement = target - num

    if complement in seen:
        return [seen[complement] + 1, i + 1]

    seen[num] = i
```

### Comparison

| Approach | Time | Space |
|-----------|------|--------|
| Two Pointers | O(n) | O(1) |
| Hash Map | O(n) | O(n) |
| Brute Force | O(n²) | O(1) |

**Why Two Pointers?**
- Array is already sorted.
- Eliminates extra space.
- Most optimal solution.

### Visualization

```text
numbers = [2, 7, 11, 15]
target = 9

l = 0 -> 2
r = 3 -> 15

2 + 15 = 17 > 9
Move r left

2 + 11 = 13 > 9
Move r left

2 + 7 = 9
Answer = [1, 2]
```

**Time:** O(n)

**Space:** O(1)

**Key Learning:**
Whenever the array is sorted and you need a pair satisfying a condition, think Two Pointers before Hash Map.

---
