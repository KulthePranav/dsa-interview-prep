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

## 15. 3Sum

**Pattern:** Sorting + Two Pointers

**Signal:**
- Need triplets that satisfy a condition.
- Array can be sorted first.
- Need unique triplets.

**Approach:**
1. Sort the array.
2. Fix one element.
3. Use two pointers on the remaining array.
4. Skip duplicates for both the fixed element and pointer values.
5. Add valid triplets to the result.

**Template:**

```python
nums.sort()

for i, n in enumerate(nums):

    if i > 0 and nums[i - 1] == n:
        continue

    l, r = i + 1, len(nums) - 1

    while l < r:
        three_sum = n + nums[l] + nums[r]

        if three_sum == 0:
            res.append([n, nums[l], nums[r]])

            l += 1

            while l < r and nums[l] == nums[l - 1]:
                l += 1

        elif three_sum < 0:
            l += 1

        else:
            r -= 1
```

### Duplicate Handling

#### Fixed Element

```python
if i > 0 and nums[i - 1] == nums[i]:
    continue
```

Avoids:

```text
[-1, 0, 1]
[-1, 0, 1]
```

being added twice.

#### Left Pointer

```python
while l < r and nums[l] == nums[l - 1]:
    l += 1
```

Skips duplicate second elements.

### Alternative Solution

Brute Force:

```python
for i:
    for j:
        for k:
```

Time: O(n³)

### Comparison

| Approach | Time | Space |
|-----------|------|--------|
| Sorting + Two Pointers | O(n²) | O(1)* |
| Brute Force | O(n³) | O(1) |

\* Ignoring output array.

### Visualization

```text
nums = [-4,-1,-1,0,1,2]

Fix -1

l = -1
r = 2

-1 + -1 + 2 = 0

Triplet Found:
[-1,-1,2]
```

**Time:** O(n²)

**Space:** O(1) extra space

**Key Learning:**
Many 3-element problems can be reduced to a series of Two Sum problems after sorting.

---

## 11. Container With Most Water

**Pattern:** Greedy + Two Pointers

**Signal:**
- Need maximum area from two boundaries.
- Brute force would check all pairs.
- Looking for O(n) solution.

**Approach:**
1. Place one pointer at the beginning and one at the end.
2. Calculate the current area.
3. Update the maximum area.
4. Move the pointer with the smaller height.
5. Continue until pointers meet.

**Formula:**

```python
area = width * height

area = (r - l) * min(height[l], height[r])
```

**Template:**

```python
max_area = 0

l, r = 0, len(height) - 1

while l < r:
    area = (r - l) * min(height[l], height[r])

    max_area = max(max_area, area)

    if height[l] < height[r]:
        l += 1
    else:
        r -= 1

return max_area
```

### Why Move the Smaller Height?

Current area:

```text
Area = Width × Min(left_height, right_height)
```

The smaller height limits the area.

Example:

```text
[1,8,6,2,5,4,8,3,7]

l = 1
r = 7

Area = width × min(1,7)

The height 1 is limiting us.
Moving height 7 cannot increase area.
```

Therefore:

```python
if height[l] < height[r]:
    l += 1
else:
    r -= 1
```

### Alternative Solution

Brute Force:

```python
for i in range(n):
    for j in range(i + 1, n):
        area = (j - i) * min(height[i], height[j])
```

### Comparison

| Approach | Time | Space |
|-----------|------|--------|
| Two Pointers | O(n) | O(1) |
| Brute Force | O(n²) | O(1) |

### Visualization

```text
height = [1,8,6,2,5,4,8,3,7]

l = 0
r = 8

Area = 8 × min(1,7)
Area = 8

Move l

l = 1
r = 8

Area = 7 × min(8,7)
Area = 49

Maximum = 49
```

**Time:** O(n)

**Space:** O(1)

**Key Learning:**
The limiting factor is always the smaller height. Move that pointer to potentially find a taller boundary.

---

## 42. Trapping Rain Water

**Pattern:** Two Pointers

**Signal:**
- Need information from both left and right sides.
- Water trapped depends on surrounding boundaries.
- Want O(n) time and O(1) extra space.

**Approach:**
1. Maintain two pointers:
   - Left pointer
   - Right pointer
2. Track:
   - left_max
   - right_max
3. The smaller boundary determines trapped water.
4. Move the pointer with the smaller maximum.
5. Add trapped water at each position.

**Formula:**

```python
water = min(left_max, right_max) - height[i]
```

### Brute Force Idea

For every position:

```python
left_max = max(height[:i])
right_max = max(height[i+1:])
```

Then:

```python
water = min(left_max, right_max) - height[i]
```

Time:

```text
O(n²)
```

### Better Approach (Prefix Max Arrays)

```python
max_left = [0] * n
max_right = [0] * n
```

Store maximum heights from both directions.

```python
max_left[i]
max_right[i]
```

Then:

```python
water = min(max_left[i], max_right[i]) - height[i]
```

Time:

```text
O(n)
```

Space:

```text
O(n)
```

### Optimal Two Pointer Approach

Observation:

```text
Water depends on the smaller boundary.
```

If:

```python
left_max < right_max
```

Then:

```python
water = left_max - height[l]
```

because right side is guaranteed to be taller.

Similarly:

```python
right_max < left_max
```

Then:

```python
water = right_max - height[r]
```

### Template

```python
l, r = 0, len(height) - 1

left_max = height[l]
right_max = height[r]

water = 0

while l < r:

    if left_max < right_max:

        l += 1

        left_max = max(left_max, height[l])

        water += left_max - height[l]

    else:

        r -= 1

        right_max = max(right_max, height[r])

        water += right_max - height[r]

return water
```

### Visualization

```text
height = [4,2,0,3,2,5]

left_max = 4
right_max = 5

Move Left

Water at 2:
4 - 2 = 2

Water at 0:
4 - 0 = 4

Water at 3:
4 - 3 = 1

Water at 2:
4 - 2 = 2

Total = 9
```

### Comparison

| Approach | Time | Space |
|-----------|------|--------|
| Two Pointers | O(n) | O(1) |
| Prefix Arrays | O(n) | O(n) |
| Brute Force | O(n²) | O(1) |


### Pattern Recognition

```text
Need left and right information?

Think:

Prefix / Postfix

Can it be optimized?

Think:

Two Pointers
```

**Time:** O(n)

**Space:** O(1)

**Key Learning:**
The smaller boundary always determines the trapped water.
This allows us to process the array using two pointers instead of extra arrays.

---

## 344. Reverse String

**Pattern:** Two Pointers (In-place Swapping)

**Signal:**
- Reverse an array or string.
- In-place modification is required.
- Minimize extra space.

### Key Idea

Use two pointers:

- Left starts from the beginning.
- Right starts from the end.

Swap both elements and move the pointers toward the center.


### Visualization

```
Input

["h", "e", "l", "l", "o"]

 l               r
 h   e   l   l   o

Swap

 o   e   l   l   h
     l       r

Swap

 o   l   l   e   h

Done
```

### Approach

1. Initialize two pointers.
2. Swap the characters at both pointers.
3. Move the left pointer forward.
4. Move the right pointer backward.
5. Continue until both pointers meet.

### Template

```python
l, r = 0, len(s) - 1

while l < r:
    s[l], s[r] = s[r], s[l]
    l += 1
    r -= 1
```

### Alternative Solution (Python Built-in)

```python
s.reverse()
```

Or

```python
s[:] = s[::-1]
```

> **Note:** While these are concise, interviewers generally expect the two-pointer solution to demonstrate understanding of in-place algorithms.


### Comparison

| Approach | Time | Space |
|-----------|------|--------|
| Two Pointers | O(n) | O(1) |
| `reverse()` | O(n) | O(1) |
| Slicing (`[::-1]`) | O(n) | O(n) |

### Pattern Recognition

```text
Need to reverse in-place?

↓

Two ends involved?

↓

Use Two Pointers

↓

Swap until pointers meet
```

**Time:** O(n)

**Space:** O(1)

**Key Learning:**
When an array or string needs to be reversed in-place, use two pointers moving toward the center while swapping elements.

---

## 680. Valid Palindrome II

**Pattern:** Two Pointers + Greedy

**Signal:**
- Check whether a string is a palindrome.
- One deletion is allowed.
- Need an O(n) solution.

## Approach

1. Initialize two pointers:
   - `l` at the beginning.
   - `r` at the end.
2. Move both pointers inward while characters match.
3. On the first mismatch:
   - Skip the left character and check if the remaining substring is a palindrome.
   - Skip the right character and check if the remaining substring is a palindrome.
4. If either check succeeds, return `True`.
5. Otherwise, return `False`.

## Visualization

Input

```
"abca"
```

```
a == a

↓

b != c

↓

Skip left

aca

✓

OR

Skip right

aba

✓
```

Answer

```
True
```

## Template

```python
def is_palindrome(l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

l, r = 0, len(s) - 1

while l < r:
    if s[l] != s[r]:
        return (
            is_palindrome(l + 1, r) or
            is_palindrome(l, r - 1)
        )

    l += 1
    r -= 1

return True
```

## Actual Solution

```python
class Solution:
    def validPalindrome(self, s: str) -> bool:

        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return (
                    is_palindrome(l + 1, r) or
                    is_palindrome(l, r - 1)
                )

            l += 1
            r -= 1

        return True
```

## Alternative Solution (Recursive)

```python
class Solution:
    def validPalindrome(self, s: str) -> bool:

        def dfs(l, r, deleted):
            while l < r:
                if s[l] != s[r]:
                    if deleted:
                        return False

                    return (
                        dfs(l + 1, r, True) or
                        dfs(l, r - 1, True)
                    )

                l += 1
                r -= 1

            return True

        return dfs(0, len(s) - 1, False)
```

The recursive solution is elegant but uses recursion stack space.

## Comparison

| Approach | Time | Space |
|----------|------|-------|
| Two Pointers + Helper | O(n) | O(1) |
| Recursive | O(n) | O(n) |

## Pattern Recognition

```text
Palindrome?

↓

One deletion allowed?

↓

First mismatch?

↓

Skip left OR Skip right

↓

Check remaining substring
```

## Common Mistakes

❌ Trying every possible deletion.

```
O(n²)
```

❌ Continuing after the first mismatch.

Only one deletion is allowed.

❌ Forgetting to check both possibilities.

```python
skip left

OR

skip right
```

**Time Complexity:** O(n)

**Space Complexity:** O(1)

**Key Learning:**
Only the first mismatch matters. After it occurs, there are exactly two possibilities: remove the left character or remove the right character.

---
