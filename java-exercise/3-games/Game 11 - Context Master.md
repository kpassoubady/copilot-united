# Context Master 🎯 (Context Selection)

## The Challenge

Learn to use Copilot's context selectors effectively: `#file`, `#selection`, `@workspace`

## Round 1: The File Reference Challenge

**Setup**: You have a `User.java` model and need to create a `UserDTO.java`

**Task**: Use `#file:User.java` in your prompt to generate a matching DTO

```text
Create a UserDTO class based on #file:User.java but exclude sensitive fields like password and include only id, name, email
```

**Scoring**:
- ✅ 3 points: DTO matches model structure
- ✅ 2 points: Sensitive fields excluded
- ✅ 1 point: Proper JavaDoc generated

---

## Round 2: The Selection Surgeon

**Setup**: Select a complex method in your code

**Task**: Use `#selection` to ask targeted questions

```text
Refactor #selection to use the Strategy pattern instead of switch statements
```

**Learning**: Students discover how precise context leads to better suggestions

---

## Round 3: The Workspace Detective

**Setup**: A multi-module project with services, repositories, and controllers

**Task**: Use `@workspace` to understand project structure

```text
@workspace Where is the UserService used? Show me all the places it's injected.
```

```text
@workspace What database tables exist in this project? List all @Entity classes.
```

**Scoring**:
- ✅ 3 points: Finds all usages across modules
- ✅ 2 points: Understands project architecture
- ✅ 1 point: Generates accurate dependency graph

---

## Round 4: Combined Context Challenge

**Task**: Use multiple context selectors together

```text
@workspace Based on the existing repository pattern in #file:UserRepository.java, create a new ProductRepository that follows the same conventions
```

---

## Learning Outcomes

- Understand when to use `#file` vs `#selection` vs `@workspace`
- Learn that better context = better suggestions
- Practice referencing code without copy-pasting
