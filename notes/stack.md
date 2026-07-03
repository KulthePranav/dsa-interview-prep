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

## 150. Evaluate Reverse Polish Notation

**Pattern:** Stack

**Signal:**
- Expression is given in postfix notation.
- Operators come after operands.
- Need to evaluate expressions while preserving order.


### What is Reverse Polish Notation (RPN)?

In RPN (Postfix notation):

Instead of:

```text
2 + 3
```

We write:

```text
2 3 +
```

Another example:

```text
(2 + 1) × 3
```

becomes

```text
2 1 + 3 *
```

No parentheses are required.


### Observation

Whenever an operator appears:

- The previous two numbers belong to it.
- The second popped value is the right operand.
- The first popped value is the left operand.

### Approach

1. Traverse every token.
2. If the token is a number:
   - Push it onto the stack.
3. Otherwise:
   - Pop two operands.
   - Perform the operation.
   - Push the result back.
4. The final element is the answer.


### Template

```python
operation_dict = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: int(a / b)
}

stack = []

for token in tokens:

    if token.lstrip("-").isdigit():
        stack.append(int(token))

    else:
        b = stack.pop()
        a = stack.pop()

        stack.append(operation_dict[token](a, b))

return stack[0]
```

### Visualization

Example:

```text
Tokens

["2","1","+","3","*"]
```

Stack:

```text
2

2 1

+

3

3

*

9
```

Answer:

```text
9
```

### Why `int(a / b)`?

Python's `//` performs **floor division**.

Example:

```python
-3 // 2
```

Result:

```text
-2
```

But the problem requires **truncate toward zero**:

```python
int(-3 / 2)
```

Result:

```text
-1
```

### Alternative Solution

Use `if-elif` instead of a dictionary.

```python
if token == "+":
    stack.append(a + b)

elif token == "-":
    stack.append(a - b)

elif token == "*":
    stack.append(a * b)

else:
    stack.append(int(a / b))
```

### Comparison

| Approach | Time | Space |
|-----------|------|--------|
| Stack + Lambda Dictionary | O(n) | O(n) |
| Stack + if-elif | O(n) | O(n) |


### Pattern Recognition

```text
Need to evaluate expression?

↓

Postfix notation?

↓

Use Stack
```

**Time:** O(n)

**Space:** O(n)

**Key Learning:**
Stacks naturally evaluate postfix expressions because operators always apply to the most recently seen operands.

---

## 739. Daily Temperatures

**Pattern:** Monotonic Stack (Next Greater Element)

**Signal:**
- Need the next greater value.
- Need the first future occurrence satisfying a condition.
- Linear-time solution required.

### Why Not Brute Force?

For every day:

```python
for j in range(i + 1, n):
```

Search for the next warmer temperature.

Time:

```text
O(n²)
```

### Observation

Some temperatures are still waiting for a warmer day.

Example:

```text
73 74 75
```

When 74 arrives:

```
73 is resolved.
```

When 75 arrives:

```
74 is resolved.
```

A stack naturally stores unresolved temperatures.

### Monotonic Stack

Maintain indices whose temperatures are in **decreasing order**.

Example:

```text
Temperatures

75
74
71
69

Stack (indices)

0
1
2
3
```

Whenever a warmer temperature appears:

```text
72
```

Resolve:

```text
69
71
```

### Why Store Indices?

We need to compute:

```python
days = current_index - previous_index
```

Storing only temperatures would lose the original positions.

### Approach

1. Traverse temperatures.
2. While the current temperature is warmer than the top of the stack:
   - Pop the previous index.
   - Calculate the number of waiting days.
3. Push the current index.
4. Any remaining indices never find a warmer day.


### Template

```python
stack = []
answer = [0] * len(temperatures)

for i, temp in enumerate(temperatures):

    while stack and temp > temperatures[stack[-1]]:

        index = stack.pop()

        answer[index] = i - index

    stack.append(i)

return answer
```

### Visualization

```text
Temperatures

73 74 75 71 69 72

Stack

73

74

75

75 71

75 71 69

72 arrives

Resolve:

69 → 1 day

71 → 2 days

Stack

75 72
```

### Alternative Solution

Brute Force

```python
for i:

    for j in range(i + 1, n):

        if temperatures[j] > temperatures[i]:
            answer[i] = j - i
            break
```

### Comparison

| Approach | Time | Space |
|-----------|------|--------|
| Monotonic Stack | O(n) | O(n) |
| Brute Force | O(n²) | O(1) |


### Pattern Recognition

```text
Need next greater element?

↓

Need first future greater value?

↓

Use Monotonic Stack
```

**Time:** O(n)

**Space:** O(n)

**Key Learning:**
A Monotonic Stack efficiently solves "Next Greater Element" problems by keeping unresolved indices in monotonic order.

---

## 853. Car Fleet

**Pattern:** Monotonic Stack (Arrival Time)

**Signal:**
- Cars move in one direction.
- Overtaking is not allowed.
- Faster cars may catch slower cars.
- Need to determine the number of fleets.

### Why Sort?

Fleet formation depends on the cars ahead.

Process cars from **closest to the target** to **farthest**.

```python
sorted(pair, reverse=True)
```

### Observation

Arrival time of a car:

```python
time = (target - position) / speed
```

If a car behind reaches the destination **earlier** than the fleet ahead:

```text
Behind arrives first

↓

It catches up

↓

Same fleet
```

Otherwise:

```text
Behind arrives later

↓

Cannot catch

↓

New fleet
```

### Approach

1. Pair each position with its speed.
2. Sort cars by position in descending order.
3. Compute each car's arrival time.
4. Push arrival time onto the stack.
5. If the current arrival time is less than or equal to the fleet ahead, merge fleets by removing the current time.
6. The stack size equals the number of fleets.

### Template

```python
pair = [[p, s] for p, s in zip(position, speed)]

stack = []

for p, s in sorted(pair, reverse=True):

    stack.append((target - p) / s)

    if len(stack) >= 2 and stack[-1] <= stack[-2]:
        stack.pop()

return len(stack)
```

### Visualization

Example:

```text
Target = 12

Position

10 8 5 3 0

Speed

2 4 1 3 1
```

Arrival times:

```text
1
1
7
3
12
```

Stack:

```text
1

1  → merge

7

7 3 → merge

7 12
```

Fleets:

```text
2
```

### Why Does `<=` Mean Merge?

Suppose:

```text
Fleet ahead arrives in 5 hours.

Current car arrives in 4 hours.
```

The current car reaches the fleet before the destination.

Since passing isn't allowed:

```text
4 <= 5

↓

Merge
```

The fleet arrival time remains:

```text
5
```

### Alternative Solution (Without Explicit Stack)

Since only the latest fleet time matters, a variable is sufficient.

```python
fleets = 0
last_time = 0

for p, s in sorted(zip(position, speed), reverse=True):

    current = (target - p) / s

    if current > last_time:
        fleets += 1
        last_time = current

return fleets
```

### Comparison

| Approach | Time | Space |
|-----------|------|--------|
| Monotonic Stack | O(n log n) | O(n) |
| Last Arrival Time Variable | O(n log n) | O(1) |

Sorting dominates the complexity.

### Pattern Recognition

```text
Cars moving toward one destination?

↓

No overtaking?

↓

Need to merge based on arrival time?

↓

Sort + Monotonic Stack
```

**Time:** O(n log n)

- Sorting → O(n log n)
- Stack traversal → O(n)

**Space:** O(n)

**Key Learning:**
Many "merge while moving" problems can be solved by sorting first and then maintaining a monotonic property (arrival time, distance, etc.)

---
