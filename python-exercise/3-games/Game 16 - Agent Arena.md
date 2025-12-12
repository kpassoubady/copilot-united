# Agent Arena 🤖 (Custom Agents & Instructions)

## The Challenge

Learn to create and use custom Copilot agents (chatmodes) for specialized assistance.

## Round 1: Create Your First Agent

**Task**: Create a FastAPI expert agent

Create file: `.github/agents/fastapi-expert.agent.md`

```markdown
---
description: 'FastAPI development specialist'
tools: []
---

You are a FastAPI expert assistant. When helping with code:

## Your Expertise
- FastAPI 0.100+ with Python 3.11+
- SQLAlchemy 2.0 with async support
- Pydantic v2 for validation
- pytest and pytest-asyncio for testing
- OAuth2/JWT authentication

## Code Style
- Use dependency injection with `Depends()`
- Prefer Pydantic models over dicts
- Use `Optional` or `| None` for nullable types
- Follow REST API best practices
- Include proper exception handling with HTTPException

## When Generating Code
- Always include necessary imports
- Add type hints everywhere
- Include docstrings for public functions
- Suggest relevant tests
- Use async/await for database operations
```

**Test it**:
```text
@workspace /agents fastapi-expert

Create a REST endpoint for user registration with Pydantic validation
```

---

## Round 2: Domain-Specific Agent Battle

**Challenge**: Create agents for different roles and compare outputs

### Agent 1: Security Expert
```markdown
---
description: 'Security-focused code reviewer'
---

You are a security expert. Always check for:
- SQL injection vulnerabilities
- XSS attack vectors
- Authentication/authorization issues
- Sensitive data exposure (passwords, API keys)
- OWASP Top 10 compliance
```

### Agent 2: Performance Expert
```markdown
---
description: 'Performance optimization specialist'
---

You are a performance expert. Always consider:
- Algorithm complexity (Big O)
- Memory usage and generators vs lists
- Database query optimization (N+1, indexes)
- Caching opportunities (functools.lru_cache, Redis)
- Async vs sync operations
```

**The Battle**: Both teams analyze the same code:

```python
def search_users(query: str) -> list[User]:
    all_users = user_repository.find_all()
    return [u for u in all_users if query in u.name]
```

**Scoring**: Which agent finds more issues?

---

## Round 3: Project Instructions

**Task**: Create project-wide Copilot instructions

Create file: `.github/copilot-instructions.md`

```markdown
# Project Coding Standards

## Architecture
This project follows clean architecture:
- `domain/` - Business logic, no framework dependencies
- `application/` - Use cases and services
- `infrastructure/` - Adapters (DB, REST, messaging)

## Naming Conventions
- Services: `*_service.py` (e.g., `order_service.py`)
- Repositories: `*_repository.py` (e.g., `user_repository.py`)
- Routers: `*_router.py` (e.g., `product_router.py`)
- Schemas: `*_schema.py` with `*Request`, `*Response` classes

## Testing
- Unit tests in `tests/unit/`
- Integration tests in `tests/integration/`
- Use `pytest-asyncio` for async tests
- Use `TestClient` for API tests

## Database
- Use Alembic migrations in `alembic/versions/`
- Migration naming: `{revision}_{description}.py`
- Always use async session for database operations
```

**Test**: Generate code and verify it follows project conventions

---

## Round 4: Agent Switching Challenge

**Scenario**: Build a feature using multiple agents

1. **Use `security-expert`**: Design authentication flow
2. **Use `fastapi-expert`**: Implement the endpoints
3. **Use `performance-expert`**: Review and optimize

**Task**: Implement a rate-limited API endpoint

```text
@workspace /agents security-expert
Design a rate limiting strategy for our API
```

```text
@workspace /agents fastapi-expert  
Implement rate limiting using slowapi library
```

```text
@workspace /agents performance-expert
Review this rate limiting implementation for performance issues
```

---

## Bonus: Agent Creation Contest

**Challenge**: Create the most useful custom agent for your team

**Judging Criteria**:
- ✅ Solves a real team problem
- ✅ Instructions are clear and specific
- ✅ Produces consistently good output
- ✅ Other team members find it valuable

**Example Ideas**:
- **Data Science Agent**: pandas, numpy, sklearn expertise
- **DevOps Agent**: Docker, CI/CD, AWS/GCP
- **Django Agent**: Django-specific patterns and ORM

---

## Learning Outcomes

- Create custom agents for specialized tasks
- Write effective agent instructions
- Use project-wide Copilot configuration
- Switch between agents for different perspectives
- Understand how context shapes AI responses
