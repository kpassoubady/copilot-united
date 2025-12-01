# Guess the prompt - Palindrome Checker - Reverse Engineering

## Instructions

1. You will be given a Java function that solves a specific problem.
2. Your task is to write a prompt that could have been used to generate this function using an AI coding assistant.
3. The prompt should be clear, specific, and include all necessary details to guide the AI in generating the provided function.
4. Consider including:
   - The problem statement
   - Input and output examples
   - Any constraints or edge cases
   - Requirements for code quality (e.g., comments, readability)
   - Testing requirements
   - Performance considerations
5. Aim to make the prompt as comprehensive as possible to ensure the AI can produce the exact solution.

```java
public class PalindromeChecker {

    public static boolean isPalindrome(String input) {
        if (input == null) return false;
        String cleaned = input.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        String reversed = new StringBuilder(cleaned).reverse().toString();
        return cleaned.equals(reversed);
    }

    public static void main(String[] args) {
        System.out.println(isPalindrome("A man, a plan, a canal: Panama")); // true
        System.out.println(isPalindrome("Hello, world")); // false
    }
}
```
