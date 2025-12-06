# 🎨 Day 1 - Session 4a: Personal Expense Tracker - Web Interface with HTMX (Alternative)

## ⚠️ When to Use This Alternative

Use this guide if:
- Thymeleaf configuration is causing issues
- Template resolution errors are occurring
- You prefer a simpler, more modern approach
- You want to leverage the REST APIs you already built

**HTMX** is a lightweight library that enhances HTML with AJAX capabilities - no complex template engine configuration required!

---

## 🎯 Learning Objectives

By the end of this session, you will:

- Create dynamic web pages using HTMX + plain HTML
- Leverage REST APIs (built in Session 3) for data operations
- Build responsive interfaces with Bootstrap 5
- Implement CRUD operations without page reloads
- Master GitHub Copilot for frontend code generation

**⏱️ Time Allocation: 45 minutes**

---

## 📋 Prerequisites Check (2 minutes)

- ✅ Session 3 completed (REST APIs working)
- ✅ All REST endpoints tested (`/api/categories`, `/api/expenses`)
- ✅ Application running on `http://localhost:8080`

**Quick Test**: Verify your APIs are ready:

```bash
curl http://localhost:8080/api/categories
curl http://localhost:8080/api/expenses
```

---

## 🚀 What is HTMX?

HTMX allows you to access modern browser features directly from HTML, without writing JavaScript:

```html
<!-- This button loads content from the server when clicked -->
<button hx-get="/api/categories" hx-target="#result">
    Load Categories
</button>
<div id="result"></div>
```

**Key Benefits:**
- No template engine configuration
- Works directly with REST APIs
- Minimal JavaScript required
- Copilot generates HTMX attributes easily

---

## 📝 Step 1: Setup Static Resources (5 minutes)

### 📁 Create Directory Structure

```
src/main/resources/
└── static/
    ├── index.html
    ├── categories.html
    ├── expenses.html
    ├── css/
    │   └── custom.css
    └── js/
        └── app.js
```

### 🔧 Enable CORS for API (if needed)

**Copilot Prompt:**

```text
@workspace Add CORS configuration to allow requests from static HTML files to REST APIs
```

Add to your Spring Boot application:

```java
// src/main/java/com/expense/tracker/config/WebConfig.java
package com.expense.tracker.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class WebConfig implements WebMvcConfigurer {
    
    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/api/**")
                .allowedOrigins("*")
                .allowedMethods("GET", "POST", "PUT", "DELETE")
                .allowedHeaders("*");
    }
}
```

---

## 📝 Step 2: Create Base HTML Page (5 minutes)

### 🏠 Main Index Page

**Copilot Prompt:**

```text
/generate Create a static HTML index page for expense tracker with:
- Bootstrap 5 CDN links
- HTMX CDN link
- Navigation bar with links to Dashboard, Categories, Expenses
- Font Awesome icons
- Footer with copyright
- Container for main content
```

**Expected file**: `src/main/resources/static/index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Personal Expense Tracker</title>
    
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Font Awesome -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" rel="stylesheet">
    <!-- Custom CSS -->
    <link href="/css/custom.css" rel="stylesheet">
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container">
            <a class="navbar-brand" href="/index.html">
                <i class="fas fa-wallet me-2"></i>Expense Tracker
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link active" href="/index.html">
                            <i class="fas fa-tachometer-alt me-1"></i>Dashboard
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/categories.html">
                            <i class="fas fa-tags me-1"></i>Categories
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/expenses.html">
                            <i class="fas fa-receipt me-1"></i>Expenses
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Alert Container -->
    <div class="container mt-3">
        <div id="alert-container"></div>
    </div>

    <!-- Main Content -->
    <main class="container mt-4 mb-5">
        <h1 class="mb-4"><i class="fas fa-tachometer-alt me-2"></i>Dashboard</h1>
        
        <!-- Summary Cards - Load on page load -->
        <div class="row mb-4" 
             hx-get="/api/expenses/summary" 
             hx-trigger="load"
             hx-target="#summary-cards"
             hx-swap="innerHTML">
            <div id="summary-cards">
                <div class="text-center py-4">
                    <div class="spinner-border text-primary" role="status">
                        <span class="visually-hidden">Loading...</span>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="row">
            <!-- Spending by Category Chart -->
            <div class="col-md-6 mb-4">
                <div class="card">
                    <div class="card-header">
                        <h5 class="mb-0"><i class="fas fa-chart-pie me-2"></i>Spending by Category</h5>
                    </div>
                    <div class="card-body">
                        <canvas id="categoryChart" height="300"></canvas>
                    </div>
                </div>
            </div>
            
            <!-- Recent Expenses -->
            <div class="col-md-6 mb-4">
                <div class="card">
                    <div class="card-header d-flex justify-content-between align-items-center">
                        <h5 class="mb-0"><i class="fas fa-clock me-2"></i>Recent Expenses</h5>
                        <a href="/expenses.html" class="btn btn-sm btn-primary">View All</a>
                    </div>
                    <div class="card-body"
                         hx-get="/api/expenses?size=5"
                         hx-trigger="load"
                         hx-target="#recent-expenses">
                        <div id="recent-expenses">
                            <div class="text-center py-4">
                                <div class="spinner-border text-primary" role="status"></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer class="bg-light py-3 mt-auto">
        <div class="container text-center text-muted">
            <small>&copy; 2024 Personal Expense Tracker | Built with Spring Boot + HTMX + Copilot</small>
        </div>
    </footer>

    <!-- JavaScript -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://unpkg.com/htmx.org@1.9.10"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
    <script src="/js/app.js"></script>
    
    <script>
        // Load dashboard data
        document.addEventListener('DOMContentLoaded', function() {
            loadDashboardData();
        });
        
        async function loadDashboardData() {
            // Load summary
            const summaryResponse = await fetch('/api/expenses/summary');
            const summary = await summaryResponse.json();
            
            document.getElementById('summary-cards').innerHTML = `
                <div class="col-md-3 mb-3">
                    <div class="card dashboard-card bg-primary text-white">
                        <div class="card-body">
                            <h6>Total Expenses</h6>
                            <h3>${summary.totalExpenses || 0}</h3>
                        </div>
                    </div>
                </div>
                <div class="col-md-3 mb-3">
                    <div class="card dashboard-card bg-success text-white">
                        <div class="card-body">
                            <h6>Total Amount</h6>
                            <h3>$${(summary.totalAmount || 0).toFixed(2)}</h3>
                        </div>
                    </div>
                </div>
                <div class="col-md-3 mb-3">
                    <div class="card dashboard-card bg-info text-white">
                        <div class="card-body">
                            <h6>Categories</h6>
                            <h3>${summary.categoryCount || 0}</h3>
                        </div>
                    </div>
                </div>
                <div class="col-md-3 mb-3">
                    <div class="card dashboard-card bg-warning text-dark">
                        <div class="card-body">
                            <h6>Average</h6>
                            <h3>$${(summary.averageExpense || 0).toFixed(2)}</h3>
                        </div>
                    </div>
                </div>
            `;
            
            // Load category chart
            const chartResponse = await fetch('/api/categories/spending');
            const chartData = await chartResponse.json();
            
            if (chartData.length > 0) {
                new Chart(document.getElementById('categoryChart'), {
                    type: 'pie',
                    data: {
                        labels: chartData.map(c => c.name),
                        datasets: [{
                            data: chartData.map(c => c.total),
                            backgroundColor: chartData.map(c => c.color || '#6c757d')
                        }]
                    },
                    options: {
                        responsive: true,
                        plugins: {
                            legend: { position: 'bottom' }
                        }
                    }
                });
            }
            
            // Load recent expenses
            const expensesResponse = await fetch('/api/expenses?size=5');
            const expensesData = await expensesResponse.json();
            const expenses = expensesData.content || expensesData;
            
            if (expenses.length > 0) {
                document.getElementById('recent-expenses').innerHTML = `
                    <table class="table table-hover">
                        <thead>
                            <tr><th>Description</th><th>Category</th><th>Amount</th></tr>
                        </thead>
                        <tbody>
                            ${expenses.map(e => `
                                <tr>
                                    <td>${e.description}</td>
                                    <td><span class="badge" style="background-color: ${e.categoryColor || '#6c757d'}">${e.categoryName}</span></td>
                                    <td class="fw-bold">$${e.amount.toFixed(2)}</td>
                                </tr>
                            `).join('')}
                        </tbody>
                    </table>
                `;
            } else {
                document.getElementById('recent-expenses').innerHTML = `
                    <div class="text-center py-4 text-muted">
                        <i class="fas fa-receipt fa-3x mb-3"></i>
                        <p>No expenses yet</p>
                    </div>
                `;
            }
        }
    </script>
</body>
</html>
```

---

## 📝 Step 3: Create Categories Page with HTMX (10 minutes)

### 🏷️ Categories Management Page

**Copilot Prompt:**

```text
/generate Create categories.html using HTMX and Bootstrap with:
- Table listing all categories from /api/categories
- Add Category button that opens a modal
- Edit/Delete buttons for each row
- HTMX for all CRUD operations without page reload
- Success/error alert messages
- Loading spinners
```

**Expected file**: `src/main/resources/static/categories.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Categories - Expense Tracker</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" rel="stylesheet">
    <link href="/css/custom.css" rel="stylesheet">
</head>
<body>
    <!-- Navigation (same as index.html) -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container">
            <a class="navbar-brand" href="/index.html">
                <i class="fas fa-wallet me-2"></i>Expense Tracker
            </a>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"><a class="nav-link" href="/index.html"><i class="fas fa-tachometer-alt me-1"></i>Dashboard</a></li>
                    <li class="nav-item"><a class="nav-link active" href="/categories.html"><i class="fas fa-tags me-1"></i>Categories</a></li>
                    <li class="nav-item"><a class="nav-link" href="/expenses.html"><i class="fas fa-receipt me-1"></i>Expenses</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Alert Container -->
    <div class="container mt-3">
        <div id="alert-container"></div>
    </div>

    <!-- Main Content -->
    <main class="container mt-4 mb-5">
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h1><i class="fas fa-tags me-2"></i>Categories</h1>
            <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#categoryModal" onclick="openAddModal()">
                <i class="fas fa-plus me-1"></i>Add Category
            </button>
        </div>
        
        <!-- Categories Table -->
        <div class="card">
            <div class="table-responsive">
                <table class="table table-hover mb-0">
                    <thead class="table-light">
                        <tr>
                            <th>Icon</th>
                            <th>Name</th>
                            <th>Description</th>
                            <th>Expenses</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody id="categories-table-body">
                        <tr>
                            <td colspan="5" class="text-center py-4">
                                <div class="spinner-border text-primary"></div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </main>

    <!-- Category Modal -->
    <div class="modal fade" id="categoryModal" tabindex="-1">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="modalTitle">Add Category</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                </div>
                <form id="categoryForm" onsubmit="saveCategory(event)">
                    <div class="modal-body">
                        <input type="hidden" id="categoryId">
                        
                        <div class="mb-3">
                            <label for="name" class="form-label">Name *</label>
                            <input type="text" class="form-control" id="name" required maxlength="100">
                        </div>
                        
                        <div class="mb-3">
                            <label for="description" class="form-label">Description</label>
                            <textarea class="form-control" id="description" rows="2" maxlength="255"></textarea>
                        </div>
                        
                        <div class="row">
                            <div class="col-md-6 mb-3">
                                <label for="icon" class="form-label">Icon</label>
                                <select class="form-select" id="icon">
                                    <option value="fas fa-folder">📁 Folder</option>
                                    <option value="fas fa-utensils">🍽️ Food</option>
                                    <option value="fas fa-car">🚗 Transport</option>
                                    <option value="fas fa-film">🎬 Entertainment</option>
                                    <option value="fas fa-shopping-bag">🛍️ Shopping</option>
                                    <option value="fas fa-file-invoice">📄 Bills</option>
                                    <option value="fas fa-medkit">🏥 Health</option>
                                    <option value="fas fa-plane">✈️ Travel</option>
                                </select>
                            </div>
                            <div class="col-md-6 mb-3">
                                <label for="color" class="form-label">Color</label>
                                <input type="color" class="form-control form-control-color w-100" id="color" value="#6c757d">
                            </div>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                        <button type="submit" class="btn btn-primary">
                            <i class="fas fa-save me-1"></i>Save
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>

    <!-- Scripts -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://unpkg.com/htmx.org@1.9.10"></script>
    
    <script>
        const API_BASE = '/api/categories';
        let categoryModal;
        
        document.addEventListener('DOMContentLoaded', function() {
            categoryModal = new bootstrap.Modal(document.getElementById('categoryModal'));
            loadCategories();
        });
        
        async function loadCategories() {
            try {
                const response = await fetch(API_BASE);
                const categories = await response.json();
                renderCategories(categories);
            } catch (error) {
                showAlert('Error loading categories', 'danger');
            }
        }
        
        function renderCategories(categories) {
            const tbody = document.getElementById('categories-table-body');
            
            if (categories.length === 0) {
                tbody.innerHTML = `
                    <tr>
                        <td colspan="5" class="text-center py-4 text-muted">
                            <i class="fas fa-folder-open fa-3x mb-3"></i>
                            <p>No categories yet. Create your first category!</p>
                        </td>
                    </tr>
                `;
                return;
            }
            
            tbody.innerHTML = categories.map(cat => `
                <tr>
                    <td>
                        <span class="badge rounded-pill" style="background-color: ${cat.color}; font-size: 1.2rem;">
                            <i class="${cat.icon}"></i>
                        </span>
                    </td>
                    <td class="fw-bold">${cat.name}</td>
                    <td>${cat.description || '-'}</td>
                    <td><span class="badge bg-secondary">${cat.expenseCount || 0} expenses</span></td>
                    <td>
                        <button class="btn btn-sm btn-outline-primary" onclick="openEditModal(${cat.id})">
                            <i class="fas fa-edit"></i>
                        </button>
                        <button class="btn btn-sm btn-outline-danger" onclick="deleteCategory(${cat.id}, '${cat.name}')">
                            <i class="fas fa-trash"></i>
                        </button>
                    </td>
                </tr>
            `).join('');
        }
        
        function openAddModal() {
            document.getElementById('modalTitle').textContent = 'Add Category';
            document.getElementById('categoryForm').reset();
            document.getElementById('categoryId').value = '';
            document.getElementById('color').value = '#6c757d';
        }
        
        async function openEditModal(id) {
            try {
                const response = await fetch(`${API_BASE}/${id}`);
                const category = await response.json();
                
                document.getElementById('modalTitle').textContent = 'Edit Category';
                document.getElementById('categoryId').value = category.id;
                document.getElementById('name').value = category.name;
                document.getElementById('description').value = category.description || '';
                document.getElementById('icon').value = category.icon;
                document.getElementById('color').value = category.color;
                
                categoryModal.show();
            } catch (error) {
                showAlert('Error loading category', 'danger');
            }
        }
        
        async function saveCategory(event) {
            event.preventDefault();
            
            const id = document.getElementById('categoryId').value;
            const data = {
                name: document.getElementById('name').value,
                description: document.getElementById('description').value,
                icon: document.getElementById('icon').value,
                color: document.getElementById('color').value
            };
            
            try {
                const url = id ? `${API_BASE}/${id}` : API_BASE;
                const method = id ? 'PUT' : 'POST';
                
                const response = await fetch(url, {
                    method: method,
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });
                
                if (response.ok) {
                    categoryModal.hide();
                    loadCategories();
                    showAlert(`Category ${id ? 'updated' : 'created'} successfully`, 'success');
                } else {
                    const error = await response.json();
                    showAlert(error.message || 'Error saving category', 'danger');
                }
            } catch (error) {
                showAlert('Error saving category', 'danger');
            }
        }
        
        async function deleteCategory(id, name) {
            if (!confirm(`Delete category "${name}"?`)) return;
            
            try {
                const response = await fetch(`${API_BASE}/${id}`, { method: 'DELETE' });
                
                if (response.ok) {
                    loadCategories();
                    showAlert('Category deleted successfully', 'success');
                } else {
                    showAlert('Error deleting category', 'danger');
                }
            } catch (error) {
                showAlert('Error deleting category', 'danger');
            }
        }
        
        function showAlert(message, type) {
            const container = document.getElementById('alert-container');
            container.innerHTML = `
                <div class="alert alert-${type} alert-dismissible fade show">
                    ${message}
                    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                </div>
            `;
            setTimeout(() => container.innerHTML = '', 5000);
        }
    </script>
</body>
</html>
```

---

## 📝 Step 4: Create Expenses Page (10 minutes)

### 💰 Expenses Management Page

**Copilot Prompt:**

```text
/generate Create expenses.html using JavaScript fetch API with:
- Table listing expenses with filtering by category
- Search by description
- Add/Edit expense modal with category dropdown
- Delete with confirmation
- Date picker for expense date
- Amount input with currency formatting
```

**Expected file**: `src/main/resources/static/expenses.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Expenses - Expense Tracker</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" rel="stylesheet">
    <link href="/css/custom.css" rel="stylesheet">
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container">
            <a class="navbar-brand" href="/index.html">
                <i class="fas fa-wallet me-2"></i>Expense Tracker
            </a>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"><a class="nav-link" href="/index.html"><i class="fas fa-tachometer-alt me-1"></i>Dashboard</a></li>
                    <li class="nav-item"><a class="nav-link" href="/categories.html"><i class="fas fa-tags me-1"></i>Categories</a></li>
                    <li class="nav-item"><a class="nav-link active" href="/expenses.html"><i class="fas fa-receipt me-1"></i>Expenses</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Alert Container -->
    <div class="container mt-3">
        <div id="alert-container"></div>
    </div>

    <!-- Main Content -->
    <main class="container mt-4 mb-5">
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h1><i class="fas fa-receipt me-2"></i>Expenses</h1>
            <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#expenseModal" onclick="openAddModal()">
                <i class="fas fa-plus me-1"></i>Add Expense
            </button>
        </div>
        
        <!-- Filters -->
        <div class="card mb-4">
            <div class="card-body">
                <div class="row g-3 align-items-end">
                    <div class="col-md-4">
                        <label class="form-label">Category</label>
                        <select class="form-select" id="filterCategory" onchange="loadExpenses()">
                            <option value="">All Categories</option>
                        </select>
                    </div>
                    <div class="col-md-4">
                        <label class="form-label">Search</label>
                        <input type="text" class="form-control" id="filterSearch" placeholder="Search description..." oninput="debounceSearch()">
                    </div>
                    <div class="col-md-4">
                        <button class="btn btn-secondary w-100" onclick="clearFilters()">
                            <i class="fas fa-times me-1"></i>Clear Filters
                        </button>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Expenses Table -->
        <div class="card">
            <div class="table-responsive">
                <table class="table table-hover mb-0">
                    <thead class="table-light">
                        <tr>
                            <th>Date</th>
                            <th>Description</th>
                            <th>Category</th>
                            <th>Amount</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody id="expenses-table-body">
                        <tr>
                            <td colspan="5" class="text-center py-4">
                                <div class="spinner-border text-primary"></div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </main>

    <!-- Expense Modal -->
    <div class="modal fade" id="expenseModal" tabindex="-1">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="expenseModalTitle">Add Expense</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                </div>
                <form id="expenseForm" onsubmit="saveExpense(event)">
                    <div class="modal-body">
                        <input type="hidden" id="expenseId">
                        
                        <div class="mb-3">
                            <label for="description" class="form-label">Description *</label>
                            <input type="text" class="form-control" id="expenseDescription" required maxlength="255">
                        </div>
                        
                        <div class="row">
                            <div class="col-md-6 mb-3">
                                <label for="amount" class="form-label">Amount *</label>
                                <div class="input-group">
                                    <span class="input-group-text">$</span>
                                    <input type="number" class="form-control" id="amount" step="0.01" min="0.01" required>
                                </div>
                            </div>
                            <div class="col-md-6 mb-3">
                                <label for="expenseDate" class="form-label">Date *</label>
                                <input type="date" class="form-control" id="expenseDate" required>
                            </div>
                        </div>
                        
                        <div class="mb-3">
                            <label for="categoryId" class="form-label">Category *</label>
                            <select class="form-select" id="categoryId" required>
                                <option value="">Select a category</option>
                            </select>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                        <button type="submit" class="btn btn-primary">
                            <i class="fas fa-save me-1"></i>Save
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>

    <!-- Scripts -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    
    <script>
        const EXPENSE_API = '/api/expenses';
        const CATEGORY_API = '/api/categories';
        let expenseModal;
        let categories = [];
        let searchTimeout;
        
        document.addEventListener('DOMContentLoaded', function() {
            expenseModal = new bootstrap.Modal(document.getElementById('expenseModal'));
            document.getElementById('expenseDate').value = new Date().toISOString().split('T')[0];
            loadCategories();
            loadExpenses();
        });
        
        async function loadCategories() {
            try {
                const response = await fetch(CATEGORY_API);
                categories = await response.json();
                
                const filterSelect = document.getElementById('filterCategory');
                const formSelect = document.getElementById('categoryId');
                
                categories.forEach(cat => {
                    filterSelect.innerHTML += `<option value="${cat.id}">${cat.name}</option>`;
                    formSelect.innerHTML += `<option value="${cat.id}">${cat.name}</option>`;
                });
            } catch (error) {
                console.error('Error loading categories:', error);
            }
        }
        
        async function loadExpenses() {
            const categoryId = document.getElementById('filterCategory').value;
            const search = document.getElementById('filterSearch').value;
            
            let url = EXPENSE_API;
            const params = new URLSearchParams();
            if (categoryId) params.append('categoryId', categoryId);
            if (search) params.append('search', search);
            if (params.toString()) url += '?' + params.toString();
            
            try {
                const response = await fetch(url);
                const data = await response.json();
                const expenses = data.content || data;
                renderExpenses(expenses);
            } catch (error) {
                showAlert('Error loading expenses', 'danger');
            }
        }
        
        function renderExpenses(expenses) {
            const tbody = document.getElementById('expenses-table-body');
            
            if (expenses.length === 0) {
                tbody.innerHTML = `
                    <tr>
                        <td colspan="5" class="text-center py-4 text-muted">
                            <i class="fas fa-receipt fa-3x mb-3"></i>
                            <p>No expenses found</p>
                        </td>
                    </tr>
                `;
                return;
            }
            
            tbody.innerHTML = expenses.map(exp => `
                <tr>
                    <td>${new Date(exp.expenseDate).toLocaleDateString()}</td>
                    <td>${exp.description}</td>
                    <td>
                        <span class="badge" style="background-color: ${exp.categoryColor || '#6c757d'}">
                            <i class="${exp.categoryIcon || 'fas fa-folder'} me-1"></i>
                            ${exp.categoryName}
                        </span>
                    </td>
                    <td class="fw-bold text-success">$${exp.amount.toFixed(2)}</td>
                    <td>
                        <button class="btn btn-sm btn-outline-primary" onclick="openEditModal(${exp.id})">
                            <i class="fas fa-edit"></i>
                        </button>
                        <button class="btn btn-sm btn-outline-danger" onclick="deleteExpense(${exp.id})">
                            <i class="fas fa-trash"></i>
                        </button>
                    </td>
                </tr>
            `).join('');
        }
        
        function debounceSearch() {
            clearTimeout(searchTimeout);
            searchTimeout = setTimeout(loadExpenses, 300);
        }
        
        function clearFilters() {
            document.getElementById('filterCategory').value = '';
            document.getElementById('filterSearch').value = '';
            loadExpenses();
        }
        
        function openAddModal() {
            document.getElementById('expenseModalTitle').textContent = 'Add Expense';
            document.getElementById('expenseForm').reset();
            document.getElementById('expenseId').value = '';
            document.getElementById('expenseDate').value = new Date().toISOString().split('T')[0];
        }
        
        async function openEditModal(id) {
            try {
                const response = await fetch(`${EXPENSE_API}/${id}`);
                const expense = await response.json();
                
                document.getElementById('expenseModalTitle').textContent = 'Edit Expense';
                document.getElementById('expenseId').value = expense.id;
                document.getElementById('expenseDescription').value = expense.description;
                document.getElementById('amount').value = expense.amount;
                document.getElementById('expenseDate').value = expense.expenseDate;
                document.getElementById('categoryId').value = expense.categoryId;
                
                expenseModal.show();
            } catch (error) {
                showAlert('Error loading expense', 'danger');
            }
        }
        
        async function saveExpense(event) {
            event.preventDefault();
            
            const id = document.getElementById('expenseId').value;
            const data = {
                description: document.getElementById('expenseDescription').value,
                amount: parseFloat(document.getElementById('amount').value),
                expenseDate: document.getElementById('expenseDate').value,
                categoryId: parseInt(document.getElementById('categoryId').value)
            };
            
            try {
                const url = id ? `${EXPENSE_API}/${id}` : EXPENSE_API;
                const method = id ? 'PUT' : 'POST';
                
                const response = await fetch(url, {
                    method: method,
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });
                
                if (response.ok) {
                    expenseModal.hide();
                    loadExpenses();
                    showAlert(`Expense ${id ? 'updated' : 'created'} successfully`, 'success');
                } else {
                    const error = await response.json();
                    showAlert(error.message || 'Error saving expense', 'danger');
                }
            } catch (error) {
                showAlert('Error saving expense', 'danger');
            }
        }
        
        async function deleteExpense(id) {
            if (!confirm('Delete this expense?')) return;
            
            try {
                const response = await fetch(`${EXPENSE_API}/${id}`, { method: 'DELETE' });
                
                if (response.ok) {
                    loadExpenses();
                    showAlert('Expense deleted successfully', 'success');
                } else {
                    showAlert('Error deleting expense', 'danger');
                }
            } catch (error) {
                showAlert('Error deleting expense', 'danger');
            }
        }
        
        function showAlert(message, type) {
            const container = document.getElementById('alert-container');
            container.innerHTML = `
                <div class="alert alert-${type} alert-dismissible fade show">
                    ${message}
                    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                </div>
            `;
            setTimeout(() => container.innerHTML = '', 5000);
        }
    </script>
</body>
</html>
```

---

## 📝 Step 5: Create CSS File (3 minutes)

**Expected file**: `src/main/resources/static/css/custom.css`

```css
/* Custom Color Scheme */
:root {
    --primary-color: #4A90E2;
    --success-color: #7ED321;
    --danger-color: #D0021B;
}

/* Dashboard Cards */
.dashboard-card {
    border: none;
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: transform 0.2s;
}

.dashboard-card:hover {
    transform: translateY(-2px);
}

/* Table Styling */
.table th {
    font-weight: 600;
    text-transform: uppercase;
    font-size: 0.8rem;
    letter-spacing: 0.5px;
}

/* Empty State */
.empty-state {
    padding: 3rem;
    text-align: center;
}

.empty-state i {
    font-size: 3rem;
    color: #dee2e6;
    margin-bottom: 1rem;
}

/* Form Controls */
.form-control-color {
    height: 38px;
}
```

---

## 📝 Step 6: Testing & Verification (5 minutes)

### ✅ Test the Application

```bash
# Start Spring Boot application
./mvnw spring-boot:run

# Open browser
open http://localhost:8080/index.html
```

### 🔍 Verification Checklist

- [ ] Dashboard loads with summary cards and chart
- [ ] Categories page shows list from API
- [ ] Add/Edit/Delete categories works
- [ ] Expenses page shows list with filtering
- [ ] Add/Edit/Delete expenses works
- [ ] Navigation between pages works

---

## 🎉 Session 4a Deliverables

### ✅ What You've Accomplished

- **✅ Static HTML Pages** - No template engine configuration needed
- **✅ HTMX/Fetch API** - Dynamic data loading from REST APIs
- **✅ Full CRUD Operations** - Without page reloads
- **✅ Bootstrap 5 UI** - Professional responsive design
- **✅ Chart.js Integration** - Data visualization

### 🆚 Comparison: Thymeleaf vs HTMX Approach

| Aspect | Thymeleaf | HTMX/Static HTML |
|--------|-----------|------------------|
| Setup | Template resolver config | Just add script tag |
| Server Rendering | Yes | No (client-side) |
| SEO | Better | Requires SSR |
| Complexity | Higher | Lower |
| Debugging | IDE support | Browser DevTools |
| Learning Curve | Steeper | Gentler |

---

## 💡 GitHub Copilot Tips for HTMX

### 🎯 Effective Prompts

```text
/generate Create HTML page using HTMX that calls [REST endpoint]
"Add HTMX attributes to load data from /api/categories on page load"
"Create JavaScript function to handle CRUD with fetch API"
```

### 🤖 Recommended Model

**Claude 3.5 Sonnet** or **GPT-4o** work best for:
- HTML/CSS/JavaScript generation
- HTMX attribute suggestions
- Bootstrap component layouts
- fetch API patterns

---

## 🎊 Alternative Complete!

You now have a fully functional web interface using HTMX instead of Thymeleaf. This approach:

- ✅ Requires no server-side template configuration
- ✅ Leverages your existing REST APIs
- ✅ Provides modern, responsive UI
- ✅ Is easier to debug with browser DevTools
