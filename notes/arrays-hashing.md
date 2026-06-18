# defaultdict(set)

```python
from collections import defaultdict

rows = defaultdict(set)
rows[0].add("5")
```

## Benefit

- Automatically creates an empty `set` for missing keys.
- Avoids manual initialization.

Instead of:

```python
if key not in rows:
    rows[key] = set()

rows[key].add(value)
```

Simply use:

```python
rows[key].add(value)
```
