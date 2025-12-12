# Command Relay Race 🏃 (Slash Commands)

## The Challenge

Master Copilot's slash commands: `/explain`, `/fix`, `/tests`, `/doc`

## Race Format

Teams compete to complete tasks using ONLY slash commands. Manual coding = disqualification!

---

## Leg 1: The Explainer `/explain`

**Setup**: Given this cryptic legacy code:

```python
def m(a: list[int]) -> int:
    r = a[0]
    for i in range(1, len(a)):
        r ^= a[i]
    return r
```

**Task**: Use `/explain` to understand what this code does

**Scoring**: First team to correctly identify "finds the single non-duplicate number using XOR" wins

---

## Leg 2: The Fixer `/fix`

**Setup**: This code has bugs:

```python
def filter_names(names: list[str]) -> list[str]:
    return sorted(
        name.upper 
        for name in names 
        if len(name) > 3
    )
```

**Task**: Select the code and use `/fix` to identify and correct all issues

**Scoring**:
- ✅ 2 points: Fixes missing parentheses `name.upper()`
- ✅ 1 point: Adds None check
- ✅ 1 point: Explains the fix

---

## Leg 3: The Tester `/tests`

**Setup**: Given this service function:

```python
def calculate_discount(price: float, customer_type: str) -> float:
    """Calculate discount based on customer type."""
    if customer_type == "VIP":
        return price * 0.20
    if customer_type == "REGULAR":
        return price * 0.10
    return 0.0
```

**Task**: Use `/tests` to generate comprehensive pytest tests

**Scoring**:
- ✅ 2 points: Tests all customer types
- ✅ 2 points: Tests edge cases (None, empty, negative price)
- ✅ 1 point: Uses `@pytest.mark.parametrize`

---

## Leg 4: The Documenter `/doc`

**Setup**: An undocumented utility module

```python
def reverse(text: str) -> str:
    ...

def is_palindrome(text: str) -> bool:
    ...

def truncate(text: str, max_length: int) -> str:
    ...
```

**Task**: Use `/doc` to generate complete docstrings for all functions

**Scoring**:
- ✅ 1 point per function documented
- ✅ 1 point for Args section
- ✅ 1 point for Returns section
- ✅ 1 point for Raises where applicable

---

## Bonus Round: Command Chain

**Challenge**: Fix, test, and document a function using only slash commands in sequence!

```python
# Start with buggy, untested, undocumented code
def fib(n: int) -> int:
    if n <= 1:
        return 1  # Bug: should be n for fib(0)=0, fib(1)=1
    return fib(n - 1) + fib(n - 2)
```

1. `/fix` - Correct the base case
2. `/tests` - Generate tests
3. `/doc` - Add documentation

**Winner**: First team to have working, tested, documented code!

---

## Learning Outcomes

- Know which command to use for each situation
- Understand command capabilities and limitations
- Practice efficient AI-assisted workflows
