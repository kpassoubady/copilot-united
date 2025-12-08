# 🏗️ Day 1 - Session 3: Personal Expense Tracker - REST APIs & Controllers (45 mins)

## 🎯 Learning Objectives

By the end of this session, you will:

- Master GitHub Copilot Chat Interface for interactive development
- Build REST API endpoints using Controllers or Minimal APIs
- Implement proper HTTP status codes and error handling
- Use Copilot agents (`@workspace`, `@terminal`, `@git`)
- Test APIs using Swagger and terminal tools

**⏱️ Time Allocation: 45 minutes (Chat Interface mastery focus)**

## 🤖 GitHub Copilot Focus: Chat Interface & Agent Mastery

**Today's Copilot Skills:**

- Advanced Chat Interface usage
- Agent-based context (`@workspace`, `@terminal`, `@git`)
- Slash commands (`/explain`, `/fix`, `/generate`)
- Chat-guided API design patterns
- Terminal-integrated testing with Copilot

---

## 📝 Step 1: Choose Your API Style (5 minutes)

### 🎯 Two Approaches

| Feature | **Option A: Minimal APIs** | **Option B: Controllers** |
|---------|---------------------------|---------------------------|
| **Style** | Modern, lightweight (like FastAPI) | Traditional MVC (like Spring Boot) |
| **Location** | Functions in `Program.cs` | Class files in `Controllers/` |
| **Boilerplate** | Less code, more concise | More structure, more verbose |
| **Best For** | Microservices, small APIs | Large applications, team projects |
| **Background** | New to .NET | Java/Spring developers |

**📌 For This Bootcamp**: We'll follow **Option B: Controllers** as the primary approach because:
- Better organized for enterprise applications
- More familiar to Java/Spring developers
- Clearer separation of concerns

> **Note**: Option A (Minimal APIs) is shown as an alternative reference in Step 2B. You only need to complete ONE option, not both.

---

## 📝 Step 2: Create API Controllers (Option B) (20 minutes)

### 🔧 ExpensesController Implementation

**Copilot Chat Prompt:**

```text
@workspace Using GitHub Copilot Chat Interface:

"Create an ASP.NET Core API Controller for Expenses in Controllers/Api/ExpensesController.cs:
- Route: /api/expenses
- Inject IExpenseService
- Implement GET all expenses - returns 200 OK
- Implement GET by id - returns 200 OK or 404 NotFound
- Implement POST create - returns 201 Created with location header
- Implement PUT update - returns 204 NoContent or 404
- Implement DELETE - returns 204 NoContent or 404
- Include proper HTTP status codes
- Add ProducesResponseType attributes for OpenAPI
- Add XML documentation comments
- Use async/await patterns"
```

**Expected Output**:

```csharp
using Microsoft.AspNetCore.Mvc;
using ExpenseTracker.Web.Services;
using ExpenseTracker.Web.DTOs;

namespace ExpenseTracker.Web.Controllers.Api;

[ApiController]
[Route("api/[controller]")]
[Produces("application/json")]
public class ExpensesController : ControllerBase
{
    private readonly IExpenseService _expenseService;
    private readonly ILogger<ExpensesController> _logger;

    public ExpensesController(IExpenseService expenseService, ILogger<ExpensesController> logger)
    {
        _expenseService = expenseService;
        _logger = logger;
    }

    /// <summary>
    /// Get all expenses
    /// </summary>
    [HttpGet]
    [ProducesResponseType(typeof(IEnumerable<ExpenseDto>), StatusCodes.Status200OK)]
    public async Task<ActionResult<IEnumerable<ExpenseDto>>> GetAllExpenses()
    {
        var expenses = await _expenseService.GetAllExpensesAsync();
        return Ok(expenses);
    }

    /// <summary>
    /// Get expense by ID
    /// </summary>
    [HttpGet("{id}")]
    [ProducesResponseType(typeof(ExpenseDto), StatusCodes.Status200OK)]
    [ProducesResponseType(StatusCodes.Status404NotFound)]
    public async Task<ActionResult<ExpenseDto>> GetExpense(Guid id)
    {
        var expense = await _expenseService.GetExpenseByIdAsync(id);
        if (expense == null)
        {
            _logger.LogWarning("Expense with ID {Id} not found", id);
            return NotFound();
        }
        return Ok(expense);
    }

    /// <summary>
    /// Create new expense
    /// </summary>
    [HttpPost]
    [ProducesResponseType(typeof(ExpenseDto), StatusCodes.Status201Created)]
    [ProducesResponseType(StatusCodes.Status400BadRequest)]
    public async Task<ActionResult<ExpenseDto>> CreateExpense([FromBody] CreateExpenseDto dto)
    {
        if (!ModelState.IsValid)
            return BadRequest(ModelState);

        var created = await _expenseService.CreateExpenseAsync(dto);
        return CreatedAtAction(nameof(GetExpense), new { id = created.Id }, created);
    }

    /// <summary>
    /// Update existing expense
    /// </summary>
    [HttpPut("{id}")]
    [ProducesResponseType(StatusCodes.Status204NoContent)]
    [ProducesResponseType(StatusCodes.Status404NotFound)]
    [ProducesResponseType(StatusCodes.Status400BadRequest)]
    public async Task<IActionResult> UpdateExpense(Guid id, [FromBody] UpdateExpenseDto dto)
    {
        if (!ModelState.IsValid)
            return BadRequest(ModelState);

        try
        {
            await _expenseService.UpdateExpenseAsync(id, dto);
            return NoContent();
        }
        catch (KeyNotFoundException)
        {
            return NotFound();
        }
    }

    /// <summary>
    /// Delete expense
    /// </summary>
    [HttpDelete("{id}")]
    [ProducesResponseType(StatusCodes.Status204NoContent)]
    [ProducesResponseType(StatusCodes.Status404NotFound)]
    public async Task<IActionResult> DeleteExpense(Guid id)
    {
        try
        {
            await _expenseService.DeleteExpenseAsync(id);
            return NoContent();
        }
        catch (KeyNotFoundException)
        {
            return NotFound();
        }
    }

    /// <summary>
    /// Get total expenses amount
    /// </summary>
    [HttpGet("total")]
    [ProducesResponseType(typeof(decimal), StatusCodes.Status200OK)]
    public async Task<ActionResult<decimal>> GetTotal()
    {
        var total = await _expenseService.GetTotalExpensesAsync();
        return Ok(total);
    }

    /// <summary>
    /// Get expenses grouped by category
    /// </summary>
    [HttpGet("by-category")]
    [ProducesResponseType(typeof(Dictionary<string, decimal>), StatusCodes.Status200OK)]
    public async Task<ActionResult<Dictionary<string, decimal>>> GetByCategory()
    {
        var grouped = await _expenseService.GetExpensesByCategoryGroupAsync();
        return Ok(grouped);
    }
}
```

### 🔧 CategoriesController Implementation

Similar pattern for `Controllers/Api/CategoriesController.cs`.

**Copilot Prompt:**
```text
@workspace "Create CategoriesController following the same pattern as ExpensesController"
```

---

## 📝 Step 2B: Create Minimal APIs (Option A - Alternative) (20 minutes)

### 🚀 Minimal API Endpoints

If you prefer Minimal APIs, add to `Program.cs`:

```csharp
// Expense endpoints
var expensesApi = app.MapGroup("/api/expenses")
    .WithTags("Expenses")
    .WithOpenApi();

expensesApi.MapGet("/", async (IExpenseService service) =>
{
    var expenses = await service.GetAllExpensesAsync();
    return Results.Ok(expenses);
})
.WithName("GetAllExpenses")
.Produces<IEnumerable<ExpenseDto>>();

expensesApi.MapGet("/{id}", async (Guid id, IExpenseService service) =>
{
    var expense = await service.GetExpenseByIdAsync(id);
    return expense is not null ? Results.Ok(expense) : Results.NotFound();
})
.WithName("GetExpense")
.Produces<ExpenseDto>()
.Produces(StatusCodes.Status404NotFound);

expensesApi.MapPost("/", async (CreateExpenseDto dto, IExpenseService service) =>
{
    var created = await service.CreateExpenseAsync(dto);
    return Results.Created($"/api/expenses/{created.Id}", created);
})
.WithName("CreateExpense")
.Produces<ExpenseDto>(StatusCodes.Status201Created);

// ... similar for PUT, DELETE
```

---

## 📝 Step 3: Test APIs with Swagger (10 minutes)

### 🧪 Using Swagger UI

```bash
# Run application
dotnet run

# Open Swagger UI
# https://localhost:5001/swagger
```

**Copilot-Assisted Testing**:

```text
@terminal "What curl commands can I use to test the expenses API?"
```

### 🔍 Test with curl

```bash
# Get all expenses
curl -X GET https://localhost:5001/api/expenses -k

# Create expense
curl -X POST https://localhost:5001/api/expenses \
  -H "Content-Type: application/json" \
  -d '{
    "amount": 45.99,
    "description": "Grocery shopping",
    "expenseDate": "2025-12-07",
    "categoryId": "<paste-category-id>"
  }' -k

# Get total
curl -X GET https://localhost:5001/api/expenses/total -k
```

---

## 📝 Step 4: Error Handling Middleware (10 minutes)

### 🛡️ Global Exception Handler

**Copilot Prompt:**

```text
@workspace "Create global exception handling middleware in Middleware/ExceptionHandlingMiddleware.cs:
- Catch all unhandled exceptions
- Log errors
- Return appropriate HTTP status codes
- Return problem details JSON
- Handle different exception types (ValidationException, KeyNotFoundException, etc.)"
```

Add to `Program.cs`:

```csharp
app.UseMiddleware<ExceptionHandlingMiddleware>();
```

---

## ✅ Session Verification (5 minutes)

### 🧪 API Testing Checklist

- [ ] Swagger UI loads successfully
- [ ] GET /api/expenses returns 200 OK
- [ ] GET /api/expenses/{id} returns 200 or 404
- [ ] POST /api/expenses creates and returns 201
- [ ] PUT /api/expenses/{id} updates and returns 204
- [ ] DELETE /api/expenses/{id} deletes and returns 204
- [ ] GET /api/expenses/total returns correct sum
- [ ] Error responses return proper JSON

---

## 🎉 Session Complete!

### ✅ What You've Built

- ✅ Complete REST API layer (Controllers or Minimal APIs)
- ✅ Proper HTTP status codes and error handling
- ✅ OpenAPI/Swagger documentation
- ✅ Global exception handling middleware
- ✅ Tested all CRUD operations

### 📚 Copilot Skills Learned

- ✅ Advanced Chat Interface usage
- ✅ Agent-based development (`@workspace`, `@terminal`)
- ✅ Chat-guided API design
- ✅ Terminal-integrated testing
- ✅ Slash command mastery

### 🚀 Next Session

**Session 4: Razor Pages & Web Interface** - Build a beautiful UI with multi-language coordination!

**Take a 5-minute break!** ☕
