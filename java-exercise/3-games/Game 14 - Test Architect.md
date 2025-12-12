# Test Architect 🧪 (Test Generation Mastery)

## The Challenge

Become a testing expert using Copilot's test generation capabilities.

## Round 1: Basic Test Generation

**Setup**: Given this service:

```java
public class EmailValidator {
    private static final Pattern EMAIL_PATTERN = 
        Pattern.compile("^[A-Za-z0-9+_.-]+@(.+)$");
    
    public boolean isValid(String email) {
        if (email == null || email.isBlank()) {
            return false;
        }
        return EMAIL_PATTERN.matcher(email).matches();
    }
    
    public String getDomain(String email) {
        if (!isValid(email)) {
            throw new IllegalArgumentException("Invalid email");
        }
        return email.substring(email.indexOf('@') + 1);
    }
}
```

**Task**: Use `/tests` and refine with follow-up prompts

```text
/tests Generate JUnit 5 tests with edge cases
```

```text
Add parameterized tests for multiple valid and invalid email formats
```

**Scoring**:
- ✅ 2 points: Tests happy path
- ✅ 2 points: Tests null/empty inputs
- ✅ 2 points: Tests boundary cases
- ✅ 2 points: Uses `@ParameterizedTest`

---

## Round 2: Mock Master

**Setup**: A service with dependencies:

```java
public class OrderService {
    private final OrderRepository repository;
    private final EmailService emailService;
    
    public Order createOrder(OrderRequest request) {
        Order order = new Order(request);
        Order saved = repository.save(order);
        emailService.sendConfirmation(saved);
        return saved;
    }
}
```

**Task**: Generate tests with Mockito mocks

```text
Generate JUnit tests for OrderService using Mockito to mock OrderRepository and EmailService
```

**Scoring**:
- ✅ 2 points: Properly mocks dependencies
- ✅ 2 points: Verifies mock interactions
- ✅ 2 points: Tests exception scenarios

---

## Round 3: Test-Driven Development (TDD)

**Challenge**: Write tests FIRST, then ask Copilot to implement

**Step 1**: Write test specification
```text
Generate JUnit tests for a ShoppingCart class that should:
- Add items with quantity
- Remove items
- Calculate total price
- Apply percentage discount
- Throw exception for negative quantities
```

**Step 2**: Ask Copilot to implement the class
```text
Based on these tests, implement the ShoppingCart class that makes all tests pass
```

**Scoring**:
- ✅ 3 points: All tests pass
- ✅ 2 points: Implementation follows test contracts
- ✅ 1 point: No test modifications needed

---

## Round 4: Integration Test Challenge

**Task**: Generate integration tests for a REST controller

```java
@RestController
@RequestMapping("/api/users")
public class UserController {
    @GetMapping("/{id}")
    public ResponseEntity<User> getUser(@PathVariable Long id) { ... }
    
    @PostMapping
    public ResponseEntity<User> createUser(@RequestBody @Valid UserRequest request) { ... }
    
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteUser(@PathVariable Long id) { ... }
}
```

```text
Generate Spring MockMvc integration tests for this controller including:
- Success scenarios
- Not found scenarios (404)
- Validation failure scenarios (400)
- Content type verification
```

---

## Bonus: Coverage Detective

**Task**: Identify untested code paths

```text
Analyze #file:OrderService.java and identify which code paths are NOT covered by #file:OrderServiceTest.java
```

**Then**: Generate tests for missing coverage

---

## Learning Outcomes

- Generate comprehensive unit tests
- Use mocking frameworks effectively
- Practice TDD workflow with AI
- Create integration tests
- Identify and fill coverage gaps
