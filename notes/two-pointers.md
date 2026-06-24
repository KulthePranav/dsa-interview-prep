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
