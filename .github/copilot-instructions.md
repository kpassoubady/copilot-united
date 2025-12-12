# GitHub Copilot Instructions for Training Repository

## Repository Overview

This is a comprehensive **1-day GitHub Copilot training** repository for building a **Personal Expense Tracker** application. The course offers **four parallel tracks** sharing the same Copilot curriculum:

- **Java Track**: Spring Boot 3.2.3 with H2/PostgreSQL database (java-exercise/)
- **Python Track**: FastAPI with SQLite database (python-exercise/)
- **.NET Track**: ASP.NET Core 10.0 with SQLite/SQL Server database (dotnet-exercise/)
- **Python Data Analysis Track**: Pandas with Matplotlib/Seaborn for data analysis (python-data-analysis-exercise/)

### Directory Structure

- **day1/**: Session 1-2 course materials - AI foundations, Copilot setup, interface mastery, shortcuts, basic context usage
- **day2/**: Session 3-4 course materials - Chat features, agents, workspace context, custom instructions, advanced workflows
- **java-exercise/**: Java Track - Complete Spring Boot Personal Expense Tracker bootcamp (4 sessions × 45 min)
- **python-exercise/**: Python Track - Complete FastAPI Personal Expense Tracker bootcamp (4 sessions × 45 min)
- **dotnet-exercise/**: .NET Track - Complete ASP.NET Core Personal Expense Tracker bootcamp (4 sessions × 45 min)
- **catalog/**: Course outline and curriculum documentation
- **project1/**: Java Track - Spring Boot Task Manager scaffold
- **project2/**: Python Track - FastAPI Task Manager scaffold
- **project3/**: .NET Track - ASP.NET Core Task Manager scaffold
- **project4/**: Python Data Analysis Track - Data Analysis Pipeline scaffold
- **python-data-analysis-exercise/**: Python Data Analysis Track - Pandas/visualization bootcamp
- **.github/agents/**: AI agent definitions (Performance Optimization Agent)

## Architecture Patterns

### Java Track (java-exercise/)
- **Standard Structure**: Maven-based Spring Boot 3.2.3 with Java 21
- **Package Convention**: `com.expensetracker` with standard MVC layers (controller, service, repository, entity, dto, exception, config)
- **Configuration**: H2 database for development, PostgreSQL for production
- **Frontend**: Thymeleaf templates with Bootstrap 5.3.2 and jQuery 3.7.1 via WebJars
- **Build**: Standard Maven lifecycle, runs on port 8080, includes OpenAPI documentation
- **Testing**: JUnit 5, Mockito, Spring Boot Test with AAA pattern
- **Session Structure**: 4 sessions × 45 min (Entities/Repos → Services → REST APIs → Thymeleaf UI)

### Python Track (python-exercise/)
- **Framework**: FastAPI with SQLite for development
- **Package Convention**: Standard Python project structure with SQLAlchemy models, Pydantic schemas, service layer
- **Configuration**: SQLite database, Alembic migrations, environment-based settings
- **Frontend**: Jinja2 templates with Bootstrap 5.3.2 for styling
- **Build**: Python virtual environment with pip/requirements.txt, runs on port 8000
- **Testing**: pytest, pytest-asyncio with AAA pattern
- **Session Structure**: 4 sessions × 45 min (Models/DB → Services → REST APIs → Jinja2 UI)

### .NET Track (dotnet-exercise/)
- **Framework**: ASP.NET Core 10.0 with Entity Framework Core 9.0
- **Project Convention**: Standard .NET solution structure with separate projects (Web, Core, Infrastructure, Tests)
- **Configuration**: SQLite for development, SQL Server for production
- **Frontend**: Razor Pages with Bootstrap 5.3.2 and Chart.js
- **Build**: .NET CLI or Visual Studio, runs on port 5000/5001, includes Swagger/OpenAPI
- **Testing**: xUnit, Moq, FluentAssertions with AAA pattern
- **Validation**: FluentValidation 11.3 for business rules
- **Session Structure**: 4 sessions × 45 min (Models/DbContext → Services → REST APIs → Razor Pages)

### Python Data Analysis Track (python-data-analysis-exercise/)
- **Framework**: Pandas 2.0+ with Matplotlib and Seaborn for visualization
- **Project Convention**: Jupyter notebooks and Python scripts organized by analysis type
- **Configuration**: Virtual environment with requirements.txt
- **Tools**: Jupyter Notebook/Lab, VS Code with Python extension
- **Build**: Python virtual environment with pip, Jupyter server
- **Testing**: pytest for utility functions, notebook validation
- **Libraries**: NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn
- **Session Structure**: 3 sessions (Setup/Intro → Breakout Exercises → Interactive Games)

## Development Workflows

### Running Spring Boot Application (Java Track)
```bash
cd java-exercise
# Create new project directory for your expense tracker
mkdir personal-expense-tracker
cd personal-expense-tracker

# Initialize Spring Boot project (or use Spring Initializr)
mvn spring-boot:run
# Alternative port: SERVER_PORT=8081 mvn spring-boot:run
```

### Running FastAPI Application (Python Track)
```bash
cd python-exercise
# Create new project directory
mkdir personal-expense-tracker
cd personal-expense-tracker

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### Running ASP.NET Core Application (.NET Track)
```bash
cd dotnet-exercise
# Create new project
dotnet new webapp -n PersonalExpenseTracker
cd PersonalExpenseTracker

# Run the application
dotnet run
# Or with hot reload
dotnet watch run
# Alternative port: dotnet run --urls="https://localhost:5002;http://localhost:5003"
```

### Running Data Analysis Pipeline (Python Data Analysis Track)
```bash
cd project4/data-pipeline

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Run Jupyter Notebook
jupyter notebook notebooks/

# Or run a script
python src/intro_pandas.py
```

### Development Environment Setup
- **Java Track**: Requires JDK 21, Maven, Git (detailed in `java-exercise/1-setup/`)
- **Python Track**: Requires Python 3.11+ (3.12 recommended), Git (detailed in `python-exercise/1-setup/`)
- **.NET Track**: Requires .NET 9+ SDK, Git (detailed in `dotnet-exercise/1-setup/`)
- **Python Data Analysis Track**: Requires Python 3.9+, Jupyter, Git (detailed in `project4/install/`)
- **IDE Extensions**: GitHub Copilot (must be authenticated before class)
  - Java: Java Extension Pack, Spring Boot Extension Pack, REST Client
  - Python: Python Extension, Pylance, Jupyter, REST Client
  - .NET: C# Dev Kit, C# Extensions, REST Client
  - Data Analysis: Python Extension, Jupyter, Data Wrangler
- **GitHub Copilot**: Must be enabled and authenticated before class

### Documentation Generation
- Use Copilot Chat with `#file` context for updating documentation
- Follow existing markdown structure in day1/ and day2/ directories
- Include code examples from actual project files
- Maintain emoji headers (🎯, 💬, ✏️) in learning materials
- Reference course outline in `catalog/GitHub Copilot - 1 Day - Personal Expense Tracker.md`
- Each track follows identical session structure for consistent learning experience

## Project-Specific Conventions

### Naming Patterns
- **Spring Boot**: Use `@RestController` for APIs, `@Controller` for MVC
- **FastAPI**: Use router decorators (`@router.get`, `@router.post`)
- **.NET**: Use Minimal APIs or Controllers, Razor Pages for MVC
- **Testing**: Test classes end with `Test`, use descriptive method names
- **Documentation**: Use emoji headers (🎯, 💬, ✏️) in learning materials
- **Configuration**: Properties over YAML (Java), .env files (Python), appsettings.json (.NET)

### Code Organization
- **Controllers/Routes**: Handle HTTP layer, delegate to services
- **Services**: Business logic, transaction boundaries
- **Repositories/Data Access**: Data layer with ORM conventions (JPA/SQLAlchemy/EF Core)
- **Tests**: Follow AAA pattern (Arrange, Act, Assert) across all tracks
- **Session Structure**: 4 progressive sessions × 45 minutes each
  - Session 1: Data models and database layer
  - Session 2: Business logic and testing
  - Session 3: REST API endpoints
  - Session 4: Web UI with templates

### Security Considerations
- Security disabled in development for training purposes
- Default credentials: admin/password for demos
- Real implementations should enable Spring Security properly

## Context Integration Points

### Cross-Project Dependencies
- All four tracks share the same Copilot curriculum and learning objectives
- Course materials split into day1/ (basics) and day2/ (advanced)
- Each track has identical session structure for consistent learning experience
- Shared learning goals: Copilot mastery over framework-specific knowledge

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

### External Dependencies (.NET Track)
- **ASP.NET Core**: Web framework with Razor Pages
- **Entity Framework Core**: ORM for database operations
- **SQLite**: Embedded database for development (SQL Server for production)
- **FluentValidation**: Fluent API for validation rules
- **Chart.js**: Interactive charts via CDN

### External Dependencies (Python Data Analysis Track)
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Matplotlib**: Static visualizations
- **Seaborn**: Statistical data visualization
- **Scikit-learn**: Machine learning utilities
- **Jupyter**: Interactive notebook environment

## Training-Specific Guidance

When generating code for this repository:

1. **Maintain Educational Value**: Add comments explaining key concepts
2. **Use Current Versions**: Stick to specified dependency versions (Spring Boot 3.2.3 for Java, Python 3.11+ for Python, .NET 9+ for .NET, Pandas 2.0+ for Data Analysis)
3. **Follow Project Structure**: Respect existing package naming and directory layout
4. **Include Error Handling**: Demonstrate proper exception handling patterns
5. **Documentation First**: Update relevant documentation when adding features
6. **Track-Agnostic Copilot Skills**: Focus on Copilot workflows over framework-specific details

### Key Files for Context
- `java-exercise/0-Java-Personal-Expense-Tracker-Breakout.md` - Java Track: Complete course overview
- `python-exercise/0-Python-Personal-Expense-Tracker-Breakout.md` - Python Track: Complete course overview
- `dotnet-exercise/0-DotNet-Personal-Expense-Tracker-Breakout.md` - .NET Track: Complete course overview
- `python-data-analysis-exercise/README.md` - Python Data Analysis Track: Complete course overview
- `catalog/GitHub Copilot - 1 Day - Personal Expense Tracker.md` - Complete course curriculum
- `day1/README.md` - Day 1 learning materials (Copilot basics)
- `day2/README.md` - Day 2 learning materials (Advanced Copilot)
- `README.md` - Course structure and learning objectives
- `.github/agents/AgentForPerformanceOptimization.agent.md` - Performance optimization agent for all four tracks

## Common Development Tasks

- **Adding REST Endpoints**: 
  - Java: Use `@RestController`, return `ResponseEntity`
  - Python: Use FastAPI decorators (`@app.get`, `@app.post`)
  - .NET: Use Minimal APIs or Controllers with action methods
- **Documentation Updates**: Follow emoji patterns and markdown structure in day1/ and day2/ folders
- **Configuration Changes**: Update `application.properties` (Java), `.env` (Python), or `appsettings.json` (.NET)
- **Exercise Creation**: Add new exercises to track-specific exercise directories with proper numbering

## Cross-Platform Development Notes

- **Java Track**: Requires JDK 21, Maven; runs on port 8080
- **Python Track**: Requires Python 3.11+; runs on port 8000 (uvicorn default)
- **.NET Track**: Requires .NET 9+ SDK; runs on port 5000/5001
- **Python Data Analysis Track**: Requires Python 3.9+; Jupyter on port 8888
- **IDE Support**: VS Code (all tracks), IntelliJ IDEA (Java), PyCharm (Python), Visual Studio (.NET)
- **Testing**: Spring Boot Test for Java, pytest for Python, xUnit for .NET, pytest for Data Analysis

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
