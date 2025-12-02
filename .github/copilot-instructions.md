# GitHub Copilot Instructions for Training Repository

## Repository Overview

This is a comprehensive **1-day GitHub Copilot training** repository for building a **Personal Expense Tracker** application. The course offers two parallel tracks sharing the same Copilot curriculum:

- **Java Track**: Spring Boot with H2 database (project1/)
- **Python Track**: FastAPI with SQLite database (project2/)

### Directory Structure

- **day1/**: All course materials - interface mastery, shortcuts, context usage, chat features, agents, and advanced workflows
- **project1/**: Java Track - Spring Boot Task Manager reference application (Java 21, Maven, Thymeleaf)
- **project2/**: Python Track - FastAPI Task Manager reference application (Python 3.11+)
- **catalog/**: Course outline and curriculum documentation
- **docs/**: Project documentation with navigation links
- **exercise/**: Hands-on breakout session materials for Personal Expense Tracker

## Architecture Patterns

### Java Track (project1/task-manager/)
- **Standard Structure**: Maven-based Spring Boot 3.2.3 with Java 21
- **Package Convention**: `com.taskmanager.app` with standard MVC layers (controller, service, repository, entity, dto, exception, config)
- **Configuration**: H2 database for development, disabled Spring Security for training
- **Frontend**: Thymeleaf templates with Bootstrap 5.3.2 and jQuery 3.7.1 via WebJars
- **Build**: Standard Maven lifecycle, runs on port 8080, includes OpenAPI documentation

### Python Track (project2/task-manager/)
- **Framework**: FastAPI with SQLite for development
- **Package Convention**: Standard Python project structure
- **Frontend**: Jinja2 templates with Bootstrap for styling
- **Build**: Python virtual environment with pip/requirements.txt

## Development Workflows

### Running Spring Boot Application
```bash
cd project1/task-manager
mvn spring-boot:run
# Or: mvn clean install && java -jar target/task-manager-1.0.0.jar
# Alternative port: SERVER_PORT=8081 mvn spring-boot:run
```

### Running FastAPI Application (Python Track)
```bash
cd project2/task-manager
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### Development Environment Setup
- **Java Track**: Requires JDK 21, Maven, Git (detailed in `project1/install/`)
- **Python Track**: Requires Python 3.11+ (3.12 recommended), Git (detailed in `project2/install/`)
- **IDE Extensions**: GitHub Copilot, REST Client
  - Java: Java Extension Pack, Spring Boot Extension Pack
  - Python: Python Extension, Pylance
- **GitHub Copilot**: Must be enabled and authenticated before class

### Documentation Generation
- Use Copilot Chat with `#file` context for updating documentation
- Follow existing markdown structure in day1/ directory
- Include code examples from actual project files
- Maintain emoji headers (🎯, 💬, ✏️) in learning materials
- Reference course outline in `catalog/GitHub Copilot - 1 Day - Personal Expense Tracker.md`

## Project-Specific Conventions

### Naming Patterns
- **Spring Boot**: Use `@RestController` for APIs, `@Controller` for MVC
- **Testing**: Test classes end with `Test`, use descriptive method names
- **Documentation**: Use emoji headers (🎯, 💬, ✏️) in learning materials
- **Configuration**: Properties over YAML, environment-specific profiles

### Code Organization
- **Controllers**: Handle HTTP layer, delegate to services
- **Services**: Business logic, transaction boundaries
- **Repositories**: Data access layer with JPA conventions
- **Tests**: Follow AAA pattern (Arrange, Act, Assert)

### Security Considerations
- Security disabled in development for training purposes
- Default credentials: admin/password for demos
- Real implementations should enable Spring Security properly

## Context Integration Points

### Cross-Project Dependencies
- Both tracks share the same Copilot curriculum and learning objectives
- All course materials consolidated in day1/ directory
- Installation guides in project1/install/ (Java) and project2/install/ (Python)
- Breakout exercises in exercise/ directory reference both tracks

### External Dependencies (Java Track)
- **Spring Boot Starters**: Web, Data JPA, Thymeleaf, Validation
- **H2 Database**: Embedded database for rapid development
- **WebJars**: Frontend dependency management (Bootstrap 5.3.2, jQuery 3.7.1)
- **OpenAPI**: Automated API documentation (Swagger UI available at `/swagger-ui.html`)

### External Dependencies (Python Track)
- **FastAPI**: Modern async web framework
- **SQLAlchemy**: ORM for database operations
- **SQLite**: Embedded database for development
- **Jinja2**: Templating engine for web UI

## Training-Specific Guidance

When generating code for this repository:

1. **Maintain Educational Value**: Add comments explaining key concepts
2. **Use Current Versions**: Stick to specified dependency versions (Spring Boot 3.2.3 for Java, Python 3.11+ for Python)
3. **Follow Project Structure**: Respect existing package naming and directory layout
4. **Include Error Handling**: Demonstrate proper exception handling patterns
5. **Documentation First**: Update relevant documentation when adding features
6. **Track-Agnostic Copilot Skills**: Focus on Copilot workflows over framework-specific details

### Key Files for Context
- `project1/task-manager/pom.xml` - Java Track: Spring Boot dependencies and versions
- `project2/task-manager/requirements.txt` - Python Track: FastAPI dependencies
- `docs/README.md` - Project documentation and navigation hub
- `catalog/GitHub Copilot - 1 Day - Personal Expense Tracker.md` - Complete course curriculum
- `day1/README.md` - All learning materials and exercises
- `README.md` - Course structure and learning objectives
- `install.md` - Cross-platform setup instructions for both tracks

## Common Development Tasks

- **Adding REST Endpoints**: 
  - Java: Use `@RestController`, return `ResponseEntity`
  - Python: Use FastAPI decorators (`@app.get`, `@app.post`)
- **Documentation Updates**: Follow emoji patterns and markdown structure in day1/ folder
- **Configuration Changes**: Update `application.properties` (Java) or `.env` (Python)
- **Exercise Creation**: Add new exercises to exercise/ directory with proper numbering

## Cross-Platform Development Notes

- **Java Track**: Requires JDK 21, Maven; runs on port 8080
- **Python Track**: Requires Python 3.11+; runs on port 8000 (uvicorn default)
- **IDE Support**: Both VS Code and IntelliJ IDEA/PyCharm are supported
- **Testing**: Spring Boot Test for Java, pytest for Python

## 1-Day Course Schedule Reference

| Session | Duration | Topics |
|---------|----------|--------|
| Foundations | 30 min | Generative AI concepts, tools comparison |
| Setup & Interface | 45 min | Copilot installation, shortcuts, suggestions |
| Breakout 1 | 90 min | Backend modeling (entities, repositories, services) |
| Chat & Context | 45 min | Hash contexts (`#file`, `#selection`, `#codebase`) |
| Breakout 2 | 90 min | Web layer & REST APIs |
| Advanced Usage | 45 min | Custom instructions, plugins, agents |
| Troubleshooting | 15 min | Copilot logs, restore points |
| Wrap-up | 35 min | Documentation generation, workflow blueprint |
