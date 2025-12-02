# Day 1: GitHub Copilot Foundation & Backend Development

**Focus**: Interface Mastery & Service Layer Implementation

**Tracks**: Java (Spring Boot) or Python (FastAPI) — choose one based on your setup

## 📚 Learning Materials

### Core GitHub Copilot Basics

- [GitHub Copilot Essentials](GitHub-Copilot-Day1-Essentials.md) - Day 1 focused techniques and tips
- [Setup Guide](Copilot-Setup-Guide.md) - Installation and configuration
- [Keyboard Shortcuts](Copilot-ShortCuts.md) - Essential shortcuts for productivity
- [Copilot Limitations](Copilot-Limitations.md) - Understanding boundaries and best practices

### Interface & Commands

- [Slash Commands](Copilot-Slash-Commands.md) - /generate, /fix, /explain, /tests commands
- [Built-in Modes](Copilot-Built-In-Modes.md) - Chat modes for different scenarios
- [Chat Participants](Copilot-Chat-Participants.md) - @workspace basics
- [Chat Cookbook](Copilot-Chat-Cookbook.md) - Common chat patterns and examples

### Configuration & Settings

- [VS Code Settings Reference](Copilot-VS-Code-Settings-Reference.md) - Copilot configuration options
- [Disable Copilot](Disable-Copilot.md) - Temporary disabling when needed

## 🎯 Key Learning Activities

### Foundation Building

- **Setup Verification** - [Java Track Setup](../java-exercise/1-setup/day1-backend-setup.md) | [Python Track Setup](../python-exercise/1-setup/day1-backend-setup.md)
- **Interface Mastery** - [Copilot Interface Basics](3-1-Copilot-Interface-Basic-Usage.md)
- **Backend Development** - [Java Track](../java-exercise/2-breakout/2-Day1-Session2-Services-Business-Logic.md) | Python Track (coming soon)
- **Knowledge Assessment** - Interface, shortcuts, and basic commands

### Advanced Skills Development

- **Code Completion Patterns** - Advanced acceptance and navigation strategies
- **Slash Commands Mastery** - Deep dive into /generate, /fix, /explain, /tests
- **Service Layer Implementation** - Complete backend with comprehensive unit tests
- **Student Demonstrations** - Showcase different Copilot techniques and workflows

## 🛠️ Technical Focus

### Spring Boot Backend Development

- **Entity Creation**: JPA entities with validation using Copilot assistance
- **Repository Layer**: Spring Data repositories with custom queries
- **Service Layer**: Business logic implementation with error handling
- **Unit Testing**: JUnit 5 tests generated with /tests command

### GitHub Copilot Skills Developed

- ✅ Basic code completion acceptance and navigation
- ✅ Essential slash commands (/generate, /explain, /fix, /tests)
- ✅ Comment-driven development patterns
- ✅ Interface familiarity and productivity shortcuts
- ✅ Quality assurance through generated testing

## 🎯 Success Criteria

By end of Day 1, students will:

- Navigate Copilot interface confidently
- Use keyboard shortcuts effectively
- Generate backend code with proper validation
- Create unit tests using Copilot assistance
- Understand Copilot's capabilities and limitations
- Build working service layer for expense management

## 📁 Resources

- **Images**: Visual references in [images/](images/) folder
- **Exercise Files**: [Java Track](../java-exercise/) | [Python Track](../python-exercise/)  
- **Setup Scripts**: Day-specific setup verification
- **Project Code**: Located in [../../project1/task-manager/](../project1/task-manager/)

---

## Advanced Context & Web Layer Development

**Focus**: Hash Context Variables & Frontend Implementation

## 📚 Learning Materials (Advanced)

### Advanced Context Mastery

- [Context Mastery Guide](GitHub-Copilot-Day2-Context-Mastery.md) - Advanced techniques and strategies
- [Hash Context Variables](Copilot-Hash-Context.md) - #file, #selection, #codebase, #editor usage
- [Workspace Context](Copilot-Workspace-Context.md) - Understanding workspace-wide context
- [Editing Sessions](Copilot-Editing-Session.md) - Managing multi-file editing workflows

### Advanced Chat Features

- [Custom Chat Modes](Copilot-Custom-Chat-Modes.md) - Creating specialized chat patterns
- [Custom Instructions](Copilot-Custom-Instructions.md) - Personalizing Copilot behavior
- [Prompt Files](Copilot-Prompt-Files.md) - Reusable prompt patterns and templates

## 🎯 Key Learning Activities (Advanced)

### Context Mastery Foundation

- **Setup Verification** - [Java Frontend Setup](../java-exercise/1-setup/day1-frontend-setup.md) | Python Frontend Setup (coming soon)
- **Hash Context Introduction** - #file, #selection, #codebase patterns and strategies
- **Web Layer Development** - [Java Track](../java-exercise/2-breakout/4-Day1-Session-Web-Interface-Templates.md) | Python Track (coming soon)
- **Knowledge Assessment** - Hash context variables and multi-context strategies

### Advanced Context Applications

- **Terminal Context** - `#terminalSelection`, `#terminalLastCommand` for debugging
- **Complete Web Implementation** - Thymeleaf templates, AJAX, and responsive design
- **Student Demonstrations** - Advanced context usage and creative problem-solving
- **Context Optimization** - Best practices for context selection and combination

## 🛠️ Technical Focus (Web Layer)

- **REST Controllers**: API endpoints using #codebase context for consistency
- **Thymeleaf Templates**: Frontend generation with #file references to backend
- **AJAX Integration**: Dynamic functionality with contextual pattern matching
- **Error Handling**: Cross-layer error patterns using #sym context

## 🧠 Context Strategy Mastery

### Layer Building Approach

1. **Broad Context**: Start with #codebase for architectural understanding
2. **Focused Context**: Narrow to #file for specific implementation details
3. **Targeted Context**: Use #selection for precise modifications
4. **Symbol Context**: Apply #sym for cross-file consistency and refactoring

### Multi-Context Combinations

- `#codebase #file:ExpenseService.java` - Create controller following service patterns
- `#selection #file:ExpenseController.java` - Refactor with existing error handling
- `#editor #codebase` - Add features following project-wide patterns

## 🎯 Advanced Skills Developed

- ✅ Hash context variables (#file, #selection, #codebase, #editor)
- ✅ Symbol-based context (#sym) for refactoring and consistency
- ✅ Multi-agent workflows (@workspace, @terminal)
- ✅ Cross-file consistency patterns and maintenance
- ✅ Advanced slash command combinations with context
- ✅ Progressive context building through conversations

## 📁 Additional Resources (Advanced)

- **Template Samples**: Thymeleaf template examples with Bootstrap integration
- **AJAX Patterns**: Dynamic frontend interaction examples
- **Multi-File Workflows**: Cross-layer consistency demonstration files
