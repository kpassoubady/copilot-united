# Agent Arena 🤖 (Custom Agents & Instructions)

## The Challenge

Learn to create and use custom Copilot agents (chatmodes) for specialized assistance.

## Round 1: Create Your First Agent

**Task**: Create a Spring Boot expert agent

Create file: `.github/agents/spring-expert.agent.md`

```markdown
---
description: 'Spring Boot development specialist'
tools: []
---

You are a Spring Boot expert assistant. When helping with code:

## Your Expertise
- Spring Boot 3.x and Spring Framework 6.x
- Spring Data JPA and Hibernate
- Spring Security with OAuth2/JWT
- Spring WebFlux for reactive programming
- Testing with JUnit 5 and MockMvc

## Code Style
- Use constructor injection (not @Autowired on fields)
- Prefer records for DTOs
- Use Optional for nullable returns
- Follow REST API best practices
- Include proper exception handling

## When Generating Code
- Always include necessary imports
- Add appropriate annotations
- Include JavaDoc for public methods
- Suggest relevant tests
```

**Test it**:
```text
@workspace /agents spring-expert

Create a REST endpoint for user registration with validation
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
- Sensitive data exposure
- OWASP Top 10 compliance
```

### Agent 2: Performance Expert
```markdown
---
description: 'Performance optimization specialist'
---

You are a performance expert. Always consider:
- Algorithm complexity (Big O)
- Memory usage
- Database query optimization
- Caching opportunities
- Lazy vs eager loading
```

**The Battle**: Both teams analyze the same code:

```java
public List<User> searchUsers(String query) {
    List<User> allUsers = userRepository.findAll();
    return allUsers.stream()
        .filter(u -> u.getName().contains(query))
        .collect(Collectors.toList());
}
```

**Scoring**: Which agent finds more issues?

---

## Round 3: Project Instructions

**Task**: Create project-wide Copilot instructions

Create file: `.github/copilot-instructions.md`

```markdown
# Project Coding Standards

## Architecture
This project follows hexagonal architecture:
- `domain/` - Business logic, no framework dependencies
- `application/` - Use cases and ports
- `infrastructure/` - Adapters (DB, REST, messaging)

## Naming Conventions
- Services: `*Service` (e.g., `OrderService`)
- Repositories: `*Repository` (e.g., `UserRepository`)
- Controllers: `*Controller` (e.g., `ProductController`)
- DTOs: `*Request`, `*Response` (e.g., `CreateUserRequest`)

## Testing
- Unit tests in `src/test/java`
- Integration tests in `src/integrationTest/java`
- Use `@DataJpaTest` for repository tests
- Use `@WebMvcTest` for controller tests

## Database
- Use Flyway migrations in `src/main/resources/db/migration`
- Migration naming: `V{version}__{description}.sql`
```

**Test**: Generate code and verify it follows project conventions

---

## Round 4: Agent Switching Challenge

**Scenario**: Build a feature using multiple agents

1. **Use `security-expert`**: Design authentication flow
2. **Use `spring-expert`**: Implement the endpoints
3. **Use `performance-expert`**: Review and optimize

**Task**: Implement a rate-limited API endpoint

```text
@workspace /agents security-expert
Design a rate limiting strategy for our API
```

```text
@workspace /agents spring-expert  
Implement rate limiting using the bucket4j library
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

---

## Learning Outcomes

- Create custom agents for specialized tasks
- Write effective agent instructions
- Use project-wide Copilot configuration
- Switch between agents for different perspectives
- Understand how context shapes AI responses
