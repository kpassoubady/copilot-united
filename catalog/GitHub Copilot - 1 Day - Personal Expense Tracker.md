# GitHub Copilot - 1 Day (Personal Expense Tracker)

**Duration**: 1 Day × 8 Hours (including bio-breaks)
**Focus**: Hands-on GitHub Copilot mastery while building a Personal Expense Tracker web app (testing excluded)
**Audience**: Working professionals (language-agnostic)
**Tracks**: Java (Spring Boot) or Python (FastAPI) — same 1‑day flow
**Prerequisites**: IDE with GitHub Copilot enabled; basic Git. Choose one track's tooling:
- Java Track: JDK 21 + Maven
- Python Track: Python 3.11+ (3.12 recommended)

---

## 🎯 Course Overview

This intensive 1-day program focuses on mastering GitHub Copilot through practical development of a Personal Expense Tracker. You’ll learn Copilot’s capabilities across completion, chat, editing, and context usage—prioritizing AI-assisted development workflows over framework details.

---

## 🧭 Main Topics Covered

- Introduction to Generative AI
  - Definition, significance, and industry applications
  - Basics of natural language generation
- Gen AI Tools Comparison
  - Developer tools: GitHub Copilot, Cursor
  - Productivity tools: Microsoft Copilot, ChatGPT
- Introduction to GitHub Copilot
  - AI-powered coding features and productivity gains
  - Setup in supported IDEs, configuration for optimal use
  - Navigating the interface and context-aware suggestions
- Developing with GitHub Copilot
  - Code completion, refactoring, and reliability improvements
  - Debugging/issue resolution with AI suggestions
  - Automated documentation (inline comments, function explanations)
  - Test case generation concepts (covered conceptually; no implementation today)
- Maximizing Efficiency
  - Customizing settings, language preferences, and integrations
  - Shortcuts and commands for efficient navigation
  - Integrating into GitHub workflows; ethical and security considerations
- Advanced Usage
  - Extending with plugins
  - Advanced refactoring assist and optimization
  - Fine-tuning settings for different environments
  - Copilot Agents and participants for architecture and reviews
  - Tool sets and integrations for workflow acceleration
  - Auto-commit workflows for rapid iteration (optional)
  - VS Code Copilot logs and troubleshooting
  - Restore points and rollback strategies

---

## 📚 Learning Outcomes

- Master core Copilot features: completion, chat, inline edits, and context usage
- Apply effective prompting strategies and utilize `@workspace` and hash contexts
- Build a working Personal Expense Tracker backend and web UI with Copilot guidance
- Integrate Copilot into daily workflows and GitHub collaboration
- Understand Copilot’s limits, security, and ethical considerations

---

## 🛠️ Project Context (Technology-Agnostic, Java-Friendly)

- Two parallel tracks share the same Copilot curriculum:
  - Java Track: Spring Boot Task Manager (H2 for dev)
  - Python Track: FastAPI Task Manager (SQLite for dev)
- Frontend: Thymeleaf/Jinja2 templates; Bootstrap for styling
- Tools: GitHub Copilot (VS Code/IntelliJ), REST Client (optional)

Note: The course emphasizes Copilot workflows over specific framework training.

---

## 🧩 Track Setup (Install Guides)

Install prerequisites for your chosen track before class:

- Java Track (Spring Boot Task Manager)
  - Windows: `project1/install/proj1-install-win.md`
  - macOS: `project1/install/proj1-install-mac.md`

- Python Track (FastAPI Task Manager)
  - Windows: `project2/install/proj2-install-win.md`
  - macOS: `project2/install/proj2-install-mac.md`

All install links in one place: `./install.md`

---

## ⏰ 8-Hour Schedule

### 1. Foundations: Generative AI + Tools Landscape (45 min)

- Generative AI concepts and NLG basics
- Comparison: GitHub Copilot vs Cursor, Microsoft Copilot vs ChatGPT
- When to use AI assistance vs traditional development

### 2. Copilot Setup & Interface Mastery (45 min)

- Install/validate GitHub Copilot; configure settings for optimal suggestions
- Keyboard shortcuts and acceptance patterns
- Understanding suggestion quality, context-aware completions
- References: `day1/1.4-Copilot-IDE-Integration.md`, `day1/Copilot-ShortCuts.md`

### 3. Breakout 1: Backend Modeling with Copilot (90 min)

- Exercise: Generate entities (Expense, Category) via Copilot completion
- Implement repositories with custom queries using chat guidance
- Add service layer (business logic) with `/generate` and `/explain`
- References: `day1/3-3-Code-Generation-Practical-Exercises.md`, `day1/Copilot-Chat-Cookbook.md`

### Bio Break (15 min)

### 4. Copilot Chat & Context Mastery (45 min)

- Hash context variables: `#file`, `#selection`, `#codebase`, `#editor`, `#sym`
- Multi-context strategies and progressive context building
- References: `day1/Copilot-Hash-Context.md`, `day1/Copilot-Workspace-Context.md`

### 5. Breakout 2: Web Layer & APIs (85 min)

- Generate REST controllers using `#codebase` for consistency
- Implement basic Thymeleaf templates with Bootstrap; optional AJAX
- API testing via REST Client examples (conceptual; focus on Copilot workflows)
- References: `day1/Copilot-Editing-Session.md`, `day1/Copilot-Custom-Chat-Modes.md`

### Lunch Break (45 min)

### 6. Efficiency & Advanced Usage (45 min)

- Custom instructions; tailoring behavior to your project
- Plugins and integrations; advanced refactoring assistance
- Ethical use, limitations, and security best practices
- References: `day1/Copilot-Limitations.md`, `day1/Copilot-Custom-Instructions.md`

### 6a. Troubleshooting and Recovery (15 min)

- Reading Copilot logs for diagnosing issues
- Using restore points and rollback strategies in VS Code
- When to disable Copilot temporarily; safe re-enable patterns
- References: `day1/VS-Code-GitHub-Copilot-Logs.md`, `day1/VS-Code-Restore-Points.md`, `day1/Disable-Copilot.md`

### Evening Break (20 min)

### 7. Wrap-up & Workflow Integration (35 min)

- Integrating Copilot into GitHub workflows and PRs
- Documentation generation patterns with context
- Personal Copilot workflow blueprint

---

## 🧪 What’s Excluded Today

- Testing exercises (JUnit/TestNG/Selenium) are intentionally excluded from this 1-day course.
- Testing is discussed conceptually but not implemented.

---

## ✅ Deliverables (End of Day)

- Working backend with entities, repositories, and services
- Functional REST endpoints and minimal web UI/templates
- Documented code using Copilot-assisted explanations and inline comments

---

## 🔧 Copilot Workflow Highlights (Practiced Throughout)

- Prompting patterns and progressive context building
- Slash commands: `/explain`, `/generate`, `/fix`, `/optimize` (testing-related commands discussed only)
- `@workspace` insights for architecture and consistency
- Multi-file editing sessions and refactoring assistance

---

## 📎 Reference Materials

- Core: `day1/README.md`, `day1/Copilot-Setup-Guide.md`, `day1/3-1-Copilot-Interface-Basic-Usage.md`
- Advanced Context & Web: `day1/Copilot-Hash-Context.md`, `day1/Copilot-Editing-Session.md`
- Shortcuts & Settings: `day1/Copilot-ShortCuts.md`, `day1/Copilot-VS-Code-Settings-Reference.md`
- Customizations: `day1/Copilot-Custom-Chat-Modes.md`, `day1/Copilot-Custom-Instructions.md`
 - Agents & Tools: `day1/Copilot-Agents.md`, `day1/Copilot-Tool-Sets.md`
 - Automation: `day1/Copilot-Auto-Commit-Setup.md`
 - Troubleshooting: `day1/VS-Code-GitHub-Copilot-Logs.md`, `day1/VS-Code-Restore-Points.md`

---

## 💡 Teaching Philosophy

- Learn by doing with AI-first workflows
- Emphasize context-aware assistance over framework minutiae
- Build a portfolio-ready app while mastering Copilot usage
