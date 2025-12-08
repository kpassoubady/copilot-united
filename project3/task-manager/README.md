# Task Manager - ASP.NET Core 10.0

A full-stack task management application built with ASP.NET Core 10.0 and Entity Framework Core 9.0, designed for GitHub Copilot training.

## Overview

This project serves as a hands-on exercise for learning AI-assisted .NET development with GitHub Copilot. Build a complete task manager application while mastering Copilot skills.

## Quick Start

```bash
# Navigate to project
cd project3/task-manager

# Restore dependencies
dotnet restore

# Build the project
dotnet build

# Create initial database migration
dotnet ef migrations add InitialCreate --project src/TaskManager.Web

# Apply migrations
dotnet ef database update --project src/TaskManager.Web

# Run the application
dotnet run --project src/TaskManager.Web
```

Open your browser to:
- **Application**: http://localhost:5000 or https://localhost:5001
- **Swagger UI**: https://localhost:5001/swagger
- **Health Check**: http://localhost:5000/health

## Project Structure

```
task-manager/
├── TaskManager.sln                    # Solution file
├── src/
│   └── TaskManager.Web/
│       ├── Models/                    # EF Core entities
│       │   ├── TaskItem.cs
│       │   └── Category.cs
│       ├── Data/                      # DbContext
│       │   └── TaskManagerContext.cs
│       ├── Services/                  # Business logic interfaces
│       │   ├── ITaskService.cs
│       │   └── ICategoryService.cs
│       ├── DTOs/                      # Data Transfer Objects
│       │   ├── TaskDtos.cs
│       │   └── CategoryDtos.cs
│       ├── Validators/                # FluentValidation
│       │   ├── TaskValidators.cs
│       │   └── CategoryValidators.cs
│       ├── Pages/                     # Razor Pages
│       │   ├── Index.cshtml
│       │   ├── Shared/
│       │   │   └── _Layout.cshtml
│       │   └── ...
│       ├── wwwroot/                   # Static files
│       │   ├── css/
│       │   └── js/
│       ├── Program.cs                 # Application entry point
│       └── appsettings.json           # Configuration
└── tests/                             # Test projects (to be created)
```

## Technology Stack

- **Framework**: ASP.NET Core 10.0
- **ORM**: Entity Framework Core 9.0
- **Database**: SQLite (development)
- **Frontend**: Razor Pages + Bootstrap 5.3
- **Validation**: FluentValidation
- **API Documentation**: Swagger/OpenAPI

## Features

### Core Functionality
- Create, read, update, delete tasks
- Organize tasks by categories
- Set task priorities (Low, Medium, High, Critical)
- Track task status (Todo, In Progress, Done, Cancelled)
- Due date management with overdue detection

### Technical Features
- RESTful API endpoints
- Fluent API database configuration
- Automatic timestamp tracking
- Input validation
- Swagger documentation
- Responsive UI with Bootstrap

## GitHub Copilot Learning Objectives

This project is designed to teach:

1. **Code Generation**: Generate entities, services, and controllers
2. **Pattern Recognition**: Implement common .NET patterns
3. **Context Selection**: Use `#selection` and `#editor` for targeted assistance
4. **Model Comparison**: Compare outputs from different AI models
5. **Test Generation**: Create unit tests with xUnit

## Development Commands

```bash
# Build
dotnet build

# Run with hot reload
dotnet watch run --project src/TaskManager.Web

# Run tests
dotnet test

# Add migration
dotnet ef migrations add <MigrationName> --project src/TaskManager.Web

# Update database
dotnet ef database update --project src/TaskManager.Web

# Remove last migration
dotnet ef migrations remove --project src/TaskManager.Web
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/tasks | Get all tasks |
| GET | /api/tasks/{id} | Get task by ID |
| POST | /api/tasks | Create new task |
| PUT | /api/tasks/{id} | Update task |
| DELETE | /api/tasks/{id} | Delete task |
| GET | /api/categories | Get all categories |
| GET | /api/categories/{id} | Get category by ID |
| POST | /api/categories | Create new category |

## Prerequisites

- .NET 9+ SDK
- Entity Framework Core CLI tools
- VS Code with C# Dev Kit or Visual Studio 2022
- GitHub Copilot extension

## Installation Guide

See the installation guides for detailed setup instructions:
- [macOS Installation](../install/proj3-install-mac.md)
- [Windows Installation](../install/proj3-install-win.md)

## Next Steps

After setup, follow the breakout session exercises:

1. **Session 1**: Models & DbContext - Build the data layer
2. **Session 2**: Services & Business Logic - Implement service layer
3. **Session 3**: REST APIs & Controllers - Create API endpoints
4. **Session 4**: Web Interface - Build Razor Pages UI

## License

Part of the GitHub Copilot United training materials.
