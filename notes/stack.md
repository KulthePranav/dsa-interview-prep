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

## 155. Min Stack

**Pattern:** Stack + Auxiliary Stack

**Signal:**
- Need normal stack operations.
- Need O(1) minimum retrieval.
- Cannot scan the stack every time.

### Why Not Brute Force?

For every `getMin()`:

```python
min(stack)
```

Time:

```text
O(n)
```

Too slow if `getMin()` is called frequently.


### Observation

While pushing an element, we already know the minimum so far.

Instead of recomputing it later, store it alongside the current stack state.


### Approach

Maintain two stacks:

- `stack` → stores all values.
- `min_stack` → stores the minimum value up to each position.

For every push:

```python
min_stack.append(min(current_value, previous_min))
```

Both stacks always have the same size.


### Visualization

Push:

```text
Push 5

Stack      Min Stack
-----      ---------
5          5
```

Push:

```text
Push 3

Stack      Min Stack
-----      ---------
5          5
3          3
```

Push:

```text
Push 7

Stack      Min Stack
-----      ---------
5          5
3          3
7          3
```

Current minimum:

```text
min_stack[-1] = 3
```

Pop:

```text
Stack      Min Stack
-----      ---------
5          5
3          3
```

Minimum is still available in O(1).


### Template

```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)

        if not self.min_stack:
            self.min_stack.append(value)
        else:
            self.min_stack.append(min(self.min_stack[-1], value))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
```

### Alternative Solution

Store `(value, current_min)` as a tuple.

```python
stack.append((value, min(value, current_min)))
```

Then:

```python
top()

stack[-1][0]

getMin()

stack[-1][1]
```

Only one stack is required.


### Comparison

| Approach | Time | Space |
|-----------|------|--------|
| Two Stacks | O(1) | O(n) |
| Stack of Tuples | O(1) | O(n) |
| Scan for Minimum | O(n) | O(1) |

### Pattern Recognition

```text
Need stack operations?

↓

Need minimum/maximum in O(1)?

↓

Maintain an auxiliary stack
```

**Time:**

- Push → O(1)
- Pop → O(1)
- Top → O(1)
- GetMin → O(1)

**Space:** O(n)

**Key Learning:**
Whenever a data structure needs extra information in constant time, consider maintaining an auxiliary data structure alongside it.

---
