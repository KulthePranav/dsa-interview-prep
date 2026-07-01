# Stack

## 20. Valid Parentheses

**Pattern:** Stack

**Signal:**
- Matching pairs of symbols.
- Nested structures.
- Last In, First Out (LIFO) behavior.

### Observation

Opening brackets are pushed onto the stack.

When a closing bracket appears:

- The stack must not be empty.
- The top of the stack must contain the corresponding opening bracket.

Otherwise, the string is invalid.

### Approach

1. Create a mapping from closing brackets to opening brackets.
2. Traverse the string.
3. If the current character is an opening bracket, push it onto the stack.
4. If it's a closing bracket:
   - Check if the stack is empty.
   - Verify the top matches the corresponding opening bracket.
   - Pop the matched bracket.
5. At the end, the stack should be empty.

### Template

```python
stack = []

mapping = {
    ')': '(',
    ']': '[',
    '}': '{'
}

for bracket in s:

    if bracket in mapping:

        if not stack or stack[-1] != mapping[bracket]:
            return False

        stack.pop()

    else:
        stack.append(bracket)

return len(stack) == 0
```

### Visualization

```text
Input

({[]})

Stack

(

({

({[

({

(

Empty

✓ Valid
```

### Alternative Solution 1 (Opening Bracket Check)

```python
stack = []

mapping = {
    ')': '(',
    ']': '[',
    '}': '{'
}

opening = {'(', '[', '{'}

for bracket in s:

    if bracket in opening:
        stack.append(bracket)

    else:
        if not stack or stack[-1] != mapping[bracket]:
            return False

        stack.pop()

return len(stack) == 0
```

### Alternative Solution 2 (Expected Closing Brackets)

Instead of storing opening brackets, push the **expected closing bracket**.

```python
stack = []

pairs = {
    '(': ')',
    '[': ']',
    '{': '}'
}

for ch in s:

    if ch in pairs:
        stack.append(pairs[ch])

    else:
        if not stack or stack.pop() != ch:
            return False

return len(stack) == 0
```

This avoids looking up the mapping during closing bracket checks.

### Comparison

| Approach | Time | Space |
|-----------|------|--------|
| Stack + Closing-to-Opening Map | O(n) | O(n) |
| Stack + Opening Set | O(n) | O(n) |
| Stack + Expected Closing Brackets | O(n) | O(n) |


### Pattern Recognition

```text
Need to match symbols?

↓

Nested structure?

↓

Last opened closes first?

↓

Use a Stack
```

**Time:** O(n)

**Space:** O(n)

**Key Learning:**
Stacks are the ideal data structure whenever the most recently seen element must be processed first (LIFO).

---
