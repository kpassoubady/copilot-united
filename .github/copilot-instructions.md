# GitHub Copilot Instructions for NFCU Training Repository

## Repository Overview

This is a comprehensive 3-day GitHub Copilot training repository containing:

- **day1/**: Foundation materials - interface mastery, shortcuts, basic commands, setup guides
- **day2/**: Advanced context materials - hash variables, chat features, multi-file workflows  
- **day3/**: Professional workflows - agents, enterprise practices, testing excellence
- **project1/**: Spring Boot Task Manager full-stack application (Java 21, Maven, Thymeleaf)
- **project2/**: Selenium UI automation testing framework (TestNG, WebDriverManager)
- **catalog/**: Course outlines and curriculum documentation with detailed 3-day timeline
- **docs/**: Project documentation with navigation links and course overview
- **exercise/**: Hands-on exercises and breakout session materials

## Architecture Patterns

### Spring Boot Project (project1/task-manager/)
- **Standard Structure**: Maven-based Spring Boot 3.2.3 with Java 21
- **Package Convention**: `com.taskmanager.app` with standard MVC layers (controller, service, repository, entity, dto, exception, config)
- **Configuration**: H2 database for development, disabled Spring Security for training
- **Frontend**: Thymeleaf templates with Bootstrap 5.3.2 and jQuery 3.7.1 via WebJars
- **Build**: Standard Maven lifecycle, runs on port 8080, includes OpenAPI documentation

### Selenium Testing Project (project2/ui-tests/)
- **Framework**: TestNG with Selenium WebDriver 4.27.0, Java 17
- **Package Convention**: `com.kavinschool.app` for test organization
- **Driver Management**: WebDriverManager 5.7.0 for automatic browser driver setup
- **Test Structure**: Page Object Model pattern encouraged, TestNG XML configuration
- **Logging**: SLF4J with Logback for test execution logging

## Development Workflows

### Running Spring Boot Application
```bash
cd project1/task-manager
mvn spring-boot:run
# Or: mvn clean install && java -jar target/task-manager-1.0.0.jar
# Alternative port: SERVER_PORT=8081 mvn spring-boot:run
```

### Running Selenium Tests
```bash
cd project2/ui-tests
mvn test
# Or specific test: mvn test -Dtest=GoogleTest
# Clean and recompile: mvn clean compile
```

### Development Environment Setup
- **Project 1**: Requires JDK 21, Maven, Git (detailed in `project1/install/`)
- **Project 2**: Requires JDK 17, Maven, Git (detailed in `project2/install/`)
- **IDE Extensions**: Java Extension Pack, Spring Boot Extension Pack, GitHub Copilot, REST Client
- **Browser Setup**: Chrome/Firefox for Selenium testing (WebDriverManager handles drivers automatically)

### Documentation Generation
- Use Copilot Chat with `#file` context for updating documentation
- Follow existing markdown structure distributed across day1/, day2/, day3/ directories
- Include code examples from actual project files
- Maintain emoji headers (🎯, 💬, ✏️) in learning materials
- Reference comprehensive course outline in catalog/ for timeline and structure

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
- Both projects use Maven with similar structure
- Shared documentation patterns across day1/, day2/, day3/ directories
- Common Java conventions across both codebases
- Installation guides distributed in project1/install/ and project2/install/
- Daily materials cross-reference exercises in exercise/ directory

### External Dependencies
- **WebDriverManager**: Automatic browser driver management (Chrome, Firefox, Edge)
- **TestNG**: Test framework with XML configuration support
- **Spring Boot Starters**: Web, Security, Data JPA, Thymeleaf, Validation
- **H2 Database**: Embedded database for rapid development
- **WebJars**: Frontend dependency management (Bootstrap 5.3.2, jQuery 3.7.1)
- **OpenAPI**: Automated API documentation (Swagger UI available at `/swagger-ui.html`)

## Training-Specific Guidance

When generating code for this repository:

1. **Maintain Educational Value**: Add comments explaining key concepts
2. **Use Current Versions**: Stick to specified dependency versions (Spring Boot 3.2.3, Selenium 4.27.0)
3. **Follow Project Structure**: Respect existing package naming and directory layout
4. **Include Error Handling**: Demonstrate proper exception handling patterns
5. **Documentation First**: Update relevant documentation when adding features

### Key Files for Context
- `project1/task-manager/pom.xml` - Spring Boot dependencies and versions
- `project2/ui-tests/pom.xml` - Selenium testing configuration  
- `docs/README.md` - Project documentation and navigation hub
- `catalog/GitHub Copilot - 3-Day Course Outline (Personal Expense Tracker).md` - Complete course curriculum
- `day1/README.md`, `day2/README.md`, `day3/README.md` - Daily learning materials and exercises
- `README.md` - Course structure and learning objectives
- `Install.md` - Cross-platform setup instructions

## Common Development Tasks

- **Adding REST Endpoints**: Use `@RestController`, return ResponseEntity
- **Creating Test Cases**: Extend existing test patterns, use WebDriverManager
- **Documentation Updates**: Follow emoji patterns and markdown structure across day folders
- **Configuration Changes**: Update application.properties, respect training environment
- **Daily Material Updates**: Maintain consistency across day1/, day2/, day3/ structure
- **Exercise Creation**: Add new exercises to exercise/ directory with proper numbering

## Cross-Platform Development Notes

- **Java Version Differences**: Project1 uses JDK 21, Project2 uses JDK 17 (both supported)
- **Build Commands**: Use standard Maven commands across both projects
- **IDE Support**: Both VS Code and IntelliJ IDEA are supported with proper extension packs
- **Testing**: TestNG for UI tests, Spring Boot Test for unit/integration tests
