# Project 1: Spring Boot Task Manager Installation Guide (Windows 11)

<!-- markdownlint-disable MD033 MD029 MD010-->
<!-- vscode-markdown-toc -->
- [Project 1: Spring Boot Task Manager Installation Guide (Windows 11)](#project-1-spring-boot-task-manager-installation-guide-windows-11)
  - [1. Step 1: Install Java Development Kit (JDK)](#1-step-1-install-java-development-kit-jdk)
    - [1.1. Set JAVA\_HOME Environment Variable](#11-set-java_home-environment-variable)
  - [2. Step 2: Install Maven](#2-step-2-install-maven)
    - [2.1. Download and Extract Maven](#21-download-and-extract-maven)
    - [2.2. Set Maven Environment Variables](#22-set-maven-environment-variables)
  - [3. Step 3: Install Git](#3-step-3-install-git)
  - [4. Project Setup](#4-project-setup)
    - [4.1. Create Project Folder](#41-create-project-folder)
    - [4.2. Create Spring Boot Full-Stack Project](#42-create-spring-boot-full-stack-project)
    - [4.3. Update Project Dependencies](#43-update-project-dependencies)
    - [4.4. Test Project Setup](#44-test-project-setup)
  - [5. IDE Setup](#5-ide-setup)
    - [5.1. Visual Studio Code Extensions](#51-visual-studio-code-extensions)
    - [5.2. IntelliJ IDEA Setup (Alternative)](#52-intellij-idea-setup-alternative)
  - [6. Database Setup](#6-database-setup)
    - [6.1. H2 Database (Default)](#61-h2-database-default)
    - [6.2. PostgreSQL (Optional)](#62-postgresql-optional)
  - [7. Verification](#7-verification)
  - [8. Troubleshooting](#8-troubleshooting)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

## 1. <a name='Step1:InstallJavaDevelopmentKitJDK'></a>Step 1: Install Java Development Kit (JDK)

Download and install Java 17 or higher (recommended: JDK 21).

1. **Download JDK**:
   - Visit [Oracle Java Downloads](https://www.oracle.com/java/technologies/javase/jdk21-archive-downloads.html) or [OpenJDK](https://jdk.java.net/21/) - [Archive](https://jdk.java.net/archive/) or [Adoptium](https://adoptium.net/)
   - Download the Windows x64 installer (.msi file)

2. **Install JDK**:
   - Run the downloaded installer
   - Follow the installation wizard
   - Note the installation path (typically `C:\Program Files\Java\jdk-21`)

### 1.1. <a name='SetJAVA_HOMEEnvironmentVariable'></a>Set JAVA_HOME Environment Variable

1. **Open Environment Variables**:
   - Press `Windows + R`, type `sysdm.cpl`, and press Enter
   - Click on the "Advanced" tab
   - Click "Environment Variables"

2. **Set JAVA_HOME**:
   - In "System Variables", click "New"
   - Variable name: `JAVA_HOME`
   - Variable value: `C:\Program Files\Java\jdk-21` (adjust path if different)
   - Click "OK"

3. **Update PATH**:
   - Find "Path" in System Variables and click "Edit"
   - Click "New" and add: `%JAVA_HOME%\bin`
   - Click "OK" to close all dialogs

4. **Verify Installation**:
   - Open Command Prompt (cmd)
   - Run the following commands:

```cmd
java -version
javac -version
```

You should see Java 21 version information.

## 2. <a name='Step2:InstallMaven'></a>Step 2: Install Maven

### 2.1. <a name='DownloadandExtractMaven'></a>Download and Extract Maven

1. **Download Maven**:
   - Visit [Apache Maven Downloads](https://maven.apache.org/download.cgi)
   - Download the Binary zip archive (e.g., `apache-maven-3.9.6-bin.zip`)

2. **Extract Maven**:
   - Extract the zip file to `C:\Program Files\Maven`
   - The final path should be `C:\Program Files\Maven\apache-maven-3.9.6`

### 2.2. <a name='SetMavenEnvironmentVariables'></a>Set Maven Environment Variables

1. **Set M2_HOME**:
   - Open Environment Variables (same as Step 1.1)
   - In "System Variables", click "New"
   - Variable name: `M2_HOME`
   - Variable value: `C:\Program Files\Maven\apache-maven-3.9.6`
   - Click "OK"

2. **Update PATH**:
   - Find "Path" in System Variables and click "Edit"
   - Click "New" and add: `%M2_HOME%\bin`
   - Click "OK" to close all dialogs

3. **Verify Installation**:
   - Open a new Command Prompt
   - Run:

```cmd
mvn -version
```

You should see Maven version information along with Java details.

## 3. <a name='Step3:InstallGit'></a>Step 3: Install Git

1. **Download Git**:
   - Visit [Git for Windows](https://git-scm.com/download/win)
   - Download the 64-bit Git for Windows Setup

2. **Install Git**:
   - Run the installer
   - Use default settings or customize as needed
   - Ensure "Git from the command line and also from 3rd-party software" is selected

3. **Configure Git**:
   - Open Command Prompt or Git Bash
   - Configure your identity:

```cmd
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

4. **Verify Installation**:

```cmd
git --version
```

## 4. <a name='ProjectSetup'></a>Project Setup

### 4.1. <a name='CreateProjectFolder'></a>Create Project Folder

> Quick start (recommended if you cloned this repo):
>
> ```cmd
> REM Use the provided Spring Boot project
> cd project1\task-manager
> mvn clean compile
> mvn spring-boot:run
> ```
>
> Then open http://localhost:8080. If you want to scaffold from scratch instead, follow the steps below.

Open Command Prompt and create the project directory:

```cmd
mkdir project1
cd project1
```

### 4.2. <a name='CreateSpringBootFull-StackProject'></a>Create Spring Boot Full-Stack Project

Create the Spring Boot project using Maven archetype:

```cmd
mvn archetype:generate -DgroupId=com.taskmanager.app -DartifactId=task-manager -DarchetypeArtifactId=maven-archetype-quickstart -DarchetypeVersion=1.5 -DinteractiveMode=false
```

Navigate to the project directory:

```cmd
cd task-manager
```

### 4.3. <a name='UpdateProjectDependencies'></a>Update Project Dependencies

Replace the contents of `pom.xml` with the following Spring Boot configuration:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.2.3</version>
        <relativePath/>
    </parent>
    
    <groupId>com.taskmanager.app</groupId>
    <artifactId>task-manager</artifactId>
    <version>1.0.0</version>
    <name>task-manager</name>
    <description>Task Manager Full-Stack Application with Spring Boot</description>
    
    <properties>
        <java.version>21</java.version>
        <maven.compiler.source>21</maven.compiler.source>
        <maven.compiler.target>21</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>
    
    <dependencies>
        <!-- Spring Boot Web Starter (includes Thymeleaf) -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        
        <!-- Thymeleaf Template Engine -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-thymeleaf</artifactId>
        </dependency>
        
        <!-- Spring Data JPA -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>
        
        <!-- Spring Security -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-security</artifactId>
        </dependency>
        
        <!-- Validation -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-validation</artifactId>
        </dependency>
        
        <!-- H2 Database -->
        <dependency>
            <groupId>com.h2database</groupId>
            <artifactId>h2</artifactId>
            <scope>runtime</scope>
        </dependency>
        
        <!-- Bootstrap and jQuery (WebJars) -->
        <dependency>
            <groupId>org.webjars</groupId>
            <artifactId>bootstrap</artifactId>
            <version>5.3.2</version>
        </dependency>
        
        <dependency>
            <groupId>org.webjars</groupId>
            <artifactId>jquery</artifactId>
            <version>3.7.1</version>
        </dependency>
        
        <dependency>
            <groupId>org.webjars</groupId>
            <artifactId>webjars-locator-core</artifactId>
        </dependency>
        
        <!-- API Documentation -->
        <dependency>
            <groupId>org.springdoc</groupId>
            <artifactId>springdoc-openapi-starter-webmvc-ui</artifactId>
            <version>2.2.0</version>
        </dependency>
        
        <!-- Development Tools -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-devtools</artifactId>
            <scope>runtime</scope>
            <optional>true</optional>
        </dependency>
        
        <!-- Testing -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
        
        <dependency>
            <groupId>org.springframework.security</groupId>
            <artifactId>spring-security-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>
    
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
</project>
```

### 4.4. <a name='TestProjectSetup'></a>Test Project Setup

Create the main Spring Boot application class. Create the directory structure and file:

```cmd
mkdir src\main\java\com\taskmanager\app
```

Create `src\main\java\com\taskmanager\app\TaskManagerApplication.java`:

```java
package com.taskmanager.app;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class TaskManagerApplication {
    public static void main(String[] args) {
        SpringApplication.run(TaskManagerApplication.class, args);
    }
}
```

Create the resources directory and configuration file:

```cmd
mkdir src\main\resources
```

Create `src\main\resources\application.properties`:

```properties
# Server Configuration
server.port=8080

# H2 Database Configuration
spring.datasource.url=jdbc:h2:mem:taskmanager
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=password

# JPA Configuration
spring.jpa.database-platform=org.hibernate.dialect.H2Dialect
spring.jpa.hibernate.ddl-auto=create-drop
spring.jpa.show-sql=true

# H2 Console (for development)
spring.h2.console.enabled=true
spring.h2.console.path=/h2-console

# Thymeleaf Configuration
spring.thymeleaf.cache=false
spring.thymeleaf.prefix=classpath:/templates/
spring.thymeleaf.suffix=.html

# API Documentation
springdoc.api-docs.path=/api-docs
springdoc.swagger-ui.path=/swagger-ui.html
```

Create a Spring Security configuration file to allow all requests during development. Create the directory and file:

```cmd
mkdir src\main\java\com\taskmanager\app\config
```

Create `src\main\java\com\taskmanager\app\config\SecurityConfig.java`:

```java
package com.taskmanager.app.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.web.SecurityFilterChain;

@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .authorizeHttpRequests(authz -> authz
                .anyRequest().permitAll()
            )
            .csrf(csrf -> csrf.disable())
            .headers(headers -> headers.frameOptions().disable()); // For H2 console if needed
        
        return http.build();
    }
}
```

Create a simple home controller. Create the directory and file:

```cmd
mkdir src\main\java\com\taskmanager\app\controller
```

Create `src\main\java\com\taskmanager\app\controller\HomeController.java`:

```java
package com.taskmanager.app.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HomeController {
    
    @GetMapping("/")
    public String home(Model model) {
        model.addAttribute("message", "Welcome to Task Manager!");
        return "index";
    }
}
```

Create the templates directory and a basic HTML template:

```cmd
mkdir src\main\resources\templates
mkdir src\main\resources\static\css
mkdir src\main\resources\static\js
```

Create `src\main\resources\templates\index.html`:

```html
<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Task Manager</title>
    <link th:href="@{/webjars/bootstrap/5.3.2/css/bootstrap.min.css}" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card">
                    <div class="card-header">
                        <h1 class="text-center">Task Manager</h1>
                    </div>
                    <div class="card-body text-center">
                        <h2 th:text="${message}">Welcome Message</h2>
                        <p class="lead">Your Java-powered task management solution</p>
                        <a href="/tasks" class="btn btn-primary">View Tasks</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <script th:src="@{/webjars/bootstrap/5.3.2/js/bootstrap.bundle.min.js}"></script>
    <script th:src="@{/webjars/jquery/3.7.1/jquery.min.js}"></script>
</body>
</html>
```

Test the application:

```cmd
mvn clean compile
mvn spring-boot:run
```

The application should start on port 8080. You can access:
- Home Page: http://localhost:8080
- H2 Console: http://localhost:8080/h2-console
- Swagger UI: http://localhost:8080/swagger-ui.html

Stop the application with `Ctrl+C`.

## 5. <a name='IDESetup'></a>IDE Setup

### 5.1. <a name='VisualStudioCodeExtensions'></a>Visual Studio Code Extensions

Install Visual Studio Code from [https://code.visualstudio.com/](https://code.visualstudio.com/)

Install the following extensions:

1. **Extension Pack for Java** - Comprehensive Java support
2. **Spring Boot Extension Pack** - Spring Boot development tools
3. **GitHub Copilot** - AI-powered code completion
4. **GitHub Copilot Chat** - AI-powered chat assistance
5. **REST Client** - API testing within VS Code
6. **Thunder Client** - Alternative API testing tool
7. **HTML CSS Support** - Enhanced HTML/CSS editing
8. **Auto Rename Tag** - Automatically rename paired HTML tags

You can install these extensions through the VS Code marketplace or using the command palette (`Ctrl+Shift+P`).

### 5.2. <a name='IntelliJIDEASetupAlternative'></a>IntelliJ IDEA Setup (Alternative)

If using IntelliJ IDEA:

1. Download and install IntelliJ IDEA Community or Ultimate from [JetBrains](https://www.jetbrains.com/idea/)
2. Install plugins:
   - Spring Boot (usually pre-installed)
   - GitHub Copilot
   - Thymeleaf

## 6. <a name='DatabaseSetup'></a>Database Setup

### 6.1. <a name='H2DatabaseDefault'></a>H2 Database (Default)

H2 is configured by default and requires no additional setup. It's an in-memory database perfect for development and testing.

### 6.2. <a name='PostgreSQLOptional'></a>PostgreSQL (Optional)

If you prefer PostgreSQL for development:

1. **Install PostgreSQL**:
   - Download from [PostgreSQL Downloads](https://www.postgresql.org/download/windows/)
   - Install using the installer
   - Remember the password you set for the postgres user

2. **Create Database**:
   - Open pgAdmin or use command line
   - Create a new database named `taskmanager`

3. **Update Configuration**:
   Update `application.properties` for PostgreSQL:

```properties
# PostgreSQL Configuration
spring.datasource.url=jdbc:postgresql://localhost:5432/taskmanager
spring.datasource.username=postgres
spring.datasource.password=your_password
spring.datasource.driver-class-name=org.postgresql.Driver

# JPA Configuration
spring.jpa.database-platform=org.hibernate.dialect.PostgreSQLDialect
spring.jpa.hibernate.ddl-auto=create-drop
spring.jpa.show-sql=true
```

4. **Add PostgreSQL Dependency**:
   Add to `pom.xml`:

```xml
<dependency>
    <groupId>org.postgresql</groupId>
    <artifactId>postgresql</artifactId>
    <scope>runtime</scope>
</dependency>
```

## 7. <a name='Verification'></a>Verification

Verify your complete setup by running these commands in Command Prompt:

1. **Java and Maven**:
   ```cmd
   java -version
   mvn -version
   ```

2. **Git**:
   ```cmd
   git --version
   ```

3. **Project Structure**:
   ```cmd
   cd project1
   dir
   ```
   
   You should see:
   - `task-manager\` (Spring Boot full-stack project)

4. **Dependencies**:
   ```cmd
   cd task-manager
   mvn dependency:tree
   ```

5. **Application Start**:
   ```cmd
   mvn spring-boot:run
   ```
   
   Verify the application starts without errors and is accessible at http://localhost:8080

## 8. <a name='Troubleshooting'></a>Troubleshooting

### Common Issues and Solutions

1. **Java Version Issues**:
   - Ensure JAVA_HOME points to the correct JDK installation
   - Verify Java 17+ is installed
   - Restart Command Prompt after setting environment variables

2. **Maven Issues**:
   - Ensure M2_HOME is set correctly
   - Verify Maven bin directory is in PATH
   - Clear Maven cache: `mvn clean install -U`

3. **Port Conflicts**:
   - Change `server.port` in `application.properties`
   - Set environment variable `PORT=8081` before running `mvn spring-boot:run`

4. **Template Issues**:
   - Ensure templates are in `src\main\resources\templates\`
   - Check Thymeleaf syntax in HTML files
   - Verify WebJars dependencies are loaded

5. **Permission Issues**:
   - Run Command Prompt as Administrator if needed
   - Ensure antivirus software isn't blocking installations

6. **Path Issues**:
   - Use full paths if relative paths don't work
   - Ensure no spaces in folder names
   - Use backslashes (`\`) for Windows paths

### Verification Commands

Run these commands to ensure everything is working:

```cmd
REM Check Java
java -version && echo Java OK

REM Check Maven
mvn -version && echo Maven OK

REM Check Git
git --version && echo Git OK

REM Test application compilation
cd project1\task-manager
mvn clean compile && echo Compilation OK
```

### Environment Variables Check

Verify your environment variables are set correctly:

```cmd
echo %JAVA_HOME%
echo %M2_HOME%
echo %PATH%
```

### Technology Stack Summary

- **Backend**: Spring Boot + Spring MVC + Spring Data JPA + Spring Security
- **Frontend**: Thymeleaf templates + Bootstrap CSS + jQuery
- **Database**: H2 (development) / PostgreSQL (optional)
- **Build Tool**: Maven
- **Development**: Spring Boot DevTools for hot reload

### Note

> If your organization requires specific Maven `settings.xml` configuration for artifact downloads, obtain the file from your DevOps team and place it in:
> 
> ```
> C:\Users\%USERNAME%\.m2\settings.xml
> ```
> 
> Contact your DevOps team for organization-specific configurations and proxy settings.
