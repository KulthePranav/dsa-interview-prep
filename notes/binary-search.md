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

## 74. Search a 2D Matrix

**Pattern:** Binary Search (Two Binary Searches)

**Signal:**
- Each row is sorted.
- Rows are globally ordered.
- Need efficient searching.

### Key Idea

Treat the problem as two Binary Searches.

1. Find the row that may contain the target.
2. Perform Binary Search within that row.

### Why Two Binary Searches?

Since:

```
Last element of row i

<

First element of row i+1
```

Each row represents a distinct search range.

Example

```
1   3   5   7

10 11 16 20

23 30 34 60
```

Target = 16

```
Find row

↓

10 <= 16 <= 20

↓

Binary Search inside row
```

### Visualization

```
Rows

0

1

2

↓

Binary Search

↓

Row = 1

↓

10 11 16 20

↓

Binary Search

↓

Found
```

### Approach

1. Binary Search the rows.
2. Check whether the target lies within the current row.
3. Binary Search that row.
4. Return True if found.

### Template

```python
l, r = 0, len(matrix) - 1

while l <= r:

    m = (l + r) // 2

    if matrix[m][0] <= target <= matrix[m][-1]:

        left, right = 0, len(matrix[m]) - 1

        while left <= right:

            middle = (left + right) // 2

            if matrix[m][middle] == target:
                return True

            elif target < matrix[m][middle]:
                right = middle - 1

            else:
                left = middle + 1

        return False

    elif target < matrix[m][0]:
        r = m - 1

    else:
        l = m + 1

return False
```

---

### Alternative Solution (Treat Matrix as 1D)

Since the matrix is globally sorted, imagine it as:

```
1 3 5 7 10 11 16 20 23 30 34 60
```

Binary Search over indices.

Convert index back to row and column.

```python
rows = len(matrix)
cols = len(matrix[0])

left, right = 0, rows * cols - 1

while left <= right:

    mid = (left + right) // 2

    row = mid // cols
    col = mid % cols

    value = matrix[row][col]

    if value == target:
        return True

    elif target < value:
        right = mid - 1

    else:
        left = mid + 1

return False
```

### Comparison

| Approach | Time | Space |
|-----------|------|--------|
| Two Binary Searches | O(log m + log n) | O(1) |
| Treat as 1D | O(log(m × n)) | O(1) |

Since:

```
log(m × n)

=

log m + log n
```

Both have the same asymptotic complexity.

### Pattern Recognition

```text
Rows are sorted?

↓

Rows don't overlap?

↓

Binary Search rows

↓

Binary Search columns
```

or

```text
Entire matrix behaves like one sorted array?

↓

Treat as 1D

↓

Binary Search
```

**Time:** O(log m + log n)

**Space:** O(1)

**Key Learning:**
When rows are globally ordered, either perform two Binary Searches or treat the matrix as a flattened sorted array.

---

## 875. Koko Eating Bananas

**Pattern:** Binary Search on Answer

**Signal:**
- Need the minimum or maximum valid value.
- A candidate answer can be verified.
- Feasibility changes monotonically.

### Key Idea

We're **not searching the array**.

Instead, we're searching the possible eating speeds.

```
Speed

1 2 3 4 5 ... maxPile
```

Each speed answers the question:

> Can Koko finish within `h` hours?

This is a monotonic property:

```
Speed ↑

Hours Needed ↓
```

Once a speed works, every larger speed also works.

### Why Binary Search Works

Example

```
Hours allowed = 8

Speed

1 ❌
2 ❌
3 ❌
4 ✅
5 ✅
6 ✅
...
```

The answer space looks like

```
False False False True True True
```

Binary Search works whenever the search space is monotonic.

### Visualization

```
Search Space

1 ---------------- maxPile

        mid

Compute total hours

↓

hours <= h ?

↓

YES

Try smaller speed

↓

NO

Need faster speed
```

### Approach

1. Lowest possible speed = 1.
2. Highest possible speed = max(piles).
3. Binary Search the speed.
4. Compute hours required at that speed.
5. If Koko can finish:
   - save answer
   - search left half
6. Otherwise:
   - search right half.

### Template

```python
left, right = 1, max(piles)
res = right

while left <= right:

    middle = (left + right) // 2
    hours = 0

    for pile in piles:
        hours += math.ceil(pile / middle)

    if hours <= h:
        res = middle
        right = middle - 1

    else:
        left = middle + 1

return res
```

### Alternative Solution

Instead of

```python
math.ceil(pile / speed)
```

use integer arithmetic:

```python
hours += (pile + speed - 1) // speed
```

This avoids floating-point operations and is generally preferred in interviews.

Example

```
10 bananas

Speed = 3

(10 + 3 - 1) // 3

12 // 3

4
```

Equivalent to

```
ceil(10 / 3)
```

### Comparison

| Approach | Time | Space |
|-----------|------|--------|
| `math.ceil()` | O(n log m) | O(1) |
| Integer Ceiling Division | O(n log m) | O(1) |

Where:

- `n` = number of piles
- `m` = maximum pile size


### Pattern Recognition

```text
Need minimum valid answer?

↓

Can check if an answer works?

↓

True/False becomes monotonic?

↓

Binary Search on Answer
```

### Common Mistakes

❌ Binary searching the piles.

You're searching the **speed**, not the array.


❌ Updating answer incorrectly.

```python
res = min(res, mid)
```

Since `mid` is always moving left after a valid answer, this can simply be:

```python
res = mid
```

❌ Forgetting ceiling division.

```python
pile // speed
```

is incorrect.

Need

```python
ceil(pile / speed)
```

or

```python
(pile + speed - 1) // speed
```

**Time:** O(n log m)

**Space:** O(1)

**Key Learning:**
Binary Search on Answer is applicable whenever candidate answers can be validated and the feasibility changes monotonically.

---

## 153. Find Minimum in Rotated Sorted Array

**Pattern:** Modified Binary Search

**Signal:**
- Rotated sorted array.
- Need minimum element.
- O(log n) solution expected.

### Key Idea

In a rotated sorted array:

- At least one half is always sorted.
- The minimum lies in the unsorted half.
- If the current search space is already sorted, the leftmost element is the minimum.

### Visualization

Example:

```
4 5 6 7 0 1 2

l           r
      m
```

Left half:

```
4 5 6 7
```

is sorted.

Minimum must be in the right half.

Another example:

```
0 1 2 4 5

l       r
```

Entire search space is sorted.

Minimum = `nums[l]`.


### Approach

1. Initialize `res` with the first element.
2. While `left <= right`:
   - If the current range is sorted, update `res` with `nums[left]` and stop.
   - Find the middle.
   - Update the minimum.
   - If the left half is sorted, search the right half.
   - Otherwise, search the left half.

### Template

```python
res = nums[0]
l, r = 0, len(nums) - 1

while l <= r:

    if nums[l] < nums[r]:
        res = min(res, nums[l])
        break

    m = (l + r) // 2
    res = min(res, nums[m])

    if nums[m] >= nums[l]:
        l = m + 1
    else:
        r = m - 1

return res
```

### Why `nums[m] >= nums[l]`?

If

```python
nums[m] >= nums[l]
```

then

```
l -------- m
```

is sorted.

Since `nums[l]` has already been considered, the minimum cannot be inside this sorted half.

Search the right half.

Otherwise,

```
m -------- r
```

is sorted, meaning the rotation point (minimum) lies in the left half.


### Alternative Solution

Instead of maintaining `res`, compare the middle element with the right element:

```python
left, right = 0, len(nums) - 1

while left < right:

    mid = (left + right) // 2

    if nums[mid] > nums[right]:
        left = mid + 1
    else:
        right = mid

return nums[left]
```

This is the most common interview solution because it directly converges on the minimum without an extra variable.

### Comparison

| Approach | Time | Space |
|-----------|------|--------|
| Track `res` (Your Solution) | O(log n) | O(1) |
| Compare with Right Pointer | O(log n) | O(1) |


### Pattern Recognition

```text
Sorted array?

↓

Rotated?

↓

Need minimum?

↓

One half is sorted

↓

Discard the sorted half
```

### Common Mistakes

❌ Forgetting to check if the current range is already sorted.

```python
if nums[left] < nums[right]:
```

Without this, you'll do unnecessary iterations.

❌ Comparing with the wrong boundary.

Use:

```python
nums[mid] >= nums[left]
```

or

```python
nums[mid] > nums[right]
```

depending on the chosen approach.

**Time:** O(log n)

**Space:** O(1)

**Key Learning:**
In a rotated sorted array, one half is always sorted. Identify the sorted half and discard it to locate the rotation point efficiently.

---

## 33. Search in Rotated Sorted Array

**Pattern:** Modified Binary Search

**Signal:**
- Rotated sorted array.
- Need O(log n) search.
- Array contains unique elements.

### Key Idea

Unlike a normal Binary Search, the array is rotated.

However:

- One half is always sorted.
- Determine which half is sorted.
- Check whether the target belongs to that half.
- Discard the other half.


### Visualization

Example

```
4 5 6 7 0 1 2
```

```
l           r
      m
```

Left half

```
4 5 6 7
```

is sorted.

Target = 1

Since

```
1 < 4
```

Target cannot be in the left half.

Search the right half.


Another example

```
6 7 1 2 3 4 5

      m
```

Right half

```
2 3 4 5
```

is sorted.

Target = 7

Target isn't inside the sorted right half.

Search the left half.

### Approach

1. Compute the middle index.
2. If the target is found, return it.
3. Determine which half is sorted.
4. Check if the target lies inside the sorted half.
5. Discard the other half.
6. Repeat until found.


### Template

```python
l, r = 0, len(nums) - 1

while l <= r:

    m = (l + r) // 2

    if nums[m] == target:
        return m

    if nums[l] <= nums[m]:

        if target < nums[l] or target > nums[m]:
            l = m + 1
        else:
            r = m - 1

    else:

        if target > nums[r] or target < nums[m]:
            r = m - 1
        else:
            l = m + 1

return -1
```

### Understanding the Conditions

#### Case 1: Left Half is Sorted

```python
nums[left] <= nums[mid]
```

Example

```
4 5 6 7 0 1 2

Left side

4 5 6 7
```

If

```
target < nums[left]

OR

target > nums[mid]
```

Target cannot be inside the sorted half.

Search right.

Otherwise,

search left.


#### Case 2: Right Half is Sorted

Example

```
6 7 1 2 3 4 5
```

If

```
target > nums[right]

OR

target < nums[mid]
```

Target cannot be inside the sorted right half.

Search left.

Otherwise,

search right.

### Alternative Solution

A slightly cleaner version checks whether the target lies **inside** the sorted half instead of checking whether it lies **outside**.

```python
if nums[left] <= nums[mid]:

    if nums[left] <= target < nums[mid]:
        right = mid - 1
    else:
        left = mid + 1

else:

    if nums[mid] < target <= nums[right]:
        left = mid + 1
    else:
        right = mid - 1
```

Many interviewers prefer this because the conditions are easier to read.

### Comparison

| Approach | Time | Space |
|-----------|------|--------|
| Your Solution | O(log n) | O(1) |
| Cleaner Condition Version | O(log n) | O(1) |


### Pattern Recognition

```text
Sorted array?

↓

Rotated?

↓

Need O(log n)?

↓

One half is always sorted

↓

Check whether target belongs to sorted half

↓

Discard the other half
```

### Common Mistakes

❌ Forgetting to identify the sorted half.


❌ Using

```python
nums[left] < nums[mid]
```

instead of

```python
nums[left] <= nums[mid]
```

The equality is important when only one element remains.

❌ Mixing up which side to discard.

Always ask:

> Is the target inside the sorted half?

If yes → search there.

Otherwise → search the other half.

**Time:** O(log n)

**Space:** O(1)

**Key Learning:**
In a rotated sorted array, one half is always sorted. Binary Search works by identifying the sorted half and determining whether the target belongs to it.

---

## 981. Time Based Key-Value Store

**Pattern:** Hash Map + Binary Search

**Signal:**
- Multiple values for the same key.
- Need to retrieve the latest value at or before a timestamp.
- Timestamps are inserted in increasing order.

### Key Idea

Store all values for a key in chronological order.

```
"foo"

↓

[
    ("bar", 1),
    ("bar2", 4),
    ("bar3", 8),
    ("bar4", 15)
]
```

Since timestamps are sorted, Binary Search can efficiently find the latest valid timestamp.

### Visualization

```
timestamp = 10

1    4    8    15

          ↑

Latest timestamp ≤ 10

↓

Return "bar3"
```

### Data Structure

```python
{
    key: [
        [value, timestamp],
        [value, timestamp],
        ...
    ]
}
```

Example

```python
{
    "foo": [
        ["bar", 1],
        ["bar2", 4],
        ["bar3", 8]
    ]
}
```

### Approach

#### set()

1. If the key doesn't exist, create an empty list.
2. Append the `(value, timestamp)` pair.
3. Since timestamps are strictly increasing, the list remains sorted.

#### get()

1. Retrieve the list for the key.
2. Binary Search for the largest timestamp ≤ target.
3. Return its value.


### Template

```python
class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key, value, timestamp):
        if key not in self.store:
            self.store[key] = []

        self.store[key].append([value, timestamp])

    def get(self, key, timestamp):

        res = ""
        values = self.store.get(key, [])

        left, right = 0, len(values) - 1

        while left <= right:

            mid = (left + right) // 2

            if values[mid][1] <= timestamp:
                res = values[mid][0]
                left = mid + 1

            else:
                right = mid - 1

        return res
```

### Why Search Right After Finding a Valid Timestamp?

Suppose

```
Target = 8

Stored

1
4
8
12
```

At timestamp `8`

```
8 <= 8

Valid

↓

Search right
```

Maybe another timestamp later is still ≤ target.

We always want the **latest** valid timestamp.

### Alternative Solution

Use Python's `bisect_right`.

```python
from bisect import bisect_right

values = self.store.get(key, [])

index = bisect_right(values, timestamp, key=lambda x: x[1]) - 1

return values[index][0] if index >= 0 else ""
```

> Note: While concise, interviewers often prefer implementing Binary Search manually unless they explicitly allow standard library helpers.

### Comparison

| Approach | set() | get() | Space |
|-----------|-------|--------|-------|
| Manual Binary Search | O(1) | O(log n) | O(n) |
| `bisect_right` | O(1) | O(log n) | O(n) |

### Pattern Recognition

```text
Need historical values?

↓

Multiple versions of same key?

↓

Need latest value before timestamp?

↓

Hash Map

+

Binary Search
```


### Common Mistakes

❌ Linear search in `get()`

```python
for value, time in values:
```

This gives **O(n)** lookup.


❌ Sorting after every insertion.

Timestamps are already guaranteed to be increasing.

Simply append.

❌ Returning immediately when

```
timestamp == values[mid][1]
```

Continue searching right because we want the **latest timestamp ≤ target**.

**Time Complexity**

```
set() : O(1)

get() : O(log n)
```

**Space Complexity**

```
O(total number of stored values)
```

**Key Learning:**
When data is stored in sorted order over time, Binary Search can efficiently retrieve the latest valid historical record.

---
