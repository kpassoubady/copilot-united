# 🏗️ Day 1 Setup: Backend & Service Layer Prerequisites

## 🎯 Setup Overview

This setup ensures you have everything needed to successfully complete Day 1 of the Personal Expense Tracker .NET project. You'll verify .NET SDK, Entity Framework tools, IDE setup, and create the initial project structure.

**⏱️ Estimated Setup Time: 10-15 minutes**

---

## ✅ Prerequisites Checklist

### 📋 Required Software

**.NET SDK**

```bash
# Check .NET version (should be 8.0 or higher)
dotnet --version

# Expected output should show version 8.0.x or higher
# If not installed, download from: https://dotnet.microsoft.com/download
```

**Entity Framework Core Tools**

```bash
# Check EF Core tools version
dotnet ef --version

# If not installed:
dotnet tool install --global dotnet-ef

# Update if already installed:
dotnet tool update --global dotnet-ef
```

**IDE and Extensions**

- VS Code or Visual Studio 2022 installed
- GitHub Copilot extension enabled and authenticated
- C# Dev Kit (for VS Code) or C# extension
- .NET Extension Pack (for VS Code - optional but recommended)

---

## 🚀 Project Structure Setup

### 📁 Create Project Directory

```bash
# Navigate to your workspace
cd /path/to/your/workspace

# Create solution and project
dotnet new sln -n ExpenseTracker
dotnet new webapp -n ExpenseTracker.Web -o src/ExpenseTracker.Web
dotnet sln add src/ExpenseTracker.Web

# Navigate into project
cd src/ExpenseTracker.Web
```

### 🔧 Verify GitHub Copilot

Test Copilot functionality:

1. Open VS Code in the solution directory: `code .` (from root, not src/)
2. Create a new file: `Test.cs`
3. Type: `// Create a simple record for Expense with Id, Description, Amount, Date`
4. Press `Tab` to accept Copilot suggestion
5. Verify Copilot generates appropriate C# code

---

## 📦 NuGet Package Installation

### 🎯 Add Required Packages

```bash
# Navigate to project directory (if not already there)
cd src/ExpenseTracker.Web

# Entity Framework Core with SQLite
dotnet add package Microsoft.EntityFrameworkCore.Sqlite --version 8.0.0
dotnet add package Microsoft.EntityFrameworkCore.Design --version 8.0.0
dotnet add package Microsoft.EntityFrameworkCore.Tools --version 8.0.0

# Validation
dotnet add package FluentValidation.AspNetCore --version 11.3.0

# OpenAPI/Swagger (usually included in webapp template)
dotnet add package Swashbuckle.AspNetCore --version 6.5.0

# Optional: SQL Server support (for production)
# dotnet add package Microsoft.EntityFrameworkCore.SqlServer --version 8.0.0
```

### 📋 Verify Packages Installed

```bash
# List all packages
dotnet list package

# You should see:
# - Microsoft.EntityFrameworkCore.Sqlite
# - Microsoft.EntityFrameworkCore.Design
# - Microsoft.EntityFrameworkCore.Tools
# - FluentValidation.AspNetCore
# - Swashbuckle.AspNetCore
```

---

## 🗄️ Database Setup

### 💾 SQLite Database Configuration

Update `appsettings.json`:

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
  },
  "AllowedHosts": "*"
}
```

### 🔒 Add Database to .gitignore

Create or update `.gitignore` in project root:

```gitignore
# Database files
*.db
*.db-shm
*.db-wal

# User-specific files
*.user
*.suo
*.userosscache

# Build results
bin/
obj/
[Dd]ebug/
[Rr]elease/

# VS Code
.vscode/
!.vscode/tasks.json
!.vscode/launch.json

# Rider
.idea/
```

---

## 📁 Project Structure Setup

### 🗂️ Create Directory Structure

```bash
# From src/ExpenseTracker.Web directory
mkdir Models
mkdir Data
mkdir Services
mkdir Validators
mkdir DTOs
```

### 📂 Expected Structure

```text
ExpenseTracker/                  # Solution root
├── ExpenseTracker.sln
├── src/
│   └── ExpenseTracker.Web/
│       ├── Models/              # EF Core entities
│       ├── Data/                # DbContext
│       ├── Services/            # Business logic
│       ├── Validators/          # FluentValidation
│       ├── DTOs/                # Data Transfer Objects
│       ├── Pages/               # Razor Pages
│       ├── wwwroot/            # Static files
│       ├── Program.cs
│       ├── appsettings.json
│       └── ExpenseTracker.Web.csproj
└── tests/                       # Will be created later
```

---

## ✅ Setup Verification

### 🧪 Test Basic Setup

Create a simple health check endpoint in `Program.cs`:

```csharp
// Add this before app.Run();
app.MapGet("/health", () => Results.Ok(new { 
    Status = "Healthy", 
    Timestamp = DateTime.UtcNow 
}))
.WithName("HealthCheck")
.WithOpenApi();
```

### 🚀 Run Verification

```bash
# Build the project
dotnet build

# Run the application
dotnet run

# Expected output:
# info: Microsoft.Hosting.Lifetime[14]
#       Now listening on: http://localhost:5000
# info: Microsoft.Hosting.Lifetime[14]
#       Now listening on: https://localhost:5001

# In another terminal, test the health endpoint:
curl http://localhost:5000/health

# Expected response:
# {"status":"Healthy","timestamp":"2025-12-07T..."}
```

---

## 🔧 IDE Configuration

### 📝 VS Code Settings

Create `.vscode/settings.json` for optimal C# development:

```json
{
    "dotnet.defaultSolution": "ExpenseTracker.sln",
    "omnisharp.enableRoslynAnalyzers": true,
    "omnisharp.enableEditorConfigSupport": true,
    "omnisharp.organizeImportsOnFormat": true,
    "[csharp]": {
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.organizeImports": "explicit"
        }
    }
}
```

### 🎨 GitHub Copilot Settings

Recommended Copilot settings for C# development:

```json
{
    "github.copilot.enable": {
        "*": true,
        "yaml": false,
        "plaintext": false
    },
    "github.copilot.advanced": {
        "length": 500,
        "temperature": 0.1
    }
}
```

### 🚀 VS Code Tasks (Optional)

Create `.vscode/tasks.json`:

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "build",
            "command": "dotnet",
            "type": "process",
            "args": [
                "build",
                "${workspaceFolder}/ExpenseTracker.sln"
            ],
            "problemMatcher": "$msCompile"
        },
        {
            "label": "run",
            "command": "dotnet",
            "type": "process",
            "args": [
                "run",
                "--project",
                "${workspaceFolder}/src/ExpenseTracker.Web"
            ],
            "problemMatcher": "$msCompile"
        }
    ]
}
```

---

## 📚 Development Tools

### 🔍 Useful Commands

```bash
# Build solution
dotnet build

# Run application with hot reload
dotnet watch run

# Run specific project
dotnet run --project src/ExpenseTracker.Web

# Clean build artifacts
dotnet clean

# Restore NuGet packages
dotnet restore

# Run tests (after creating test project)
dotnet test

# Create EF Core migration
dotnet ef migrations add InitialCreate --project src/ExpenseTracker.Web

# Update database
dotnet ef database update --project src/ExpenseTracker.Web
```

### 🌐 Access Points (after app starts)

- **Application**: <http://localhost:5000> or <https://localhost:5001>
- **Swagger UI**: <https://localhost:5001/swagger>
- **Health Check**: <http://localhost:5000/health>

---

## 🚨 Troubleshooting

### Common Issues and Solutions

**NuGet Packages Not Restoring**

```bash
# Clear NuGet cache
dotnet nuget locals all --clear

# Restore packages
dotnet restore
```

**.NET SDK Version Issues**

```bash
# List installed SDKs
dotnet --list-sdks

# Install .NET 8 SDK if missing:
# Download from https://dotnet.microsoft.com/download/dotnet/8.0
```

**EF Core Tools Not Found**

```bash
# Install or update globally
dotnet tool install --global dotnet-ef

# Verify installation
dotnet ef --version
```

**Port Already in Use**

```bash
# Change port in Properties/launchSettings.json
# Or kill process using port:
# macOS/Linux: lsof -ti:5000 | xargs kill
# Windows: netstat -ano | findstr :5000
```

**IDE Not Recognizing C#**

- Restart VS Code
- Run: `.NET: Restart Language Server` from Command Palette (Cmd+Shift+P)
- Verify C# Dev Kit extension is installed and enabled
- Check that OmniSharp server is running (bottom status bar)

**GitHub Copilot Not Working**

- Check authentication: `GitHub Copilot: Sign In` in Command Palette
- Verify subscription status: `GitHub Copilot: Check Status`
- Restart VS Code
- Check Copilot output panel for errors

---

## ✅ Ready for Day 1

### 🎯 Success Checklist

- [ ] .NET 8 SDK installed and verified
- [ ] Entity Framework Core tools installed
- [ ] IDE configured with C# and Copilot extensions
- [ ] Solution and project structure created
- [ ] NuGet packages installed successfully
- [ ] Application builds without errors
- [ ] Application runs and health endpoint responds
- [ ] GitHub Copilot generating suggestions

### 🚀 Next Steps

You're now ready to start **Day 1 - Session 1: Models & DbContext**!

The setup process should have taken about 10-15 minutes. If you encountered any issues, please resolve them before starting the main exercise.

**Time to build something amazing with GitHub Copilot! 🎉**

---

## 📖 Additional Resources

- [.NET CLI Documentation](https://docs.microsoft.com/dotnet/core/tools/)
- [Entity Framework Core Getting Started](https://docs.microsoft.com/ef/core/get-started/)
- [ASP.NET Core Documentation](https://docs.microsoft.com/aspnet/core)
- [VS Code C# Extension](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csharp)
