# Context Master 🎯 (Context Selection)

## The Challenge

Learn to use Copilot's context selectors effectively: `#file`, `#selection`, `@workspace`

## Round 1: The File Reference Challenge

**Setup**: You have a `user.py` model and need to create a `user_dto.py`

**Task**: Use `#file:user.py` in your prompt to generate a matching DTO

```text
Create a UserDTO Pydantic model based on #file:models/user.py but exclude sensitive fields like password_hash and include only id, name, email
```

**Scoring**:
- ✅ 3 points: DTO matches model structure
- ✅ 2 points: Sensitive fields excluded
- ✅ 1 point: Proper docstrings generated

---

## Round 2: The Selection Surgeon

**Setup**: Select a complex function in your code

**Task**: Use `#selection` to ask targeted questions

```text
Refactor #selection to use the Strategy pattern instead of if/elif chains
```

**Learning**: Students discover how precise context leads to better suggestions

---

## Round 3: The Workspace Detective

**Setup**: A FastAPI project with services, repositories, and routes

**Task**: Use `@workspace` to understand project structure

```text
@workspace Where is the UserService used? Show me all the places it's imported.
```

```text
@workspace What database models exist in this project? List all SQLAlchemy model classes.
```

**Scoring**:
- ✅ 3 points: Finds all usages across modules
- ✅ 2 points: Understands project architecture
- ✅ 1 point: Generates accurate dependency graph

---

## Round 4: Combined Context Challenge

**Task**: Use multiple context selectors together

```text
@workspace Based on the existing repository pattern in #file:repositories/user_repository.py, create a new ProductRepository that follows the same conventions
```

---

## Example Code for Practice

**models/user.py**:
```python
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    password_hash: Mapped[str] = mapped_column(String(255))  # Sensitive!
    created_at: Mapped[datetime] = mapped_column(DateTime)
```

**Expected DTO output**:
```python
from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserDTO(BaseModel):
    id: int
    name: str
    email: EmailStr
    
    model_config = ConfigDict(from_attributes=True)
```

---

## Learning Outcomes

- Understand when to use `#file` vs `#selection` vs `@workspace`
- Learn that better context = better suggestions
- Practice referencing code without copy-pasting
