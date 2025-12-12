# Doc or Die 📝 (Documentation Generation)

## The Challenge

Transform undocumented "legacy" code into beautifully documented, maintainable code using Copilot.

## The Setup

You inherit this undocumented class:

```java
public class OrderProcessor {
    private List<Order> orders = new ArrayList<>();
    private Map<String, Double> discounts = new HashMap<>();
    
    public void addOrder(Order o) {
        if (o != null && o.getTotal() > 0) {
            orders.add(o);
        }
    }
    
    public double calc(String code) {
        double t = 0;
        for (Order o : orders) {
            t += o.getTotal();
        }
        if (discounts.containsKey(code)) {
            t *= (1 - discounts.get(code));
        }
        return t;
    }
    
    public void addD(String c, double d) {
        if (d > 0 && d < 1) {
            discounts.put(c, d);
        }
    }
}
```

---

## Round 1: Method Documentation Race

**Task**: Generate complete JavaDoc for each method

**Prompts to try**:
```text
Generate JavaDoc for this method including @param, @return, and @throws
```

```text
/doc Add comprehensive documentation explaining the business logic
```

**Scoring**:
- ✅ 2 points: Complete `@param` descriptions
- ✅ 2 points: Clear `@return` explanation
- ✅ 1 point: Documents any exceptions
- ✅ 1 point: Explains business rules

---

## Round 2: Variable Naming Makeover

**Task**: Ask Copilot to suggest better names

```text
Suggest better variable names for this method. The current names are: t, o, c, d
```

**Expected transformation**:
- `t` → `totalAmount`
- `o` → `order`
- `c` → `discountCode`
- `d` → `discountPercentage`

---

## Round 3: Class-Level Documentation

**Task**: Generate a class-level overview

```text
Write a class-level JavaDoc that explains:
- What this class does
- How to use it (with example)
- Thread-safety considerations
- Any limitations
```

---

## Round 4: README Generation

**Task**: Use the documented class to generate a README section

```text
Based on #file:OrderProcessor.java, generate a README.md section explaining the order processing system with usage examples
```

---

## Bonus: Inline Comments Challenge

**Task**: Add inline comments explaining complex logic

```java
// Before: No comments
public double calc(String code) {
    double t = 0;
    for (Order o : orders) {
        t += o.getTotal();
    }
    if (discounts.containsKey(code)) {
        t *= (1 - discounts.get(code));
    }
    return t;
}
```

**Goal**:
```java
// After: Clear inline comments
public double calculateTotal(String discountCode) {
    // Sum all order totals
    double total = 0;
    for (Order order : orders) {
        total += order.getTotal();
    }
    
    // Apply discount if valid code provided
    if (discounts.containsKey(discountCode)) {
        double discountRate = discounts.get(discountCode);
        total *= (1 - discountRate);  // Reduce total by discount percentage
    }
    
    return total;
}
```

---

## Learning Outcomes

- Generate professional JavaDoc documentation
- Improve code readability with better naming
- Create user-facing documentation from code
- Understand documentation best practices
