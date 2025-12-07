# Command Relay Race 🏃 (Slash Commands)

## The Challenge

Master Copilot's slash commands: `/explain`, `/fix`, `/tests`, `/doc`

## Race Format

Teams compete to complete tasks using ONLY slash commands. Manual coding = disqualification!

---

## Leg 1: The Explainer `/explain`

**Setup**: Given this cryptic legacy code:

```java
public int m(int[] a) {
    int r = a[0];
    for (int i = 1; i < a.length; i++) {
        r ^= a[i];
    }
    return r;
}
```

**Task**: Use `/explain` to understand what this code does

**Scoring**: First team to correctly identify "finds the single non-duplicate number using XOR" wins

---

## Leg 2: The Fixer `/fix`

**Setup**: This code has bugs:

```java
public List<String> filterNames(List<String> names) {
    return names.stream()
        .filter(n -> n.length() > 3)
        .map(n -> n.toUpperCase)
        .sorted()
        .toList();
}
```

**Task**: Select the code and use `/fix` to identify and correct all issues

**Scoring**:
- ✅ 2 points: Fixes missing parentheses `toUpperCase()`
- ✅ 1 point: Adds null check
- ✅ 1 point: Explains the fix

---

## Leg 3: The Tester `/tests`

**Setup**: Given this service method:

```java
public class DiscountCalculator {
    public double calculateDiscount(double price, String customerType) {
        if ("VIP".equals(customerType)) return price * 0.20;
        if ("REGULAR".equals(customerType)) return price * 0.10;
        return 0;
    }
}
```

**Task**: Use `/tests` to generate comprehensive JUnit tests

**Scoring**:
- ✅ 2 points: Tests all customer types
- ✅ 2 points: Tests edge cases (null, empty, negative price)
- ✅ 1 point: Uses parameterized tests

---

## Leg 4: The Documenter `/doc`

**Setup**: An undocumented utility class

```java
public class StringUtils {
    public static String reverse(String input) { ... }
    public static boolean isPalindrome(String input) { ... }
    public static String truncate(String input, int maxLength) { ... }
}
```

**Task**: Use `/doc` to generate complete JavaDoc for all methods

**Scoring**:
- ✅ 1 point per method documented
- ✅ 1 point for `@param` tags
- ✅ 1 point for `@return` tags
- ✅ 1 point for `@throws` where applicable

---

## Bonus Round: Command Chain

**Challenge**: Fix, test, and document a method using only slash commands in sequence!

```java
// Start with buggy, untested, undocumented code
public int fib(int n) {
    if (n <= 1) return 1;  // Bug: should be n for fib(0)=0, fib(1)=1
    return fib(n-1) + fib(n-2);
}
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
