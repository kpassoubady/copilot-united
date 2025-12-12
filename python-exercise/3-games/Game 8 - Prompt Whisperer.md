# The "Prompt Whisperer" Mystery 🕵️ (Prompt Engineering)

The Challenge: Reverse-engineer a complex Python data transformation.

## The Setup

Here is the code:

```python
from collections import Counter

result = Counter(
    t.currency for t in transactions if t.amount > 1000
)
```

## The Goal

Students must write a natural language prompt that gets Copilot to output this exact data transformation on the first try.

## Hints for Students

- Think about what the code does step-by-step
- Be specific about filtering conditions
- Mention the desired output type (`Counter` or `dict`)