# Doc or Die 📝 (Documentation Generation)

## The Challenge

Transform undocumented "legacy" code into beautifully documented, maintainable code using Copilot.

## The Setup

You inherit this undocumented class:

```python
class OrderProcessor:
    def __init__(self):
        self.orders = []
        self.discounts = {}
    
    def add_order(self, o):
        if o and o.total > 0:
            self.orders.append(o)
    
    def calc(self, code):
        t = 0
        for o in self.orders:
            t += o.total
        if code in self.discounts:
            t *= (1 - self.discounts[code])
        return t
    
    def add_d(self, c, d):
        if 0 < d < 1:
            self.discounts[c] = d
```

---

## Round 1: Method Documentation Race

**Task**: Generate complete docstrings for each method

**Prompts to try**:
```text
Generate Google-style docstrings for this method including Args, Returns, and Raises
```

```text
/doc Add comprehensive documentation explaining the business logic
```

**Scoring**:
- ✅ 2 points: Complete Args descriptions
- ✅ 2 points: Clear Returns explanation
- ✅ 1 point: Documents any exceptions
- ✅ 1 point: Explains business rules

---

## Round 2: Variable Naming Makeover

**Task**: Ask Copilot to suggest better names

```text
Suggest better variable names for this method. The current names are: t, o, c, d
```

**Expected transformation**:
- `t` → `total_amount`
- `o` → `order`
- `c` → `discount_code`
- `d` → `discount_percentage`

---

## Round 3: Class-Level Documentation

**Task**: Generate a class-level overview

```text
Write a class-level docstring that explains:
- What this class does
- How to use it (with example)
- Thread-safety considerations
- Any limitations
```

**Expected output**:
```python
class OrderProcessor:
    """
    Process and calculate totals for customer orders with discount support.
    
    This class manages a collection of orders and applies discount codes
    to calculate final totals.
    
    Example:
        >>> processor = OrderProcessor()
        >>> processor.add_order(Order(total=100.0))
        >>> processor.add_d("SAVE10", 0.10)
        >>> processor.calc("SAVE10")
        90.0
    
    Note:
        This class is not thread-safe. For concurrent access,
        use appropriate synchronization.
    """
```

---

## Round 4: README Generation

**Task**: Use the documented class to generate a README section

```text
Based on #file:order_processor.py, generate a README.md section explaining the order processing system with usage examples
```

---

## Bonus: Type Hints Challenge

**Task**: Add comprehensive type hints to the undocumented code

```python
# Before: No type hints
def calc(self, code):
    t = 0
    for o in self.orders:
        t += o.total
    ...
```

**Goal**:
```python
# After: Full type hints
from decimal import Decimal
from typing import Optional

def calculate_total(self, discount_code: Optional[str] = None) -> Decimal:
    """Calculate the total order amount with optional discount."""
    total: Decimal = Decimal("0")
    for order in self.orders:
        total += order.total
    ...
```

---

## Learning Outcomes

- Generate professional Python docstrings (Google/NumPy style)
- Improve code readability with better naming
- Add comprehensive type hints
- Create user-facing documentation from code
- Understand documentation best practices
