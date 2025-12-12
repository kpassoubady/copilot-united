# Test Architect 🧪 (Test Generation Mastery)

## The Challenge

Become a testing expert using Copilot's test generation capabilities.

## Round 1: Basic Test Generation

**Setup**: Given this service:

```python
import re

class EmailValidator:
    EMAIL_PATTERN = re.compile(r"^[A-Za-z0-9+_.-]+@(.+)$")
    
    def is_valid(self, email: str | None) -> bool:
        if not email or not email.strip():
            return False
        return bool(self.EMAIL_PATTERN.match(email))
    
    def get_domain(self, email: str) -> str:
        if not self.is_valid(email):
            raise ValueError("Invalid email")
        return email.split("@")[1]
```

**Task**: Use `/tests` and refine with follow-up prompts

```text
/tests Generate pytest tests with edge cases
```

```text
Add parametrized tests for multiple valid and invalid email formats
```

**Scoring**:
- ✅ 2 points: Tests happy path
- ✅ 2 points: Tests None/empty inputs
- ✅ 2 points: Tests boundary cases
- ✅ 2 points: Uses `@pytest.mark.parametrize`

---

## Round 2: Mock Master

**Setup**: A service with dependencies:

```python
class OrderService:
    def __init__(self, repository, email_service):
        self.repository = repository
        self.email_service = email_service
    
    def create_order(self, request: OrderRequest) -> Order:
        order = Order.from_request(request)
        saved = self.repository.save(order)
        self.email_service.send_confirmation(saved)
        return saved
```

**Task**: Generate tests with unittest.mock or pytest-mock

```text
Generate pytest tests for OrderService using unittest.mock to mock repository and email_service dependencies
```

**Scoring**:
- ✅ 2 points: Properly mocks dependencies
- ✅ 2 points: Verifies mock interactions with `assert_called_*`
- ✅ 2 points: Tests exception scenarios

---

## Round 3: Test-Driven Development (TDD)

**Challenge**: Write tests FIRST, then ask Copilot to implement

**Step 1**: Write test specification
```text
Generate pytest tests for a ShoppingCart class that should:
- Add items with quantity
- Remove items
- Calculate total price
- Apply percentage discount
- Raise ValueError for negative quantities
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

**Task**: Generate integration tests for a FastAPI router

```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/api/users")

@router.get("/{user_id}")
async def get_user(user_id: int) -> User:
    ...

@router.post("/")
async def create_user(request: UserRequest) -> User:
    ...

@router.delete("/{user_id}")
async def delete_user(user_id: int) -> None:
    ...
```

```text
Generate FastAPI TestClient integration tests for this router including:
- Success scenarios
- Not found scenarios (404)
- Validation failure scenarios (422)
- Content type verification
```

**Expected test structure**:
```python
from fastapi.testclient import TestClient

def test_get_user_success(client: TestClient):
    response = client.get("/api/users/1")
    assert response.status_code == 200
    assert "id" in response.json()

def test_get_user_not_found(client: TestClient):
    response = client.get("/api/users/99999")
    assert response.status_code == 404
```

---

## Bonus: Coverage Detective

**Task**: Identify untested code paths

```text
Analyze #file:services/order_service.py and identify which code paths are NOT covered by #file:tests/test_order_service.py
```

**Then**: Generate tests for missing coverage

---

## Learning Outcomes

- Generate comprehensive unit tests with pytest
- Use mocking effectively with `unittest.mock`
- Practice TDD workflow with AI
- Create integration tests with TestClient
- Identify and fill coverage gaps
