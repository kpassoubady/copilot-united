# Project 3: ASP.NET Core Task Manager Installation Guide (Windows)

<!-- markdownlint-disable MD033 MD029 MD010-->
<!-- vscode-markdown-toc -->
- [Project 3: ASP.NET Core Task Manager Installation Guide (Windows)](#project-3-aspnet-core-task-manager-installation-guide-windows)
  - [1. Step 1: Install .NET SDK](#1-step-1-install-net-sdk)
    - [1.1. Option A: Using winget (Recommended)](#11-option-a-using-winget-recommended)
    - [1.2. Option B: Manual Download](#12-option-b-manual-download)
    - [1.3. Verify Installation](#13-verify-installation)
  - [2. Step 2: Install Entity Framework Core Tools](#2-step-2-install-entity-framework-core-tools)
  - [3. Step 3: Install Git](#3-step-3-install-git)
  - [4. Project Setup](#4-project-setup)
    - [4.1. Quick Start (Recommended)](#41-quick-start-recommended)
    - [4.2. Create ASP.NET Core Project from Scratch](#42-create-aspnet-core-project-from-scratch)
    - [4.3. Install NuGet Packages](#43-install-nuget-packages)
    - [4.4. Test Project Setup](#44-test-project-setup)
  - [5. IDE Setup](#5-ide-setup)
    - [5.1. Visual Studio Code Extensions](#51-visual-studio-code-extensions)
    - [5.2. Visual Studio 2022 (Alternative)](#52-visual-studio-2022-alternative)
  - [6. Database Setup](#6-database-setup)
    - [6.1. SQLite Database (Default)](#61-sqlite-database-default)
    - [6.2. SQL Server LocalDB (Optional)](#62-sql-server-localdb-optional)
  - [7. Verification](#7-verification)
  - [8. Troubleshooting](#8-troubleshooting)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

## 1. <a name='Step1:InstallNETSDK'></a>Step 1: Install .NET SDK

### 1.1. <a name='OptionA:Usingwinget'></a>Option A: Using winget (Recommended)

Open PowerShell as Administrator and run:

```powershell
winget install Microsoft.DotNet.SDK.9
```

### 1.2. <a name='OptionB:ManualDownload'></a>Option B: Manual Download

1. Visit [Microsoft .NET Downloads](https://dotnet.microsoft.com/download/dotnet/9.0)
2. Download the .NET 9.0 SDK installer for Windows
3. Run the installer and follow the prompts
4. Restart your terminal after installation

### 1.3. <a name='VerifyInstallation'></a>Verify Installation

Open a new PowerShell or Command Prompt window:

```powershell
dotnet --version
# Expected: 9.0.x or higher

dotnet --list-sdks
# Should show .NET 9.0+ SDK installed
```

## 2. <a name='Step2:InstallEntityFrameworkCoreTools'></a>Step 2: Install Entity Framework Core Tools

Install EF Core CLI tools globally:

```powershell
dotnet tool install --global dotnet-ef
```

If already installed, update to the latest version:

```powershell
dotnet tool update --global dotnet-ef
```

Verify installation:

```powershell
dotnet ef --version
# Expected: Entity Framework Core .NET Command-line Tools 9.x.x
```

If the command is not found, ensure the .NET tools path is in your PATH:

```powershell
# Add to user PATH (run in PowerShell)
$env:PATH += ";$env:USERPROFILE\.dotnet\tools"

# To make permanent, add to system environment variables
[Environment]::SetEnvironmentVariable("PATH", $env:PATH + ";$env:USERPROFILE\.dotnet\tools", "User")
```

## 3. <a name='Step3:InstallGit'></a>Step 3: Install Git

### Using winget

```powershell
winget install Git.Git
```

### Manual Download

1. Download from [Git for Windows](https://git-scm.com/download/win)
2. Run the installer with default options

### Configure Git

```powershell
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Verify Git installation:

```powershell
git --version
```

## 4. <a name='ProjectSetup'></a>Project Setup

### 4.1. <a name='QuickStartRecommended'></a>Quick Start (Recommended)

If you cloned this repo, use the provided project:

```powershell
# Navigate to the project directory
cd project3\task-manager

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

```powershell
mkdir project3
cd project3

# Create solution and project
dotnet new sln -n TaskManager
dotnet new webapp -n TaskManager.Web -o src\TaskManager.Web
dotnet sln add src\TaskManager.Web

# Navigate to project
cd src\TaskManager.Web
```

### 4.3. <a name='InstallNuGetPackages'></a>Install NuGet Packages

```powershell
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

```powershell
dotnet list package
```

### 4.4. <a name='TestProjectSetup'></a>Test Project Setup

Build and run the application:

```powershell
# Build the project
dotnet build

# Run the application
dotnet run --project src/TaskManager.Web

# Application should start on:
# - HTTP:  http://localhost:5000
# - HTTPS: https://localhost:5001
```

Test the health endpoint (after adding it):

```powershell
Invoke-RestMethod http://localhost:5000/health
# Expected: status: Healthy, timestamp: ...
```

Stop the application with `Ctrl+C`.

## 5. <a name='IDESetup'></a>IDE Setup

### 5.1. <a name='VisualStudioCodeExtensions'></a>Visual Studio Code Extensions

Install VS Code first:

```powershell
winget install Microsoft.VisualStudioCode
```

Then install extensions:

```powershell
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

Recommended extensions from VS Code marketplace:

1. **C# Dev Kit** - Comprehensive C# support
2. **GitHub Copilot** - AI-powered code completion
3. **REST Client** - API testing within VS Code
4. **NuGet Gallery** - Package management

### 5.2. <a name='VisualStudio2022Alternative'></a>Visual Studio 2022 (Alternative)

Install Visual Studio 2022:

```powershell
winget install Microsoft.VisualStudio.2022.Community
```

During installation, select:
- **ASP.NET and web development** workload
- **GitHub Copilot** component (if available)

Or install GitHub Copilot extension:
1. Open Visual Studio
2. Extensions → Manage Extensions
3. Search for "GitHub Copilot"
4. Download and install

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

### 6.2. <a name='SQLServerLocalDBOptional'></a>SQL Server LocalDB (Optional)

SQL Server LocalDB is included with Visual Studio. To use it:

1. Open Visual Studio Installer
2. Modify installation
3. Under Individual Components, ensure **SQL Server Express LocalDB** is checked

Update packages and connection string:

```powershell
dotnet add package Microsoft.EntityFrameworkCore.SqlServer --version 9.0.0
```

```json
{
  "ConnectionStrings": {
    "DefaultConnection": "Server=(localdb)\\mssqllocaldb;Database=TaskManager;Trusted_Connection=True;MultipleActiveResultSets=true"
  }
}
```

## 7. <a name='Verification'></a>Verification

Run these commands to verify your setup:

```powershell
# Check .NET SDK
dotnet --version
Write-Host "✓ .NET SDK OK" -ForegroundColor Green

# Check EF Core tools
dotnet ef --version
Write-Host "✓ EF Core Tools OK" -ForegroundColor Green

# Check Git
git --version
Write-Host "✓ Git OK" -ForegroundColor Green

# Test project compilation
cd project3\task-manager
dotnet build
Write-Host "✓ Build OK" -ForegroundColor Green

# Run application (Ctrl+C to stop)
dotnet run --project src/TaskManager.Web
```

Expected access points after starting:

- **Application**: http://localhost:5000 or https://localhost:5001
- **Swagger UI**: https://localhost:5001/swagger
- **Health Check**: http://localhost:5000/health

## 8. <a name='Troubleshooting'></a>Troubleshooting

### Common Issues and Solutions

**1. .NET SDK Not Found**

```powershell
# Check installation
dotnet --list-sdks

# If missing, reinstall
winget install Microsoft.DotNet.SDK.9 --force
```

**2. EF Core Tools Not Found**

```powershell
# Ensure tools are in PATH
$env:PATH += ";$env:USERPROFILE\.dotnet\tools"

# Reinstall tools
dotnet tool uninstall --global dotnet-ef
dotnet tool install --global dotnet-ef
```

**3. Port Already in Use**

```powershell
# Find process using port 5000
netstat -ano | findstr :5000

# Kill process by PID (replace 1234 with actual PID)
taskkill /PID 1234 /F

# Or change port in Properties/launchSettings.json
```

**4. NuGet Packages Not Restoring**

```powershell
# Clear NuGet cache
dotnet nuget locals all --clear

# Restore packages
dotnet restore
```

**5. SSL Certificate Issues**

```powershell
# Trust development certificate
dotnet dev-certs https --trust
```

**6. IDE Not Recognizing C#**

- Restart VS Code
- Press `Ctrl+Shift+P` → `.NET: Restart Language Server`
- Verify C# Dev Kit extension is installed and enabled

**7. PowerShell Execution Policy**

```powershell
# If scripts are blocked
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Technology Stack Summary

- **Framework**: ASP.NET Core 10.0
- **ORM**: Entity Framework Core 9.0
- **Database**: SQLite (development) / SQL Server LocalDB (optional)
- **Frontend**: Razor Pages + Bootstrap 5.3
- **Validation**: FluentValidation
- **Testing**: xUnit, Moq, FluentAssertions
- **API Documentation**: Swagger/OpenAPI

### Next Steps

After completing setup:

1. Open the project in VS Code: `code project3\task-manager`
2. Verify GitHub Copilot is working
3. Start building the Task Manager application!
