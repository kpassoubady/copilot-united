# Hallucination Hunter 🐛 (Critical Review)

## The Challenge: The Mutable Default Argument Trap

Here is the code:

```python
def add_item(item, items=[]):
    """Copilot suggests this 'convenient' default to avoid None checks."""
    items.append(item)
    return items


# Usage
print(add_item("apple"))   # Expected: ['apple']
print(add_item("banana"))  # Expected: ['banana'] — but what actually happens?
```

## The Goal

Students must use Copilot Chat to ask, "Does this code have a bug?" or write a unit test to expose the bug.

## What's Wrong?

The mutable default argument (`items=[]`) is shared across all calls! This is one of Python's most common gotchas.

## Bonus Challenge

Ask Copilot to find the bug in this code:

```python
class UserCache:
    # Copilot suggests this 'optimization' to cache user data
    _cache = {}
    
    @classmethod
    def get_user(cls, user_id: int) -> dict:
        if user_id not in cls._cache:
            cls._cache[user_id] = fetch_user_from_db(user_id)
        return cls._cache[user_id]
```

**Question**: What happens in a multi-threaded environment? Is this thread-safe?
