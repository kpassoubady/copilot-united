# 🏗️ Day 1 - Session 1: Personal Expense Tracker - Models & DbContext (45 mins)

## 🎯 Learning Objectives

By the end of this session, you will:

- Create ASP.NET Core project structure with EF Core entities
- Implement DbContext with Fluent API configuration
- Set up SQLite database and migrations
- Master GitHub Copilot interface and context selection
- Verify entities and database work correctly

**⏱️ Time Allocation: 45 minutes (includes Copilot mastery)**

## 🤖 GitHub Copilot Focus: Basic Interface & Code Generation

**Today's Copilot Skills:**

- Interface basics (inline completions, chat, command palette)
- Context selection with `#selection`, `#editor`
- Model selection and basic prompting
- Code generation for entities and DbContext

📚 **Reference**: [Copilot Mastery Guide](../0-copilot-mastery-guide.md) for advanced techniques

---

## 📋 Prerequisites Check (2 minutes)

- ✅ .NET 8 SDK installed
- ✅ Entity Framework Core tools installed
- ✅ IDE setup (VS Code or Visual Studio)
- ✅ GitHub Copilot enabled and authenticated

**Quick Test**: Verify setup by running:

```bash
dotnet --version
dotnet ef --version
```

---

## 🚀 Session Overview

In this first session, you'll build the foundation data layer of the expense tracker. We'll focus on creating solid Entity Framework Core entities and DbContext without rushing into complex business logic.

### 🎯 What You'll Build (45 minutes)

- **EF Core Entities**: Category and Expense with relationships
- **DbContext Layer**: Fluent API configuration and database setup
- **Database Migrations**: Initial database schema
- **Basic Validation**: Essential entity validation with Data Annotations

---

## 📝 Step 1: Project Setup & Configuration (8 minutes)

### 🔧 Verify Current Project Structure

First, let's examine what we have:

```bash
# Navigate to project directory
cd ExpenseTracker/src/ExpenseTracker.Web

# Check current structure
ls -la
```

### 📄 Verify appsettings.json

Ensure `appsettings.json` contains database configuration:

```json
{
  "ConnectionStrings": {
    "DefaultConnection": "Data Source=expensetracker.db"
  },
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning",
      "Microsoft.EntityFrameworkCore.Database.Command": "Information"
    }
  }
}
```

**GitHub Copilot Prompt:**

```text
@workspace Check appsettings.json configuration for SQLite and suggest any missing EF Core settings for development
```

**🤖 Copilot Practice**: Try switching models and compare responses:

```text
# In Copilot Chat, try:
/model gpt-4-turbo
"What database configuration is missing for development?"

/model claude-3.5-sonnet  
"Review this SQLite setup and suggest improvements"
```

---

## 📝 Step 1.5: Create Specialized Development Assistant (5 minutes)

### 🤖 GitHub Copilot Agent Setup

Create a specialized .NET/EF Core assistant:

**Create `.github/agents/dotnet-expert.agent.md`:**

```text
/generate Create specialized GitHub Copilot agent for .NET development:

Filepath: .github/agents/dotnet-expert.agent.md

Include YAML frontmatter with:
- description: 'ASP.NET Core & EF Core development specialist for expense tracker'
- tools: []

Specialized behavior for:
- Project Context: ASP.NET Core 8.0, C# 12, Entity Framework Core 8.0
- Database: SQLite (dev), SQL Server (prod optional)
- Project structure: Models, Data, Services, DTOs, Validators

Expertise areas:
- Entity design with proper EF Core conventions
- DbContext configuration with Fluent API
- Repository pattern and service layer
- FluentValidation rules
- REST API best practices
- Razor Pages development

Make responses project-specific and actionable
```

**Test Your .NET Expert:**

```text
@workspace /agents dotnet-expert

"Help me design the Category entity with proper EF Core attributes and relationships."
```

---

## 📝 Step 2: Create Category Entity (10 minutes)

### 🏷️ Category Entity Implementation

**Copilot Prompt:**

```text
/generate Create an Entity Framework Core Category entity in Models/Category.cs with:
- Guid Id (primary key, generated value)
- string Name (required, max 100 characters, unique)
- string? Description (optional, max 255 characters)
- string? Icon (max 50 characters for FontAwesome icons like "fas fa-utensils")
- string? Color (7 characters for hex color codes like "#FF5733", default "#6c757d")
- DateTime CreatedAt (automatic, defaults to UtcNow)
- DateTime UpdatedAt (automatic, updated on changes)
- Navigation property: ICollection<Expense> Expenses (one-to-many)
- Include Data Annotations for validation
- Add constructors (default and parameterized)
```

**Expected file location**: `src/ExpenseTracker.Web/Models/Category.cs`

**Example Output**:

```csharp
using System.ComponentModel.DataAnnotations;

namespace ExpenseTracker.Web.Models;

public class Category
{
    [Key]
    public Guid Id { get; set; } = Guid.NewGuid();

    [Required]
    [MaxLength(100)]
    public string Name { get; set; } = string.Empty;

    [MaxLength(255)]
    public string? Description { get; set; }

    [MaxLength(50)]
    public string? Icon { get; set; }

    [MaxLength(7)]
    [RegularExpression(@"^#[0-9A-Fa-f]{6}$")]
    public string? Color { get; set; } = "#6c757d";

    public DateTime CreatedAt { get; set; } = DateTime.UtcNow;
    public DateTime UpdatedAt { get; set; } = DateTime.UtcNow;

    // Navigation property
    public ICollection<Expense> Expenses { get; set; } = new List<Expense>();

    public Category()
    {
    }

    public Category(string name, string? description = null, string? icon = null, string? color = null)
    {
        Name = name;
        Description = description;
        Icon = icon;
        Color = color ?? "#6c757d";
    }
}
```

### 🤖 Advanced Copilot Practice

1. **Context Selection**: Select the entire entity class, then ask:
```text
"Analyze #selection and suggest improvements for EF Core best practices"
```

2. **Model Comparison**:
```text
/model gpt-4-turbo
"Review #selection for performance optimizations"
```

### ✅ Verification Point

- Ensure the entity compiles without errors
- Check that Data Annotations are correct
- Verify navigation property is in place

---

## 📝 Step 3: Create Expense Entity (10 minutes)

### 💰 Expense Entity Implementation

**Copilot Prompt:**

```text
/generate Create an Entity Framework Core Expense entity in Models/Expense.cs with:
- Guid Id (primary key, generated value)
- decimal Amount (required, precision 18, scale 2, positive values only)
- string Description (required, max 255 characters)
- DateTime ExpenseDate (required, defaults to today)
- Guid CategoryId (foreign key)
- Category Category (navigation property, required)
- DateTime CreatedAt, UpdatedAt (automatic audit fields)
- Include Data Annotations for validation
- Add constructors and computed property for CategoryName
```

**Expected file location**: `src/ExpenseTracker.Web/Models/Expense.cs`

**Example Output**:

```csharp
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace ExpenseTracker.Web.Models;

public class Expense
{
    [Key]
    public Guid Id { get; set; } = Guid.NewGuid();

    [Required]
    [Column(TypeName = "decimal(18,2)")]
    [Range(0.01, double.MaxValue, ErrorMessage = "Amount must be greater than 0")]
    public decimal Amount { get; set; }

    [Required]
    [MaxLength(255)]
    public string Description { get; set; } = string.Empty;

    [Required]
    public DateTime ExpenseDate { get; set; } = DateTime.Today;

    [Required]
    public Guid CategoryId { get; set; }

    // Navigation property
    [Required]
    public Category Category { get; set; } = null!;

    public DateTime CreatedAt { get; set; } = DateTime.UtcNow;
    public DateTime UpdatedAt { get; set; } = DateTime.UtcNow;

    // Computed property
    [NotMapped]
    public string CategoryName => Category?.Name ?? "Unknown";

    public Expense()
    {
    }

    public Expense(decimal amount, string description, DateTime expenseDate, Guid categoryId)
    {
        Amount = amount;
        Description = description;
        ExpenseDate = expenseDate;
        CategoryId = categoryId;
    }
}
```

---

## 📝 Step 4: Create DbContext (10 minutes)

### 🗄️ ExpenseTrackerContext Implementation

**Copilot Prompt:**

```text
/generate Create Entity Framework Core DbContext in Data/ExpenseTrackerContext.cs with:
- DbSet<Category> Categories
- DbSet<Expense> Expenses
- OnModelCreating with Fluent API configurations:
  * Category.Name unique index
  * Expense-Category relationship with cascade delete
  * Automatic CreatedAt/UpdatedAt timestamps via SaveChanges override
  * Default values for Category.Color
- Include seed data method with 5 sample categories
```

**Expected file location**: `src/ExpenseTracker.Web/Data/ExpenseTrackerContext.cs`

**Example Output**:

```csharp
using Microsoft.EntityFrameworkCore;
using ExpenseTracker.Web.Models;

namespace ExpenseTracker.Web.Data;

public class ExpenseTrackerContext : DbContext
{
    public ExpenseTrackerContext(DbContextOptions<ExpenseTrackerContext> options)
        : base(options)
    {
    }

    public DbSet<Category> Categories => Set<Category>();
    public DbSet<Expense> Expenses => Set<Expense>();

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        base.OnModelCreating(modelBuilder);

        // Category configuration
        modelBuilder.Entity<Category>(entity =>
        {
            entity.HasIndex(c => c.Name).IsUnique();
            entity.Property(c => c.Color).HasDefaultValue("#6c757d");
        });

        // Expense configuration
        modelBuilder.Entity<Expense>(entity =>
        {
            entity.HasOne(e => e.Category)
                  .WithMany(c => c.Expenses)
                  .HasForeignKey(e => e.CategoryId)
                  .OnDelete(DeleteBehavior.Cascade);

            entity.Property(e => e.Amount).HasColumnType("decimal(18,2)");
        });

        // Seed data
        SeedData(modelBuilder);
    }

    private void SeedData(ModelBuilder modelBuilder)
    {
        var categories = new[]
        {
            new Category { Id = Guid.NewGuid(), Name = "Food & Dining", Icon = "fas fa-utensils", Color = "#FF6384" },
            new Category { Id = Guid.NewGuid(), Name = "Transportation", Icon = "fas fa-car", Color = "#36A2EB" },
            new Category { Id = Guid.NewGuid(), Name = "Entertainment", Icon = "fas fa-film", Color = "#FFCE56" },
            new Category { Id = Guid.NewGuid(), Name = "Shopping", Icon = "fas fa-shopping-cart", Color = "#4BC0C0" },
            new Category { Id = Guid.NewGuid(), Name = "Healthcare", Icon = "fas fa-heartbeat", Color = "#9966FF" }
        };

        modelBuilder.Entity<Category>().HasData(categories);
    }

    public override int SaveChanges()
    {
        UpdateTimestamps();
        return base.SaveChanges();
    }

    public override Task<int> SaveChangesAsync(CancellationToken cancellationToken = default)
    {
        UpdateTimestamps();
        return base.SaveChangesAsync(cancellationToken);
    }

    private void UpdateTimestamps()
    {
        var entries = ChangeTracker.Entries()
            .Where(e => e.State == EntityState.Added || e.State == EntityState.Modified);

        foreach (var entry in entries)
        {
            if (entry.State == EntityState.Added)
            {
                entry.Property("CreatedAt").CurrentValue = DateTime.UtcNow;
            }
            entry.Property("UpdatedAt").CurrentValue = DateTime.UtcNow;
        }
    }
}
```

---

## 📝 Step 5: Configure Services & Create Migration (5 minutes)

### ⚙️ Update Program.cs

**Copilot Prompt:**

```text
/generate Add DbContext configuration to Program.cs:
- Register ExpenseTrackerContext with dependency injection
- Use SQLite connection string from appsettings.json
- Enable sensitive data logging in development
```

Add to `Program.cs`:

```csharp
using Microsoft.EntityFrameworkCore;
using ExpenseTracker.Web.Data;

var builder = WebApplication.CreateBuilder(args);

// Add DbContext
builder.Services.AddDbContext<ExpenseTrackerContext>(options =>
{
    options.UseSqlite(builder.Configuration.GetConnectionString("DefaultConnection"));
    if (builder.Environment.IsDevelopment())
    {
        options.EnableSensitiveDataLogging();
        options.EnableDetailedErrors();
    }
});

// Rest of configuration...
```

### 🗄️ Create Initial Migration

```bash
# Create initial migration
dotnet ef migrations add InitialCreate --project src/ExpenseTracker.Web

# Apply migration to database
dotnet ef database update --project src/ExpenseTracker.Web

# Verify database created
ls -la *.db
```

---

## ✅ Session Verification (5 minutes)

### 🧪 Test Database Setup

Create `Pages/DbTest.cshtml.cs`:

```csharp
using Microsoft.AspNetCore.Mvc.RazorPages;
using ExpenseTracker.Web.Data;
using Microsoft.EntityFrameworkCore;

namespace ExpenseTracker.Web.Pages;

public class DbTestModel : PageModel
{
    private readonly ExpenseTrackerContext _context;

    public DbTestModel(ExpenseTrackerContext context)
    {
        _context = context;
    }

    public int CategoryCount { get; set; }
    public int ExpenseCount { get; set; }

    public async Task OnGetAsync()
    {
        CategoryCount = await _context.Categories.CountAsync();
        ExpenseCount = await _context.Expenses.CountAsync();
    }
}
```

### 🚀 Run and Verify

```bash
# Run application
dotnet run

# Open browser: https://localhost:5001/DbTest
# You should see: Categories: 5, Expenses: 0
```

---

## 🎉 Session Complete!

### ✅ What You've Built

- ✅ Category and Expense entities with proper EF Core configuration
- ✅ ExpenseTrackerContext with Fluent API and seed data
- ✅ SQLite database with migrations
- ✅ Automatic timestamp tracking
- ✅ Verified database connectivity

### 📚 Copilot Skills Learned

- ✅ Context selection (`#selection`, `#editor`)
- ✅ Model switching for comparison
- ✅ Agent creation for specialized assistance
- ✅ Code generation for entities and DbContext

### 🚀 Next Session

**Session 2: Services & Business Logic** - Build the service layer with business logic, FluentValidation, and unit tests!

**Great work! Take a 5-minute break before continuing.** ☕
