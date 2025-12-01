# Project 1: Spring Boot Task Manager Installation Guide (macOS)

<!-- markdownlint-disable MD033 MD029 MD010-->
<!-- vscode-markdown-toc -->
- [Project 1: Spring Boot Task Manager Installation Guide (macOS)](#project-1-spring-boot-task-manager-installation-guide-macos)
  - [1. Step 1: Install Java Development Kit (JDK)](#1-step-1-install-java-development-kit-jdk)
    - [1.1. Setup JAVA\_HOME](#11-setup-java_home)
  - [2. Step 2: Install Maven](#2-step-2-install-maven)
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

Open the terminal and install OpenJDK 17 or higher (recommended: JDK 21)

```bash
brew install openjdk@21
```

### 1.1. <a name='SetupJAVA_HOME'></a>Setup JAVA_HOME

After installation, create a symbolic link for system-wide access:

```bash
sudo ln -sfn /usr/local/opt/openjdk@21/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk-21.jdk
```

Add OpenJDK to your PATH by adding this line to your shell profile:

```bash
echo 'export PATH="/usr/local/opt/openjdk@21/bin:$PATH"' >> ~/.zshrc
```

Set JAVA_HOME in your ~/.zshrc:

```bash
echo 'export JAVA_HOME=`/usr/libexec/java_home -v 21`' >> ~/.zshrc
```

Reload your shell configuration:

```bash
source ~/.zshrc
```

Note: On Apple Silicon (M1/M2/M3), Homebrew usually installs under `/opt/homebrew` instead of `/usr/local`. If `brew --prefix` prints `/opt/homebrew`, adjust the paths above accordingly:

```bash
echo 'export PATH="$(brew --prefix)/opt/openjdk@21/bin:$PATH"' >> ~/.zshrc
sudo ln -sfn "$(brew --prefix)/opt/openjdk@21/libexec/openjdk.jdk" /Library/Java/JavaVirtualMachines/openjdk-21.jdk
source ~/.zshrc
```

Validate Java installation:

```bash
java -version
javac -version
```

You should see Java 21 version information.

## 2. <a name='Step2:InstallMaven'></a>Step 2: Install Maven

Install Maven using Homebrew:

```bash
brew install maven
```

Add Maven to your PATH by adding these lines to your ~/.zshrc:

```bash
export M2_HOME=/usr/local/Cellar/maven/$(brew list --versions maven | cut -d' ' -f2)
export M2=$M2_HOME/bin
export PATH=$M2:$PATH
```

Reload your shell configuration:

```bash
source ~/.zshrc
```

Validate Maven installation:

```bash
mvn -version
```

You should see Maven version information along with Java details.

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

Validate Git installation:

```bash
git --version
```

## 4. <a name='ProjectSetup'></a>Project Setup

### 4.1. <a name='CreateProjectFolder'></a>Create Project Folder

> Quick start (recommended if you cloned this repo):
>
> ```bash
> # Use the provided Spring Boot project
> cd project1/task-manager
> mvn clean compile
> mvn spring-boot:run
> ```
>
> Then open http://localhost:8080. If you want to scaffold from scratch instead, follow the steps below.

Create the main project directory:

```bash
mkdir -p project1
cd project1
```

### 4.2. <a name='CreateSpringBootFull-StackProject'></a>Create Spring Boot Full-Stack Project

Create the Spring Boot project using Maven archetype:

```bash
mvn archetype:generate \
  -DgroupId=com.taskmanager.app \
  -DartifactId=task-manager \
  -DarchetypeArtifactId=maven-archetype-quickstart \
  -DarchetypeVersion=1.5 \
  -DinteractiveMode=false
```

Navigate to the project directory:

```bash
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

Create the main Spring Boot application class. Create the file `src/main/java/com/taskmanager/app/TaskManagerApplication.java`:

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

Create `src/main/resources/application.properties`:

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

```bash
mkdir -p src/main/java/com/taskmanager/app/config
```

Create `src/main/java/com/taskmanager/app/config/SecurityConfig.java`:

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

Create a simple home controller. Create the file `src/main/java/com/taskmanager/app/controller/HomeController.java`:

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

```bash
mkdir -p src/main/resources/templates
mkdir -p src/main/resources/static/css
mkdir -p src/main/resources/static/js
```

Create `src/main/resources/templates/index.html`:

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

```bash
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

Install the following VS Code extensions:

Install via VS Code marketplace:

1. **Extension Pack for Java** - Comprehensive Java support
2. **Spring Boot Extension Pack** - Spring Boot development tools
3. **GitHub Copilot** - AI-powered code completion
4. **REST Client** - API testing within VS Code
5. **Thunder Client** - Alternative API testing tool
6. **HTML CSS Support** - Enhanced HTML/CSS editing
7. **Auto Rename Tag** - Automatically rename paired HTML tags

Install via VS Code through command line:
Enable code installation from command line:
Code > Settings > Command Line > Enable code installation from command line
Code > View > Command Palette > Type "Shell Command: Install 'code' command in PATH" and press Enter
> Press OK to install > Wait for installation to complete > Press OK to close the window 

Open a new terminal > Type "code --version" and press Enter > You should see the version of VS Code installed

Install extensions:
```bash
code --install-extension vscjava.vscode-java-pack
code --install-extension vmware.vscode-spring-boot
code --install-extension github.copilot
code --install-extension humao.rest-client
code --install-extension rangav.vscode-thunder-client
code --install-extension ecmel.vscode-html-css
code --install-extension formulahendry.auto-rename-tag
```

### 5.2. <a name='IntelliJIDEASetupAlternative'></a>IntelliJ IDEA Setup (Alternative)

If using IntelliJ IDEA:

1. Install IntelliJ IDEA Community or Ultimate
2. Install plugins:
   - Spring Boot (usually pre-installed)
   - GitHub Copilot


## 6. <a name='DatabaseSetup'></a>Database Setup

### 6.1. <a name='H2DatabaseDefault'></a>H2 Database (Default)

H2 is configured by default and requires no additional setup. It's an in-memory database perfect for development.

### 6.2. <a name='PostgreSQLOptional'></a>PostgreSQL (Optional)

If you prefer PostgreSQL for development (optional):

Install PostgreSQL:

```bash
brew install postgresql@15
brew services start postgresql@15
```

Restart your terminal or open a new terminal.

Create a database:

```bash
createdb taskmanager
```

Update `application.properties` for PostgreSQL:

```properties
# PostgreSQL Configuration
spring.datasource.url=jdbc:postgresql://localhost:5432/taskmanager
spring.datasource.username=your_username
spring.datasource.password=your_password
spring.datasource.driver-class-name=org.postgresql.Driver

# JPA Configuration
spring.jpa.database-platform=org.hibernate.dialect.PostgreSQLDialect
spring.jpa.hibernate.ddl-auto=create-drop
spring.jpa.show-sql=true
```

Add PostgreSQL dependency to `pom.xml`:

```xml
<dependency>
    <groupId>org.postgresql</groupId>
    <artifactId>postgresql</artifactId>
    <scope>runtime</scope>
</dependency>
```

## 7. <a name='Verification'></a>Verification

Verify your complete setup:

1. **Java and Maven**:
   ```bash
   java -version
   mvn -version
   ```

2. **Project Structure**:
   ```bash
   cd project1
   ls -la
   ```
   
   You should see:
   - `task-manager/` (Spring Boot full-stack project)

3. **Dependencies**:
   ```bash
   cd task-manager
   mvn dependency:tree
   ```

4. **Application Start**:
   ```bash
   mvn spring-boot:run
   ```
   
   Verify the application starts without errors and is accessible at http://localhost:8080

## 8. <a name='Troubleshooting'></a>Troubleshooting

### Common Issues and Solutions

1. **Java Version Issues**:
   - Ensure JAVA_HOME is set correctly
   - Verify Java 17+ is installed
   - Check Maven is using the correct Java version

2. **Port Conflicts**:
   - Change `server.port` in `application.properties`
   - Use `SERVER_PORT=8081 mvn spring-boot:run`

3. **Maven Dependencies**:
   - Clear Maven cache: `mvn clean install -U`
   - Check internet connection for dependency downloads

4. **Template Issues**:
   - Ensure templates are in `src/main/resources/templates/`
   - Check Thymeleaf syntax in HTML files
   - Verify WebJars dependencies are loaded

5. **Permission Issues**:
   - Ensure proper file permissions
   - Use `sudo` only when necessary for system-wide installations

### Verification Commands

Run these commands to ensure everything is working:

```bash
# Check Java
java -version && echo "✓ Java OK"

# Check Maven
mvn -version && echo "✓ Maven OK"

# Check Git
git --version && echo "✓ Git OK"

# Test application compilation
cd project1/task-manager
mvn clean compile && echo "✓ Compilation OK"
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
> ```bash
> ~/.m2/settings.xml
> ```
> 
> Contact your DevOps team for organization-specific configurations.
