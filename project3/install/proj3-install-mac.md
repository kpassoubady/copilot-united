# Project 3: ASP.NET Core Task Manager Installation Guide (macOS)

<!-- markdownlint-disable MD033 MD029 MD010-->
<!-- vscode-markdown-toc -->
- [Project 3: ASP.NET Core Task Manager Installation Guide (macOS)](#project-3-aspnet-core-task-manager-installation-guide-macos)
  - [1. Step 1: Install .NET SDK](#1-step-1-install-net-sdk)
    - [1.1. Verify Installation](#11-verify-installation)
  - [2. Step 2: Install Entity Framework Core Tools](#2-step-2-install-entity-framework-core-tools)
  - [3. Step 3: Install Git](#3-step-3-install-git)
  - [4. Project Setup](#4-project-setup)
    - [4.1. Quick Start (Recommended)](#41-quick-start-recommended)
    - [4.2. Create ASP.NET Core Project from Scratch](#42-create-aspnet-core-project-from-scratch)
    - [4.3. Install NuGet Packages](#43-install-nuget-packages)
    - [4.4. Test Project Setup](#44-test-project-setup)
  - [5. IDE Setup](#5-ide-setup)
    - [5.1. Visual Studio Code Extensions](#51-visual-studio-code-extensions)
    - [5.2. Visual Studio for Mac (Alternative)](#52-visual-studio-for-mac-alternative)
  - [6. Database Setup](#6-database-setup)
    - [6.1. SQLite Database (Default)](#61-sqlite-database-default)
    - [6.2. SQL Server (Optional)](#62-sql-server-optional)
  - [7. Verification](#7-verification)
  - [8. Troubleshooting](#8-troubleshooting)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

## 1. <a name='Step1:InstallNETSDK'></a>Step 1: Install .NET SDK

Install .NET 9+ SDK using Homebrew:

```bash
brew install --cask dotnet-sdk
```

Alternatively, download from [Microsoft .NET Downloads](https://dotnet.microsoft.com/download/dotnet/9.0).

### 1.1. <a name='VerifyInstallation'></a>Verify Installation

```bash
dotnet --version
# Expected: 9.0.x or higher

dotnet --list-sdks
# Should show .NET 9.0+ SDK installed
```

Add .NET tools to your PATH (if not already):

```bash
echo 'export PATH="$PATH:$HOME/.dotnet/tools"' >> ~/.zshrc
source ~/.zshrc
```

## 2. <a name='Step2:InstallEntityFrameworkCoreTools'></a>Step 2: Install Entity Framework Core Tools

Install EF Core CLI tools globally:

```bash
dotnet tool install --global dotnet-ef
```

If already installed, update to the latest version:

```bash
dotnet tool update --global dotnet-ef
```

Verify installation:

```bash
dotnet ef --version
# Expected: Entity Framework Core .NET Command-line Tools 9.x.x
```

## 3. <a name='Step3:InstallGit'></a>Step 3: Install Git

Install Git using Homebrew:

```bash
brew install git
```

Configure Git with your information:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Verify Git installation:

```bash
git --version
```

## 4. <a name='ProjectSetup'></a>Project Setup

### 4.1. <a name='QuickStartRecommended'></a>Quick Start (Recommended)

If you cloned this repo, use the provided project:

```bash
# Navigate to the project directory
cd project3/task-manager

# Restore dependencies
dotnet restore

# Build the project
dotnet build

# Create database migrations
dotnet ef migrations add InitialCreate --project src/TaskManager.Web
dotnet ef database update --project src/TaskManager.Web

# Run the application
dotnet run --project src/TaskManager.Web

# Open http://localhost:5000 or https://localhost:5001
```

### 4.2. <a name='CreateASPNETCoreProjectfromScratch'></a>Create ASP.NET Core Project from Scratch

Create the project directory and solution:

```bash
mkdir -p project3
cd project3

# Create solution and project
dotnet new sln -n TaskManager
dotnet new webapp -n TaskManager.Web -o src/TaskManager.Web
dotnet sln add src/TaskManager.Web

# Navigate to project
cd src/TaskManager.Web
```

### 4.3. <a name='InstallNuGetPackages'></a>Install NuGet Packages

```bash
# Entity Framework Core with SQLite
dotnet add package Microsoft.EntityFrameworkCore.Sqlite --version 9.0.0
dotnet add package Microsoft.EntityFrameworkCore.Design --version 9.0.0
dotnet add package Microsoft.EntityFrameworkCore.Tools --version 9.0.0

# Validation
dotnet add package FluentValidation.AspNetCore --version 11.3.0

# OpenAPI/Swagger
dotnet add package Swashbuckle.AspNetCore --version 6.5.0
```

Verify packages installed:

```bash
dotnet list package
```

### 4.4. <a name='TestProjectSetup'></a>Test Project Setup

Build and run the application:

```bash
# Build the project
dotnet build

# Run the application
dotnet run

# Application should start on:
# - HTTP:  http://localhost:5000
# - HTTPS: https://localhost:5001
```

Test the health endpoint (after adding it):

```bash
curl http://localhost:5000/health
# Expected: {"status":"Healthy","timestamp":"..."}
```

Stop the application with `Ctrl+C`.

## 5. <a name='IDESetup'></a>IDE Setup

### 5.1. <a name='VisualStudioCodeExtensions'></a>Visual Studio Code Extensions

Install recommended VS Code extensions:

```bash
# C# Dev Kit (includes C# extension and IntelliCode)
code --install-extension ms-dotnettools.csdevkit

# .NET Extension Pack
code --install-extension ms-dotnettools.vscode-dotnet-pack

# GitHub Copilot
code --install-extension github.copilot

# REST Client for API testing
code --install-extension humao.rest-client

# Thunder Client (alternative API testing)
code --install-extension rangav.vscode-thunder-client
```

Alternatively, install via VS Code marketplace:

1. **C# Dev Kit** - Comprehensive C# support
2. **GitHub Copilot** - AI-powered code completion
3. **REST Client** - API testing within VS Code
4. **NuGet Gallery** - Package management

### 5.2. <a name='VisualStudioforMacAlternative'></a>Visual Studio for Mac (Alternative)

If using Visual Studio for Mac:

1. Download from [Visual Studio for Mac](https://visualstudio.microsoft.com/vs/mac/)
2. Install with ASP.NET and web development workload
3. Install GitHub Copilot extension from Extensions Manager

## 6. <a name='DatabaseSetup'></a>Database Setup

### 6.1. <a name='SQLiteDatabaseDefault'></a>SQLite Database (Default)

SQLite is configured by default. No additional setup required.

Update `appsettings.json`:

```json
{
  "ConnectionStrings": {
    "DefaultConnection": "Data Source=taskmanager.db"
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

Add to `.gitignore`:

```gitignore
# Database files
*.db
*.db-shm
*.db-wal
```

### 6.2. <a name='SQLServerOptional'></a>SQL Server (Optional)

For SQL Server (using Docker):

```bash
# Pull SQL Server image
docker pull mcr.microsoft.com/mssql/server:2022-latest

# Run SQL Server container
docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=YourStrong@Password" \
  -p 1433:1433 --name sql-server -d mcr.microsoft.com/mssql/server:2022-latest
```

Update packages and connection string:

```bash
dotnet add package Microsoft.EntityFrameworkCore.SqlServer --version 9.0.0
```

```json
{
  "ConnectionStrings": {
    "DefaultConnection": "Server=localhost;Database=TaskManager;User Id=sa;Password=YourStrong@Password;TrustServerCertificate=True"
  }
}
```

## 7. <a name='Verification'></a>Verification

Run these commands to verify your setup:

```bash
# Check .NET SDK
dotnet --version && echo "✓ .NET SDK OK"

# Check EF Core tools
dotnet ef --version && echo "✓ EF Core Tools OK"

# Check Git
git --version && echo "✓ Git OK"

# Test project compilation
cd project3/task-manager
dotnet build && echo "✓ Build OK"

# Run application (Ctrl+C to stop)
dotnet run
```

Expected access points after starting:

- **Application**: http://localhost:5000 or https://localhost:5001
- **Swagger UI**: https://localhost:5001/swagger
- **Health Check**: http://localhost:5000/health

## 8. <a name='Troubleshooting'></a>Troubleshooting

### Common Issues and Solutions

**1. .NET SDK Not Found**

```bash
# Check installation
dotnet --list-sdks

# If missing, reinstall via Homebrew
brew reinstall --cask dotnet-sdk
```

**2. EF Core Tools Not Found**

```bash
# Ensure tools are in PATH
export PATH="$PATH:$HOME/.dotnet/tools"

# Reinstall tools
dotnet tool uninstall --global dotnet-ef
dotnet tool install --global dotnet-ef
```

**3. Port Already in Use**

```bash
# Find process using port 5000
lsof -ti:5000 | xargs kill -9

# Or change port in Properties/launchSettings.json
```

**4. NuGet Packages Not Restoring**

```bash
# Clear NuGet cache
dotnet nuget locals all --clear

# Restore packages
dotnet restore
```

**5. SSL Certificate Issues**

```bash
# Trust development certificate
dotnet dev-certs https --trust
```

**6. IDE Not Recognizing C#**

- Restart VS Code
- Run: `.NET: Restart Language Server` from Command Palette (Cmd+Shift+P)
- Verify C# Dev Kit extension is installed and enabled

### Technology Stack Summary

- **Framework**: ASP.NET Core 10.0
- **ORM**: Entity Framework Core 9.0
- **Database**: SQLite (development) / SQL Server (optional)
- **Frontend**: Razor Pages + Bootstrap 5.3
- **Validation**: FluentValidation
- **Testing**: xUnit, Moq, FluentAssertions
- **API Documentation**: Swagger/OpenAPI

### Next Steps

After completing setup:

1. Open the project in VS Code: `code project3/task-manager`
2. Verify GitHub Copilot is working
3. Start building the Task Manager application!
