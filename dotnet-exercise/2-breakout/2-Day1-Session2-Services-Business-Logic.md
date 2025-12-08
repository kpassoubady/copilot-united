# 🏗️ Day 1 - Session 2: Personal Expense Tracker - Services & Business Logic (45 mins)

## 🎯 Learning Objectives

By the end of this session, you will:

- Create service interfaces and implementations with dependency injection
- Implement FluentValidation for business rules
- Generate comprehensive unit tests with xUnit
- Create realistic sample data using Copilot
- Master pattern-based AI code generation

**⏱️ Time Allocation: 45 minutes (includes AI-assisted testing)**

## 🤖 GitHub Copilot Focus: Pattern Recognition & Test Generation

**Today's Copilot Skills:**

- Pattern-based code generation for services
- FluentValidation rule creation
- Unit test generation with AAA pattern
- Realistic test data creation
- Intermediate context-aware suggestions

📚 **Reference**: [Copilot Mastery Guide](../0-copilot-mastery-guide.md)

---

## 📝 Step 1: Create DTOs (8 minutes)

### 📦 Create Data Transfer Objects

**Copilot Prompt:**

```text
/generate Create DTOs in DTOs/ directory:

1. CategoryDto.cs - for reading categories:
   - Guid Id
   - string Name
   - string? Description
   - string? Icon
   - string? Color
   - int ExpenseCount
   - DateTime CreatedAt

2. CreateCategoryDto.cs - for creating categories:
   - string Name (required, max 100)
   - string? Description (max 255)
   - string? Icon (max 50)
   - string? Color (7 chars, regex for hex)
   - Include Data Annotations

3. UpdateCategoryDto.cs - for updating categories:
   - Same as CreateCategoryDto

4. ExpenseDto.cs - for reading expenses:
   - Guid Id
   - decimal Amount
   - string Description
   - DateTime ExpenseDate
   - Guid CategoryId
   - string CategoryName
   - string? CategoryColor
   - DateTime CreatedAt

5. CreateExpenseDto.cs - for creating expenses:
   - decimal Amount (required, > 0)
   - string Description (required, max 255)
   - DateTime ExpenseDate
   - Guid CategoryId
   - Include Data Annotations

6. UpdateExpenseDto.cs - for updating expenses:
   - Same as CreateExpenseDto
```

---

## 📝 Step 2: Create Service Interfaces (5 minutes)

### 🔧 Service Interface Definitions

**Copilot Prompt:**

```text
/generate Create service interfaces in Services/ directory:

1. Services/ICategoryService.cs:
   - Task<IEnumerable<CategoryDto>> GetAllCategoriesAsync()
   - Task<CategoryDto?> GetCategoryByIdAsync(Guid id)
   - Task<CategoryDto> CreateCategoryAsync(CreateCategoryDto dto)
   - Task<CategoryDto> UpdateCategoryAsync(Guid id, UpdateCategoryDto dto)
   - Task DeleteCategoryAsync(Guid id)
   - Task<bool> CategoryExistsAsync(Guid id)

2. Services/IExpenseService.cs:
   - Task<IEnumerable<ExpenseDto>> GetAllExpensesAsync()
   - Task<IEnumerable<ExpenseDto>> GetExpensesByCategoryAsync(Guid categoryId)
   - Task<ExpenseDto?> GetExpenseByIdAsync(Guid id)
   - Task<ExpenseDto> CreateExpenseAsync(CreateExpenseDto dto)
   - Task<ExpenseDto> UpdateExpenseAsync(Guid id, UpdateExpenseDto dto)
   - Task DeleteExpenseAsync(Guid id)
   - Task<decimal> GetTotalExpensesAsync()
   - Task<Dictionary<string, decimal>> GetExpensesByCategoryGroupAsync()
```

---

## 📝 Step 3: Create FluentValidation Validators (10 minutes)

### ✅ FluentValidation Rules

**Copilot Prompt:**

```text
/generate Create FluentValidation validators in Validators/ directory:

1. CreateCategoryDtoValidator.cs:
   - Name: Required, max length 100, must be unique (async rule checking database)
   - Description: Optional, max length 255
   - Color: Optional, must match hex pattern #RRGGBB
   - Icon: Optional, max length 50

2. CreateExpenseDtoValidator.cs:
   - Amount: Required, must be > 0, max 2 decimal places
   - Description: Required, max length 255
   - ExpenseDate: Required, cannot be future date
   - CategoryId: Required, must exist in database (async rule)

Include proper error messages and async database checks using DbContext
```

**Example Output** (`Validators/CreateCategoryDtoValidator.cs`):

```csharp
using FluentValidation;
using ExpenseTracker.Web.DTOs;
using ExpenseTracker.Web.Data;
using Microsoft.EntityFrameworkCore;

namespace ExpenseTracker.Web.Validators;

public class CreateCategoryDtoValidator : AbstractValidator<CreateCategoryDto>
{
    private readonly ExpenseTrackerContext _context;

    public CreateCategoryDtoValidator(ExpenseTrackerContext context)
    {
        _context = context;

        RuleFor(x => x.Name)
            .NotEmpty().WithMessage("Category name is required")
            .MaximumLength(100).WithMessage("Category name cannot exceed 100 characters")
            .MustAsync(BeUniqueName).WithMessage("Category name already exists");

        RuleFor(x => x.Description)
            .MaximumLength(255).WithMessage("Description cannot exceed 255 characters")
            .When(x => !string.IsNullOrEmpty(x.Description));

        RuleFor(x => x.Color)
            .Matches(@"^#[0-9A-Fa-f]{6}$").WithMessage("Color must be a valid hex code (#RRGGBB)")
            .When(x => !string.IsNullOrEmpty(x.Color));

        RuleFor(x => x.Icon)
            .MaximumLength(50).WithMessage("Icon cannot exceed 50 characters")
            .When(x => !string.IsNullOrEmpty(x.Icon));
    }

    private async Task<bool> BeUniqueName(string name, CancellationToken cancellationToken)
    {
        return !await _context.Categories.AnyAsync(c => c.Name == name, cancellationToken);
    }
}
```

---

## 📝 Step 4: Implement Service Layer (15 minutes)

### 🔧 ExpenseService Implementation

**Copilot Prompt:**

```text
/generate Create ExpenseService implementation in Services/ExpenseService.cs:
- Implement IExpenseService interface
- Use ExpenseTrackerContext via dependency injection
- Map entities to DTOs using manual mapping or extension methods
- Include proper error handling with custom exceptions
- Use async/await patterns
- Add XML documentation comments
- Include logging (inject ILogger<ExpenseService>)

Follow repository pattern, service layer best practices
```

**Key Methods to Generate**:

```csharp
public class ExpenseService : IExpenseService
{
    private readonly ExpenseTrackerContext _context;
    private readonly ILogger<ExpenseService> _logger;

    public ExpenseService(ExpenseTrackerContext context, ILogger<ExpenseService> logger)
    {
        _context = context;
        _logger = logger;
    }

    public async Task<IEnumerable<ExpenseDto>> GetAllExpensesAsync()
    {
        // Implementation with Include for Category
    }

    public async Task<ExpenseDto> CreateExpenseAsync(CreateExpenseDto dto)
    {
        // Validate category exists
        // Create entity
        // Save changes
        // Return DTO
    }

    // ... other methods
}
```

### 🔧 CategoryService Implementation

Similar pattern for `Services/CategoryService.cs` implementing `ICategoryService`.

---

## 📝 Step 5: Create Unit Tests (10 minutes)

### 🧪 Generate Comprehensive Tests

**Copilot Prompt:**

```text
/generate Create xUnit test project and test class for ExpenseService:

1. Create test project:
   dotnet new xunit -n ExpenseTracker.Tests -o tests/ExpenseTracker.Tests
   dotnet sln add tests/ExpenseTracker.Tests

2. Add packages:
   - Microsoft.EntityFrameworkCore.InMemory
   - Moq
   - FluentAssertions
   - xunit
   - xunit.runner.visualstudio

3. Create ExpenseServiceTests.cs with tests:
   - GetAllExpensesAsync_ReturnsAllExpenses
   - GetExpenseByIdAsync_ValidId_ReturnsExpense
   - GetExpenseByIdAsync_InvalidId_ReturnsNull
   - CreateExpenseAsync_ValidData_CreatesExpense
   - CreateExpenseAsync_InvalidCategoryId_ThrowsException
   - UpdateExpenseAsync_ValidData_UpdatesExpense
   - DeleteExpenseAsync_ValidId_DeletesExpense
   - GetTotalExpensesAsync_CalculatesCorrectTotal

Use Arrange-Act-Assert pattern, in-memory database, realistic test data
```

**Example Test**:

```csharp
using Xunit;
using FluentAssertions;
using Microsoft.EntityFrameworkCore;
using ExpenseTracker.Web.Data;
using ExpenseTracker.Web.Services;
using ExpenseTracker.Web.Models;
using ExpenseTracker.Web.DTOs;
using Microsoft.Extensions.Logging.Abstractions;

namespace ExpenseTracker.Tests.Services;

public class ExpenseServiceTests : IDisposable
{
    private readonly ExpenseTrackerContext _context;
    private readonly ExpenseService _service;

    public ExpenseServiceTests()
    {
        var options = new DbContextOptionsBuilder<ExpenseTrackerContext>()
            .UseInMemoryDatabase(databaseName: Guid.NewGuid().ToString())
            .Options;

        _context = new ExpenseTrackerContext(options);
        _service = new ExpenseService(_context, NullLogger<ExpenseService>.Instance);

        SeedTestData();
    }

    private void SeedTestData()
    {
        var category = new Category { Id = Guid.NewGuid(), Name = "Food" };
        _context.Categories.Add(category);

        var expense = new Expense 
        { 
            Id = Guid.NewGuid(), 
            Amount = 25.50m, 
            Description = "Lunch",
            ExpenseDate = DateTime.Today,
            CategoryId = category.Id
        };
        _context.Expenses.Add(expense);

        _context.SaveChanges();
    }

    [Fact]
    public async Task GetAllExpensesAsync_ReturnsAllExpenses()
    {
        // Arrange - already done in constructor

        // Act
        var result = await _service.GetAllExpensesAsync();

        // Assert
        result.Should().NotBeEmpty();
        result.Should().HaveCount(1);
        result.First().Description.Should().Be("Lunch");
    }

    [Fact]
    public async Task CreateExpenseAsync_ValidData_CreatesExpense()
    {
        // Arrange
        var category = await _context.Categories.FirstAsync();
        var dto = new CreateExpenseDto
        {
            Amount = 50.00m,
            Description = "Dinner",
            ExpenseDate = DateTime.Today,
            CategoryId = category.Id
        };

        // Act
        var result = await _service.CreateExpenseAsync(dto);

        // Assert
        result.Should().NotBeNull();
        result.Amount.Should().Be(50.00m);
        result.Description.Should().Be("Dinner");

        var dbExpense = await _context.Expenses.FindAsync(result.Id);
        dbExpense.Should().NotBeNull();
    }

    public void Dispose()
    {
        _context.Database.EnsureDeleted();
        _context.Dispose();
    }
}
```

### 🚀 Run Tests

```bash
# Run all tests
dotnet test

# Run with detailed output
dotnet test --logger "console;verbosity=detailed"

# Expected: All tests passing ✅
```

---

## 📝 Step 6: Register Services in DI Container (2 minutes)

### ⚙️ Update Program.cs

Add service registrations:

```csharp
// Add services to DI container
builder.Services.AddScoped<IExpenseService, ExpenseService>();
builder.Services.AddScoped<ICategoryService, CategoryService>();

// Add FluentValidation
builder.Services.AddFluentValidationAutoValidation();
builder.Services.AddValidatorsFromAssemblyContaining<Program>();
```

---

## ✅ Session Verification (5 minutes)

### 🧪 Final Verification

1. **Build Solution**: `dotnet build` - should succeed
2. **Run Tests**: `dotnet test` - all tests should pass
3. **Run Application**: `dotnet run` - should start without errors
4. **Check Services**: Services should be available via DI

---

## 🎉 Session Complete!

### ✅ What You've Built

- ✅ Complete DTO layer for data transfer
- ✅ Service interfaces with clear contracts
- ✅ FluentValidation rules with async database checks
- ✅ ExpenseService and CategoryService implementations
- ✅ 15+ comprehensive unit tests with xUnit
- ✅ Dependency injection configured

### 📚 Copilot Skills Learned

- ✅ Pattern-based service generation
- ✅ FluentValidation rule creation
- ✅ Comprehensive test generation
- ✅ Realistic test data creation
- ✅ Intermediate context-aware coding

### 🚀 Next Session

**Session 3: REST APIs & Controllers** - Build RESTful API endpoints with Chat Interface mastery!

**Great work! Take a 5-minute break before afternoon sessions.** ☕
