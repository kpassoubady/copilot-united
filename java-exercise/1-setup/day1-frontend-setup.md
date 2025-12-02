# 🎨 Day 1 Setup: Frontend & Web Layer Prerequisites

## 🎯 Setup Overview

This setup ensures Day 1 backend is working correctly and prepares your environment for Day 1 frontend development (afternoon sessions). You'll verify the backend services and add frontend dependencies.

**⏱️ Estimated Setup Time: 3 minutes**

---

## ✅ Prerequisites Verification

### 🏗️ Day 1 Backend Must Be Complete

**Verify Backend Services Working**

```bash
# Navigate to your project directory
cd Personal-Expense-Tracker

# Start the application
mvn spring-boot:run

# In another terminal, test the backend
curl -X GET http://localhost:8080/api/categories
curl -X GET http://localhost:8080/api/expenses

# You should see JSON responses with sample data
# Stop the application with Ctrl+C
```

**Required Backend Components**

- [ ] `ExpenseTrackerApplication.java` starts without errors
- [ ] `CategoryService` and `ExpenseService` working
- [ ] H2 database with sample data
- [ ] All unit tests passing: `mvn test`

---

## 📦 Frontend Dependencies Setup

### 🔧 Update Maven Dependencies

Add these dependencies to your `pom.xml` (if not already present):

```xml
<!-- Thymeleaf for templating -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-thymeleaf</artifactId>
</dependency>

<!-- WebJars for frontend libraries -->
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

<!-- Optional: Chart.js for dashboard charts -->
<dependency>
    <groupId>org.webjars.npm</groupId>
    <artifactId>chart.js</artifactId>
    <version>4.4.0</version>
</dependency>
```

**Install Dependencies**

```bash
# Download new dependencies
mvn clean install
```

---

## 🗂️ Frontend Directory Structure

### 📁 Create Frontend Directories

```bash
# Create template directories
mkdir -p src/main/resources/templates/layout
mkdir -p src/main/resources/templates/home
mkdir -p src/main/resources/templates/expenses
mkdir -p src/main/resources/templates/categories

# Create static resource directories  
mkdir -p src/main/resources/static/css
mkdir -p src/main/resources/static/js
mkdir -p src/main/resources/static/images
```

### 🎨 Expected Structure After Web Layer Session

```text
src/main/resources/
├── templates/
│   ├── layout/
│   │   └── main.html
│   ├── home/
│   │   └── dashboard.html
│   ├── expenses/
│   │   ├── list.html
│   │   └── form.html
│   └── categories/
│       ├── list.html
│       └── form.html
└── static/
    ├── css/
    │   └── custom.css
    ├── js/
    │   ├── dashboard.js
    │   └── expenses.js
    └── images/
```

---

## 🔧 Configuration Updates

### ⚙️ Update Application Properties

Add frontend-specific configuration to `application.properties`:

```properties
# Existing configuration...

# Thymeleaf Configuration
spring.thymeleaf.cache=false
spring.thymeleaf.mode=HTML
spring.thymeleaf.encoding=UTF-8
spring.thymeleaf.prefix=classpath:/templates/
spring.thymeleaf.suffix=.html

# Static Resources
spring.web.resources.static-locations=classpath:/static/
spring.web.resources.cache.cachecontrol.max-age=3600

# File Upload Configuration (for future enhancements)
spring.servlet.multipart.max-file-size=10MB
spring.servlet.multipart.max-request-size=10MB

# Error Page Configuration
server.error.include-message=always
server.error.include-binding-errors=always
```

---

## 🌐 Web Browser Setup

### 🔍 Browser Developer Tools

Ensure you have:

- **Chrome DevTools** or **Firefox Developer Tools** enabled
- **Responsive Design Mode** for testing mobile layouts
- **Console** access for JavaScript debugging
- **Network Tab** for monitoring AJAX requests

### 📱 Testing Viewports

Prepare to test these screen sizes:

- Desktop: 1920x1080, 1366x768
- Tablet: 768x1024, 1024x768  
- Mobile: 375x667, 414x736

---

## ✅ Setup Verification

### 🧪 Test Template Rendering

Create a simple test template to verify setup:

```html
<!-- src/main/resources/templates/test.html -->
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>Setup Test</title>
    <link href="/webjars/bootstrap/5.3.2/css/bootstrap.min.css" rel="stylesheet">
    <style>
      body { padding: 2rem; }
    </style>
  </head>
<body>
    <div class="container">
        <h1 class="text-primary">Day 1 Setup Successful!</h1>
        <p>Bootstrap CSS is working</p>
        <button class="btn btn-success">Bootstrap Button Works</button>
    </div>
    <script src="/webjars/jquery/3.7.1/jquery.min.js"></script>
    <script src="/webjars/bootstrap/5.3.2/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

### 🎮 Create Test Controller

```java
// src/main/java/com/expensetracker/app/controller/TestController.java
package com.expensetracker.app.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class TestController {
    
    @GetMapping("/test")
    public String testPage() {
        return "test";
    }
}
```

### 🚀 Run Verification Test

```bash
# Start the application
mvn spring-boot:run

# Open browser and visit:
# http://localhost:8080/test

# You should see:
# - "Day 1 Setup Successful!" heading in blue
# - Bootstrap-styled button
# - No console errors in browser
```

---

## 🎨 IDE Extensions for Frontend

### 📝 VS Code Extensions (Optional but Recommended)

Install these extensions for better frontend development:

- **HTML CSS Support** - Enhanced HTML/CSS IntelliSense
- **Auto Rename Tag** - Automatically rename paired HTML tags
- **Live Server** - Live reload for static files (if needed)
- **Thymeleaf Language Support** - Syntax highlighting for Thymeleaf
- **Bootstrap 5 Quick Snippets** - Bootstrap component snippets

### 🔧 VS Code Settings for Frontend

Add to your `.vscode/settings.json`:

```json
{
    "emmet.includeLanguages": {
        "html": "html",
        "javascript": "html"
    },
    "html.format.indentHandlebars": true,
    "html.format.indentInnerHtml": true,
    "css.validate": true,
    "javascript.validate.enable": true
}
```

---

## 🚨 Troubleshooting

### Common Frontend Issues

**Bootstrap CSS Not Loading**

```bash
# Verify WebJars dependencies
mvn dependency:tree | grep webjars

# Check static resource mapping in logs
# Should see: "Mapped to ResourceHttpRequestHandler"
```

**Thymeleaf Templates Not Found**

```text
# Check template path structure:
src/main/resources/templates/
# Templates must have .html extension
# Use th: namespace in templates
```

**JavaScript Console Errors**

- Check browser Network tab for 404 errors
- Verify jQuery loads before Bootstrap
- Check for syntax errors in custom JavaScript

---

## ✅ Ready for Day 1 Afternoon

### 🎯 Success Checklist

- [ ] Day 1 backend fully functional and tested
- [ ] Frontend dependencies added and downloaded
- [ ] Template directory structure created
- [ ] Static resource directories created
- [ ] Application properties updated for frontend
- [ ] Test template renders correctly with Bootstrap styling
- [ ] No console errors in browser
- [ ] IDE configured for frontend development

### 🚀 Next Steps

You're now ready to start **Day 1: Web Layer & Frontend Implementation**!

### 📋 What You'll Build Today

- REST API controllers for all CRUD operations
- Beautiful Thymeleaf templates with responsive design
- Interactive dashboard with charts and analytics
- Form handling with validation and AJAX
- Mobile-responsive expense management interface

**Let's create an amazing web interface! 🎨**
