# Guess the prompt - Palindrome Checker - Reverse Engineering

## Instructions

1. You will be given a Python function that solves a specific problem.
2. Your task is to write a prompt that could have been used to generate this function using an AI coding assistant.
3. The prompt should be clear, specific, and include all necessary details to guide the AI in generating the provided function.
4. Consider including:
   - The problem statement
   - Input and output examples
   - Any constraints or edge cases
   - Requirements for code quality (e.g., comments, readability, type hints)
   - Testing requirements
   - Performance considerations
5. Aim to make the prompt as comprehensive as possible to ensure the AI can produce the exact solution.

```python
import re


def is_palindrome(input_string: str | None) -> bool:
    """Check if a string is a palindrome, ignoring non-alphanumeric characters."""
    if input_string is None:
        return False
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', input_string).lower()
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal: Panama"))  # True
    print(is_palindrome("Hello, world"))  # False
```
