# Copilot Edits: Multi-File Editing

Use GitHub Copilot's agent-based editing to make coordinated changes across multiple files.

---

## 🎯 Overview

**Copilot Edits** is an advanced feature that allows you to:
- Make changes across multiple files simultaneously
- Maintain consistency when refactoring
- Create new files as part of a larger change
- Review and accept/reject changes before applying

---

## 🚀 Getting Started

### Opening Copilot Edits

**VS Code:**
- Open Command Palette: `Cmd+Shift+P` (Mac) / `Ctrl+Shift+P` (Windows)
- Search: "Copilot Edits: Open"
- Or click the Copilot Edits icon in the sidebar

### The Edits Interface

1. **Working Set**: Files included in the editing session
2. **Prompt Area**: Describe the changes you want
3. **Preview Panel**: See proposed changes before applying
4. **Accept/Reject**: Control which changes to apply

---

## 📝 Basic Usage

### Add Files to Working Set

1. Click "Add Files" in Copilot Edits panel
2. Select files to include
3. Or drag files from Explorer into the panel

### Describe Your Changes

```
Prompt: Add a new "notes" field to the Expense entity and update:
- The entity class
- The DTO
- The repository
- The service layer
- The controller endpoints
```

### Review and Apply

1. Copilot shows proposed changes for each file
2. Review changes in diff view
3. Click ✓ to accept or ✗ to reject per file
4. Apply accepted changes

---

## 🔧 Common Multi-File Patterns

### Pattern 1: Add New Field Across Layers

```
Prompt: Add a "category" field (String) to the Expense:
- Add to Expense.java entity with JPA annotations
- Add to ExpenseDTO.java
- Update ExpenseMapper to map the field
- Add filter by category to ExpenseRepository
- Update ExpenseService with category filtering
- Add category parameter to controller endpoints
```

### Pattern 2: Rename Across Codebase

```
Prompt: Rename the class "ExpenseManager" to "ExpenseService" across all files:
- Update class name and file name
- Update all imports
- Update all references
- Update test files
```

### Pattern 3: Add New Feature

```
Prompt: Add expense export functionality:
- Create ExportService.java with CSV export method
- Create ExportController.java with /api/expenses/export endpoint
- Add export button to expenses.html template
- Create ExportServiceTest.java with unit tests
```

### Pattern 4: Implement Interface

```
Prompt: Create an Auditable interface and implement it:
- Create Auditable.java interface with createdAt, updatedAt, createdBy
- Implement in Expense.java entity
- Implement in Category.java entity
- Add JPA auditing configuration
```

---

## 💡 Tips for Effective Multi-File Edits

### Be Specific About Files

```
Prompt: Update these specific files:
- src/main/java/com/expense/entity/Expense.java
- src/main/java/com/expense/dto/ExpenseDTO.java
- src/main/java/com/expense/service/ExpenseService.java
```

### Describe the Relationship

```
Prompt: Add validation that ensures:
- ExpenseDTO validates amount > 0
- ExpenseService throws ValidationException for invalid amounts
- ExpenseController returns 400 Bad Request with error details
- Tests verify the validation chain
```

### Include Context

```
Prompt: Following the existing patterns in #codebase:
- Add a new Budget entity similar to Expense
- Create matching DTO, repository, service, and controller
- Follow the same package structure and naming conventions
```

---

## 🔄 Iterative Editing

### Refine Changes

After initial generation:
```
Prompt: The Expense entity changes look good, but also:
- Add @NotNull annotation to the category field
- Add database index for category queries
```

### Partial Accept

1. Accept changes to Entity and DTO
2. Reject changes to Controller
3. Request revised Controller changes:
```
Prompt: Regenerate the controller changes with proper request validation
```

---

## ⚠️ Limitations

- **Preview Required**: Always review changes before applying
- **Complex Refactors**: May need multiple iterations
- **Build Verification**: Run builds after applying changes
- **Test Coverage**: Regenerate or update tests separately

---

## 🔧 Practical Exercises

### Exercise 1: Add a New Field

1. Open Copilot Edits
2. Add Entity, DTO, Service, Controller to working set
3. Prompt: "Add a 'tags' field (List<String>) across all layers"
4. Review and apply changes
5. Verify the application compiles

### Exercise 2: Refactor Package Structure

1. Add multiple files to working set
2. Prompt: "Move all DTOs from com.expense.dto to com.expense.model.dto"
3. Review import updates
4. Apply and verify

### Exercise 3: Add Complete Feature

1. Prompt: "Create a complete Category management feature with CRUD operations"
2. Review generated files
3. Accept/reject individual changes
4. Fill in any gaps manually

---

## ✅ Best Practices

- **Start Small**: Begin with 2-3 files before larger changes
- **Review Carefully**: Check each file's changes individually
- **Test After**: Always run tests after applying edits
- **Commit Incrementally**: Commit working states frequently
- **Use Git**: Easy to revert if changes don't work

---

## 🔗 Related Resources

- [Copilot Editing Session](Copilot-Editing-Session.md) - Single-file editing patterns
- [Workspace Context](Copilot-Workspace-Context.md) - Using `@workspace` for context
- [Copilot Agents](Copilot-Agents.md) - Agent-based assistance
