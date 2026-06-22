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
