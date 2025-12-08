# 🏗️ Day 1 - Session 4: Personal Expense Tracker - Razor Pages & Web Interface (45 mins)

## 🎯 Learning Objectives

By the end of this session, you will:

- Create Razor Pages with Bootstrap 5 integration
- Practice multi-language coordination (C# + Razor + JavaScript)
- Implement Copilot-assisted form handling with Tag Helpers
- Build interactive dashboards with Chart.js
- Master frontend pattern recognition across languages

**⏱️ Time Allocation: 45 minutes (Frontend AI coordination)**

## 🤖 GitHub Copilot Focus: Multi-Language Coordination

**Today's Copilot Skills:**

- Multi-language context (C#, Razor, HTML, CSS, JavaScript)
- Frontend pattern recognition
- UI component generation
- JavaScript integration with Copilot
- Professional frontend AI workflows

---

## 📝 Step 1: Create Shared Layout (10 minutes)

### 🎨 Main Layout Template

**Copilot Prompt:**

```text
@workspace "Create Razor Pages _Layout.cshtml in Pages/Shared/ with:
- Bootstrap 5.3.2 CDN links (CSS and JS)
- jQuery 3.7.1 CDN
- Chart.js 4.4.0 CDN
- Responsive navigation bar with links to Home, Expenses, Categories
- Main content area with @RenderBody()
- Footer with copyright
- Include site.css and RenderSection for page-specific scripts
- Modern, clean design"
```

**Expected Output** (`Pages/Shared/_Layout.cshtml`):

```cshtml
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>@ViewData["Title"] - Expense Tracker</title>
    
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Font Awesome -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <!-- Custom CSS -->
    <link rel="stylesheet" href="~/css/site.css" asp-append-version="true" />
</head>
<body>
    <header>
        <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
            <div class="container-fluid">
                <a class="navbar-brand" href="/">
                    <i class="fas fa-wallet"></i> Expense Tracker
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav ms-auto">
                        <li class="nav-item">
                            <a class="nav-link" asp-page="/Index">
                                <i class="fas fa-home"></i> Dashboard
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" asp-page="/Expenses/Index">
                                <i class="fas fa-money-bill-wave"></i> Expenses
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" asp-page="/Categories/Index">
                                <i class="fas fa-tags"></i> Categories
                            </a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    </header>

    <main class="container my-4">
        @RenderBody()
    </main>

    <footer class="footer mt-auto py-3 bg-light">
        <div class="container text-center">
            <span class="text-muted">© 2025 Expense Tracker - Built with GitHub Copilot</span>
        </div>
    </footer>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    <!-- jQuery -->
    <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
    <!-- Chart.js -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
    <!-- Custom scripts -->
    <script src="~/js/site.js" asp-append-version="true"></script>
    @await RenderSectionAsync("Scripts", required: false)
</body>
</html>
```

---

## 📝 Step 2: Create Dashboard Page (15 minutes)

### 📊 Dashboard with Chart.js

**Copilot Prompt (C# PageModel):**

```text
@workspace "Create Razor Page model Pages/Index.cshtml.cs:
- Inject IExpenseService and ICategoryService
- OnGetAsync method to load:
  * Total expenses (decimal)
  * Expense count (int)
  * Category count (int)
  * Recent expenses (List<ExpenseDto>, top 5)
  * Expenses by category for Chart.js (Dictionary<string, decimal>)
- Properties for all data with proper types"
```

**Expected Output** (`Pages/Index.cshtml.cs`):

```csharp
using Microsoft.AspNetCore.Mvc.RazorPages;
using ExpenseTracker.Web.Services;
using ExpenseTracker.Web.DTOs;

namespace ExpenseTracker.Web.Pages;

public class IndexModel : PageModel
{
    private readonly IExpenseService _expenseService;
    private readonly ICategoryService _categoryService;

    public IndexModel(IExpenseService expenseService, ICategoryService categoryService)
    {
        _expenseService = expenseService;
        _categoryService = categoryService;
    }

    public decimal TotalExpenses { get; set; }
    public int ExpenseCount { get; set; }
    public int CategoryCount { get; set; }
    public List<ExpenseDto> RecentExpenses { get; set; } = new();
    public Dictionary<string, decimal> ExpensesByCategory { get; set; } = new();

    public async Task OnGetAsync()
    {
        TotalExpenses = await _expenseService.GetTotalExpensesAsync();
        
        var allExpenses = await _expenseService.GetAllExpensesAsync();
        ExpenseCount = allExpenses.Count();
        RecentExpenses = allExpenses.OrderByDescending(e => e.ExpenseDate).Take(5).ToList();

        var allCategories = await _categoryService.GetAllCategoriesAsync();
        CategoryCount = allCategories.Count();

        ExpensesByCategory = await _expenseService.GetExpensesByCategoryGroupAsync();
    }
}
```

**Copilot Prompt (Razor View):**

```text
@workspace "Create Razor Page view Pages/Index.cshtml:
- Display summary cards for Total Expenses, Expense Count, Category Count
- Show Chart.js pie chart for expenses by category
- Display recent expenses table
- Use Bootstrap 5 card components
- Include responsive grid layout
- Add Font Awesome icons
- Include JavaScript for Chart.js in @section Scripts"
```

**Expected Output** (`Pages/Index.cshtml`):

```cshtml
@page
@model IndexModel
@{
    ViewData["Title"] = "Dashboard";
}

<div class="row mb-4">
    <div class="col-md-4">
        <div class="card text-white bg-primary">
            <div class="card-body">
                <h5 class="card-title"><i class="fas fa-dollar-sign"></i> Total Expenses</h5>
                <h2 class="card-text">$@Model.TotalExpenses.ToString("N2")</h2>
            </div>
        </div>
    </div>
    <div class="col-md-4">
        <div class="card text-white bg-success">
            <div class="card-body">
                <h5 class="card-title"><i class="fas fa-receipt"></i> Total Transactions</h5>
                <h2 class="card-text">@Model.ExpenseCount</h2>
            </div>
        </div>
    </div>
    <div class="col-md-4">
        <div class="card text-white bg-info">
            <div class="card-body">
                <h5 class="card-title"><i class="fas fa-tags"></i> Categories</h5>
                <h2 class="card-text">@Model.CategoryCount</h2>
            </div>
        </div>
    </div>
</div>

<div class="row mb-4">
    <div class="col-md-6">
        <div class="card">
            <div class="card-header">
                <h5><i class="fas fa-chart-pie"></i> Expenses by Category</h5>
            </div>
            <div class="card-body">
                <canvas id="categoryChart"></canvas>
            </div>
        </div>
    </div>
    <div class="col-md-6">
        <div class="card">
            <div class="card-header">
                <h5><i class="fas fa-clock"></i> Recent Expenses</h5>
            </div>
            <div class="card-body">
                <table class="table table-hover">
                    <thead>
                        <tr>
                            <th>Date</th>
                            <th>Description</th>
                            <th>Category</th>
                            <th>Amount</th>
                        </tr>
                    </thead>
                    <tbody>
                        @foreach (var expense in Model.RecentExpenses)
                        {
                            <tr>
                                <td>@expense.ExpenseDate.ToString("MM/dd/yyyy")</td>
                                <td>@expense.Description</td>
                                <td>
                                    <span class="badge" style="background-color: @expense.CategoryColor">
                                        @expense.CategoryName
                                    </span>
                                </td>
                                <td>$@expense.Amount.ToString("N2")</td>
                            </tr>
                        }
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>

@section Scripts {
    <script>
        // Chart.js configuration
        const ctx = document.getElementById('categoryChart').getContext('2d');
        const categoryData = @Html.Raw(Json.Serialize(Model.ExpensesByCategory));

        const chart = new Chart(ctx, {
            type: 'pie',
            data: {
                labels: Object.keys(categoryData),
                datasets: [{
                    data: Object.values(categoryData),
                    backgroundColor: [
                        '#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF',
                        '#FF9F40', '#FF6384', '#C9CBCF'
                    ]
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'bottom'
                    },
                    title: {
                        display: true,
                        text: 'Spending by Category'
                    }
                }
            }
        });
    </script>
}
```

---

## 📝 Step 3: Create Expense Management Pages (15 minutes)

### 📝 Expenses List Page

**Copilot Prompt:**

```text
@workspace "Create Razor Page for expense list Pages/Expenses/Index.cshtml and Index.cshtml.cs:
- Load all expenses async
- Display in Bootstrap table
- Add 'Create New' button
- Include Edit and Delete buttons for each expense
- Show category badge with color
- Format amounts and dates
- Add search/filter functionality with JavaScript"
```

### ✏️ Create/Edit Expense Form

**Copilot Prompt:**

```text
@workspace "Create Razor Page for creating expense Pages/Expenses/Create.cshtml and Create.cshtml.cs:
- Form with asp-for Tag Helpers
- Amount, Description, ExpenseDate, CategoryId fields
- Category dropdown populated from database
- Bootstrap form styling
- Client-side validation with asp-validation-for
- OnPostAsync handler to create expense
- Redirect to Index on success
- Display validation errors"
```

**Example Form** (`Pages/Expenses/Create.cshtml`):

```cshtml
@page
@model CreateModel
@{
    ViewData["Title"] = "Create Expense";
}

<div class="row">
    <div class="col-md-6 offset-md-3">
        <div class="card">
            <div class="card-header">
                <h4><i class="fas fa-plus-circle"></i> Create New Expense</h4>
            </div>
            <div class="card-body">
                <form method="post">
                    <div class="mb-3">
                        <label asp-for="Input.Amount" class="form-label"></label>
                        <div class="input-group">
                            <span class="input-group-text">$</span>
                            <input asp-for="Input.Amount" class="form-control" />
                        </div>
                        <span asp-validation-for="Input.Amount" class="text-danger"></span>
                    </div>

                    <div class="mb-3">
                        <label asp-for="Input.Description" class="form-label"></label>
                        <input asp-for="Input.Description" class="form-control" />
                        <span asp-validation-for="Input.Description" class="text-danger"></span>
                    </div>

                    <div class="mb-3">
                        <label asp-for="Input.ExpenseDate" class="form-label"></label>
                        <input asp-for="Input.ExpenseDate" type="date" class="form-control" />
                        <span asp-validation-for="Input.ExpenseDate" class="text-danger"></span>
                    </div>

                    <div class="mb-3">
                        <label asp-for="Input.CategoryId" class="form-label"></label>
                        <select asp-for="Input.CategoryId" asp-items="Model.Categories" class="form-select">
                            <option value="">-- Select Category --</option>
                        </select>
                        <span asp-validation-for="Input.CategoryId" class="text-danger"></span>
                    </div>

                    <div class="d-grid gap-2">
                        <button type="submit" class="btn btn-primary">
                            <i class="fas fa-save"></i> Create Expense
                        </button>
                        <a asp-page="./Index" class="btn btn-outline-secondary">
                            <i class="fas fa-times"></i> Cancel
                        </a>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>

@section Scripts {
    <partial name="_ValidationScriptsPartial" />
}
```

---

## 📝 Step 4: Add Client-Side Interactivity (5 minutes)

### 💡 JavaScript Enhancements

**Copilot Prompt:**

```text
@workspace "Create wwwroot/js/expenses.js with:
- Real-time search/filter for expenses table
- Confirm delete with SweetAlert or Bootstrap modal
- Auto-format currency inputs
- Date picker enhancements
- Form validation feedback"
```

---

## ✅ Session Verification (5 minutes)

### 🧪 UI Testing Checklist

- [ ] Dashboard displays correctly with charts
- [ ] Expenses list shows all expenses
- [ ] Create form validates and saves
- [ ] Edit form loads data and updates
- [ ] Delete confirmation works
- [ ] Responsive design works on mobile
- [ ] JavaScript enhancements functional

---

## 🎉 Day 1 Complete! 🎊

### ✅ What You've Built Today

**Backend:**
- ✅ EF Core entities with proper relationships
- ✅ DbContext with Fluent API and migrations
- ✅ Service layer with business logic
- ✅ FluentValidation rules
- ✅ Comprehensive unit tests (15+)

**Frontend:**
- ✅ REST API endpoints (Controllers/Minimal APIs)
- ✅ Swagger/OpenAPI documentation
- ✅ Razor Pages with Bootstrap UI
- ✅ Interactive dashboard with Chart.js
- ✅ CRUD operations for expenses
- ✅ Responsive, professional design

### 📚 Copilot Skills Mastered

- ✅ Interface basics and inline completions
- ✅ Context selection (`#selection`, `#editor`, `#file`)
- ✅ Model switching and comparison
- ✅ Agent usage (`@workspace`, `@terminal`, `@git`)
- ✅ Pattern-based code generation
- ✅ Test generation with realistic data
- ✅ Multi-language coordination (C#/Razor/JS)
- ✅ Chat Interface mastery
- ✅ Professional AI workflows

### 🚀 Next Steps

**Optional Enhancements:**
- Add authentication with ASP.NET Core Identity
- Implement export to CSV/Excel
- Add expense reports and analytics
- Create expense categories management
- Add file upload for receipts
- Implement budget tracking
- Add monthly/yearly comparisons

### 📖 Continue Learning

- Explore [Day 2 materials](../../day2/) for advanced context mastery
- Practice with [Copilot Custom Instructions](../../day2/Copilot-Custom-Instructions.md)
- Review [Copilot Chat Cookbook](../../day1/Copilot-Chat-Cookbook.md)

---

## 🎓 Congratulations!

You've successfully built a complete ASP.NET Core expense tracker application using GitHub Copilot! You've mastered AI-assisted development from database design through to a polished web interface.

**Keep practicing and exploring - you're now a GitHub Copilot power user!** 🚀

**Happy Coding!** 💻✨
