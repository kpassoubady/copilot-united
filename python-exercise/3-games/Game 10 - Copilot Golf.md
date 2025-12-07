# Copilot Golf ⛳ (Efficiency)

## The Challenge

Implement an LRU (Least Recently Used) Cache with a prompt.

## The Goal

Use the fewest manual keystrokes to get a working implementation.

## The Setup

Students need to implement a fixed-size cache that removes the least recently accessed item when full.

## Python-Specific Approaches

### Option 1: Use Built-in Decorator

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_function(n: int) -> int:
    # Cached automatically!
    return n * n
```

### Option 2: Custom Implementation with OrderedDict

Ask Copilot to generate:

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get(self, key: str) -> int | None:
        # Move to end on access (most recently used)
        ...
    
    def put(self, key: str, value: int) -> None:
        # Evict oldest if at capacity
        ...
```

## Scoring

- **Par (3 strokes)**: Using `@lru_cache` decorator
- **Birdie (2 strokes)**: One-line prompt that generates complete custom class
- **Eagle (1 stroke)**: Perfect implementation with just a function signature comment

## Bonus Round

Try to generate a **thread-safe** LRU cache with minimal prompting!
