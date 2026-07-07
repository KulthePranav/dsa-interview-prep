# Binary Search

## 704. Binary Search

**Pattern:** Binary Search

**Signal:**
- Array is sorted.
- Need to find an element efficiently.
- O(log n) solution expected.

### Key Idea

At each step:

1. Find the middle element.
2. If it matches the target, return its index.
3. If the target is smaller, search the left half.
4. Otherwise, search the right half.

Each comparison eliminates half of the remaining search space.

### Visualization

```
nums = [-1,0,3,5,9,12]
target = 9

l                 r
-1 0 3 5 9 12
      ↑
    mid = 5

9 > 3

Search right half

            l     r
-1 0 3 5 9 12
          ↑
         mid

Found
```

### Approach

1. Initialize two pointers:
   - `left = 0`
   - `right = len(nums) - 1`
2. While `left <= right`:
   - Compute the middle index.
   - Compare `nums[mid]` with the target.
   - Discard half of the search space.
3. If not found, return `-1`.

### Template

```python
left = 0
right = len(nums) - 1

while left <= right:

    middle = (left + right) // 2

    if target == nums[middle]:
        return middle

    elif target < nums[middle]:
        right = middle - 1

    else:
        left = middle + 1

return -1
```

### Alternative Solution (Recursive)

```python
def binarySearch(left, right):

    if left > right:
        return -1

    mid = (left + right) // 2

    if nums[mid] == target:
        return mid

    if target < nums[mid]:
        return binarySearch(left, mid - 1)

    return binarySearch(mid + 1, right)

return binarySearch(0, len(nums) - 1)
```

### Comparison

| Approach | Time | Space |
|-----------|------|--------|
| Iterative | O(log n) | O(1) |
| Recursive | O(log n) | O(log n) (call stack) |


### Pattern Recognition

```text
Is the array sorted?

↓

Need fast searching?

↓

Can eliminate half each step?

↓

Use Binary Search
```

### Common Mistakes

❌ Using:

```python
while left < right
```

when the target may be at the last remaining position.

✅ Correct:

```python
while left <= right
```


❌ Incorrect middle calculation (in languages with integer overflow):

```python
mid = (left + right) // 2
```

Preferred in Java/C++:

```python
mid = left + (right - left) // 2
```

Python integers don't overflow, so either is fine.


**Time:** O(log n)

**Space:** O(1)

**Key Learning:**
Binary Search works because each comparison removes half of the remaining search space, reducing the time complexity from O(n) to O(log n).

---
