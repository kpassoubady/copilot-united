# 🎨 Day 1 - Session 4c: Personal Expense Tracker - Web Interface with React (Alternative)

## ⚠️ When to Use This Alternative

Use this guide if:
- Thymeleaf configuration is causing issues
- You prefer a **modern SPA (Single Page Application)** approach
- You want to learn React alongside Spring Boot
- You're comfortable with JavaScript/TypeScript

**React** is a popular JavaScript library for building user interfaces with a component-based architecture.

---

## 🎯 Learning Objectives

By the end of this session, you will:

- Create a React frontend that consumes your REST APIs
- Build reusable UI components with hooks
- Implement CRUD operations with fetch/axios
- Use modern React patterns (functional components, hooks)
- Master GitHub Copilot for React code generation

**⏱️ Time Allocation: 45 minutes**

---

## 📋 Prerequisites Check (2 minutes)

- ✅ Session 3 completed (REST APIs working)
- ✅ Node.js 18+ installed (`node --version`)
- ✅ All REST endpoints tested (`/api/categories`, `/api/expenses`)

**Quick Test**:

```bash
node --version    # Should be 18+
npm --version     # Should be 9+
curl http://localhost:8080/api/categories
```

---

## 🚀 Project Structure

We'll create a separate React frontend that communicates with your Spring Boot backend:

```
expense-tracker/
├── backend/          # Your existing Spring Boot app (port 8080)
└── frontend/         # New React app (port 3000)
    ├── src/
    │   ├── components/
    │   ├── pages/
    │   ├── services/
    │   └── App.jsx
    └── package.json
```

---

## 📝 Step 1: Create React Project (5 minutes)

### 🛠️ Initialize with Vite

```bash
# Create React project with Vite (faster than create-react-app)
npm create vite@latest frontend -- --template react

cd frontend
npm install

# Install dependencies
npm install axios react-router-dom chart.js react-chartjs-2 bootstrap
```

### 🔧 Configure Proxy for API Calls

Create `vite.config.js`:

```javascript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    proxy: {
      '/api': {
        target: 'http://localhost:8080',
        changeOrigin: true
      }
    }
  }
})
```

---

## 📝 Step 2: Create API Service Layer (5 minutes)

### 📡 API Service

**Copilot Prompt:**

```text
/generate Create a React API service using axios with:
- Base URL configuration for /api
- Category CRUD methods: getAll, getById, create, update, delete
- Expense CRUD methods: getAll, getById, create, update, delete, getByCategory
- Error handling with try-catch
- Export as named functions
```

**Expected file**: `src/services/api.js`

```javascript
import axios from 'axios';

const API_BASE = '/api';

// Configure axios defaults
const api = axios.create({
  baseURL: API_BASE,
  headers: {
    'Content-Type': 'application/json'
  }
});

// ============== Categories ==============

export const categoryService = {
  async getAll() {
    const response = await api.get('/categories');
    return response.data;
  },

  async getById(id) {
    const response = await api.get(`/categories/${id}`);
    return response.data;
  },

  async create(category) {
    const response = await api.post('/categories', category);
    return response.data;
  },

  async update(id, category) {
    const response = await api.put(`/categories/${id}`, category);
    return response.data;
  },

  async delete(id) {
    await api.delete(`/categories/${id}`);
  },

  async getSpending() {
    const response = await api.get('/categories/spending');
    return response.data;
  }
};

// ============== Expenses ==============

export const expenseService = {
  async getAll(params = {}) {
    const response = await api.get('/expenses', { params });
    return response.data;
  },

  async getById(id) {
    const response = await api.get(`/expenses/${id}`);
    return response.data;
  },

  async create(expense) {
    const response = await api.post('/expenses', expense);
    return response.data;
  },

  async update(id, expense) {
    const response = await api.put(`/expenses/${id}`, expense);
    return response.data;
  },

  async delete(id) {
    await api.delete(`/expenses/${id}`);
  },

  async getByCategory(categoryId) {
    const response = await api.get(`/expenses/category/${categoryId}`);
    return response.data;
  },

  async getSummary() {
    const response = await api.get('/expenses/summary');
    return response.data;
  }
};

export default api;
```

---

## 📝 Step 3: Create Layout Components (5 minutes)

### 🏠 Main Layout with Navigation

**Copilot Prompt:**

```text
/generate Create a React Layout component with:
- Bootstrap navbar with brand "Expense Tracker"
- Navigation links: Dashboard, Categories, Expenses
- React Router NavLink with active styling
- Footer with copyright
- Outlet for child routes
```

**Expected file**: `src/components/Layout.jsx`

```jsx
import { NavLink, Outlet } from 'react-router-dom';

function Layout() {
  return (
    <div className="d-flex flex-column min-vh-100">
      {/* Navigation */}
      <nav className="navbar navbar-expand-lg navbar-dark bg-primary">
        <div className="container">
          <NavLink className="navbar-brand" to="/">
            <i className="fas fa-wallet me-2"></i>
            Expense Tracker
          </NavLink>
          
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span className="navbar-toggler-icon"></span>
          </button>
          
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav ms-auto">
              <li className="nav-item">
                <NavLink className="nav-link" to="/">
                  <i className="fas fa-tachometer-alt me-1"></i>Dashboard
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" to="/categories">
                  <i className="fas fa-tags me-1"></i>Categories
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" to="/expenses">
                  <i className="fas fa-receipt me-1"></i>Expenses
                </NavLink>
              </li>
            </ul>
          </div>
        </div>
      </nav>

      {/* Alert Container */}
      <div className="container mt-3">
        <div id="alert-container"></div>
      </div>

      {/* Main Content */}
      <main className="container mt-4 mb-5 flex-grow-1">
        <Outlet />
      </main>

      {/* Footer */}
      <footer className="bg-light py-3 mt-auto">
        <div className="container text-center text-muted">
          <small>&copy; 2024 Personal Expense Tracker | Built with Spring Boot + React + Copilot</small>
        </div>
      </footer>
    </div>
  );
}

export default Layout;
```

---

## 📝 Step 4: Create Dashboard Page (10 minutes)

### 📊 Dashboard with Charts

**Copilot Prompt:**

```text
/generate Create a React Dashboard component with:
- useState and useEffect hooks to load data
- Summary cards: total expenses, total amount, categories, average
- Pie chart using react-chartjs-2 for spending by category
- Recent expenses table
- Loading spinner while fetching
- Error handling with try-catch
```

**Expected file**: `src/pages/Dashboard.jsx`

```jsx
import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { Pie } from 'react-chartjs-2';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
import { expenseService, categoryService } from '../services/api';

ChartJS.register(ArcElement, Tooltip, Legend);

function Dashboard() {
  const [summary, setSummary] = useState(null);
  const [recentExpenses, setRecentExpenses] = useState([]);
  const [spendingData, setSpendingData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    loadDashboardData();
  }, []);

  const loadDashboardData = async () => {
    try {
      setLoading(true);
      const [summaryRes, expensesRes, spendingRes] = await Promise.all([
        expenseService.getSummary(),
        expenseService.getAll({ size: 5 }),
        categoryService.getSpending()
      ]);
      
      setSummary(summaryRes);
      setRecentExpenses(expensesRes.content || expensesRes);
      setSpendingData(spendingRes);
    } catch (err) {
      setError('Failed to load dashboard data');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const chartData = {
    labels: spendingData.map(c => c.name),
    datasets: [{
      data: spendingData.map(c => c.total),
      backgroundColor: spendingData.map(c => c.color || '#6c757d'),
      borderWidth: 2,
      borderColor: '#fff'
    }]
  };

  if (loading) {
    return (
      <div className="text-center py-5">
        <div className="spinner-border text-primary" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
      </div>
    );
  }

  if (error) {
    return <div className="alert alert-danger">{error}</div>;
  }

  return (
    <div>
      <h1 className="mb-4">
        <i className="fas fa-tachometer-alt me-2"></i>Dashboard
      </h1>

      {/* Summary Cards */}
      <div className="row mb-4">
        <div className="col-md-3 mb-3">
          <div className="card bg-primary text-white h-100">
            <div className="card-body">
              <h6 className="card-subtitle mb-1">Total Expenses</h6>
              <h3 className="card-title mb-0">{summary?.totalExpenses || 0}</h3>
            </div>
          </div>
        </div>
        
        <div className="col-md-3 mb-3">
          <div className="card bg-success text-white h-100">
            <div className="card-body">
              <h6 className="card-subtitle mb-1">Total Amount</h6>
              <h3 className="card-title mb-0">${(summary?.totalAmount || 0).toFixed(2)}</h3>
            </div>
          </div>
        </div>
        
        <div className="col-md-3 mb-3">
          <div className="card bg-info text-white h-100">
            <div className="card-body">
              <h6 className="card-subtitle mb-1">Categories</h6>
              <h3 className="card-title mb-0">{summary?.categoryCount || 0}</h3>
            </div>
          </div>
        </div>
        
        <div className="col-md-3 mb-3">
          <div className="card bg-warning text-dark h-100">
            <div className="card-body">
              <h6 className="card-subtitle mb-1">Average</h6>
              <h3 className="card-title mb-0">${(summary?.averageExpense || 0).toFixed(2)}</h3>
            </div>
          </div>
        </div>
      </div>

      <div className="row">
        {/* Chart */}
        <div className="col-md-6 mb-4">
          <div className="card h-100">
            <div className="card-header">
              <h5 className="mb-0">
                <i className="fas fa-chart-pie me-2"></i>Spending by Category
              </h5>
            </div>
            <div className="card-body">
              {spendingData.length > 0 ? (
                <Pie data={chartData} options={{ 
                  responsive: true,
                  plugins: { legend: { position: 'bottom' } }
                }} />
              ) : (
                <p className="text-muted text-center">No data available</p>
              )}
            </div>
          </div>
        </div>

        {/* Recent Expenses */}
        <div className="col-md-6 mb-4">
          <div className="card h-100">
            <div className="card-header d-flex justify-content-between align-items-center">
              <h5 className="mb-0">
                <i className="fas fa-clock me-2"></i>Recent Expenses
              </h5>
              <Link to="/expenses" className="btn btn-sm btn-primary">View All</Link>
            </div>
            <div className="card-body">
              {recentExpenses.length > 0 ? (
                <table className="table table-hover">
                  <thead>
                    <tr>
                      <th>Description</th>
                      <th>Category</th>
                      <th>Amount</th>
                    </tr>
                  </thead>
                  <tbody>
                    {recentExpenses.map(expense => (
                      <tr key={expense.id}>
                        <td>{expense.description}</td>
                        <td>
                          <span 
                            className="badge" 
                            style={{ backgroundColor: expense.categoryColor || '#6c757d' }}
                          >
                            {expense.categoryName}
                          </span>
                        </td>
                        <td className="fw-bold">${expense.amount.toFixed(2)}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              ) : (
                <p className="text-muted text-center">No expenses yet</p>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
```

---

## 📝 Step 5: Create Categories Page (10 minutes)

### 🏷️ Category Management

**Copilot Prompt:**

```text
/generate Create a React Categories component with:
- useState for categories list, modal state, form data
- useEffect to load categories on mount
- Table with icon, name, description, expense count, actions
- Bootstrap modal for add/edit form
- Form fields: name, description, icon (select), color (input type color)
- handleSubmit for create/update
- handleDelete with confirmation
- Loading and error states
```

**Expected file**: `src/pages/Categories.jsx`

```jsx
import { useState, useEffect } from 'react';
import { categoryService } from '../services/api';

const ICON_OPTIONS = [
  { value: 'fas fa-folder', label: '📁 Folder' },
  { value: 'fas fa-utensils', label: '🍽️ Food' },
  { value: 'fas fa-car', label: '🚗 Transport' },
  { value: 'fas fa-film', label: '🎬 Entertainment' },
  { value: 'fas fa-shopping-bag', label: '🛍️ Shopping' },
  { value: 'fas fa-file-invoice', label: '📄 Bills' },
  { value: 'fas fa-medkit', label: '🏥 Health' },
  { value: 'fas fa-plane', label: '✈️ Travel' },
];

function Categories() {
  const [categories, setCategories] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showModal, setShowModal] = useState(false);
  const [editingCategory, setEditingCategory] = useState(null);
  const [formData, setFormData] = useState({
    name: '', description: '', icon: 'fas fa-folder', color: '#6c757d'
  });
  const [message, setMessage] = useState(null);

  useEffect(() => {
    loadCategories();
  }, []);

  const loadCategories = async () => {
    try {
      setLoading(true);
      const data = await categoryService.getAll();
      setCategories(data);
    } catch (err) {
      showMessage('Error loading categories', 'danger');
    } finally {
      setLoading(false);
    }
  };

  const showMessage = (text, type) => {
    setMessage({ text, type });
    setTimeout(() => setMessage(null), 5000);
  };

  const openAddModal = () => {
    setEditingCategory(null);
    setFormData({ name: '', description: '', icon: 'fas fa-folder', color: '#6c757d' });
    setShowModal(true);
  };

  const openEditModal = (category) => {
    setEditingCategory(category);
    setFormData({
      name: category.name,
      description: category.description || '',
      icon: category.icon,
      color: category.color
    });
    setShowModal(true);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (editingCategory) {
        await categoryService.update(editingCategory.id, formData);
        showMessage('Category updated successfully', 'success');
      } else {
        await categoryService.create(formData);
        showMessage('Category created successfully', 'success');
      }
      setShowModal(false);
      loadCategories();
    } catch (err) {
      showMessage(err.response?.data?.message || 'Error saving category', 'danger');
    }
  };

  const handleDelete = async (category) => {
    if (!window.confirm(`Delete "${category.name}"?`)) return;
    
    try {
      await categoryService.delete(category.id);
      showMessage('Category deleted successfully', 'success');
      loadCategories();
    } catch (err) {
      showMessage('Error deleting category', 'danger');
    }
  };

  if (loading) {
    return (
      <div className="text-center py-5">
        <div className="spinner-border text-primary"></div>
      </div>
    );
  }

  return (
    <div>
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h1><i className="fas fa-tags me-2"></i>Categories</h1>
        <button className="btn btn-primary" onClick={openAddModal}>
          <i className="fas fa-plus me-1"></i>Add Category
        </button>
      </div>

      {message && (
        <div className={`alert alert-${message.type} alert-dismissible fade show`}>
          {message.text}
          <button type="button" className="btn-close" onClick={() => setMessage(null)}></button>
        </div>
      )}

      <div className="card">
        <div className="table-responsive">
          <table className="table table-hover mb-0">
            <thead className="table-light">
              <tr>
                <th>Icon</th>
                <th>Name</th>
                <th>Description</th>
                <th>Expenses</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {categories.length === 0 ? (
                <tr>
                  <td colSpan="5" className="text-center py-4 text-muted">
                    No categories yet. Create your first category!
                  </td>
                </tr>
              ) : (
                categories.map(cat => (
                  <tr key={cat.id}>
                    <td>
                      <span 
                        className="badge rounded-pill" 
                        style={{ backgroundColor: cat.color, fontSize: '1.2rem' }}
                      >
                        <i className={cat.icon}></i>
                      </span>
                    </td>
                    <td className="fw-bold">{cat.name}</td>
                    <td>{cat.description || '-'}</td>
                    <td>
                      <span className="badge bg-secondary">
                        {cat.expenseCount || 0} expenses
                      </span>
                    </td>
                    <td>
                      <button 
                        className="btn btn-sm btn-outline-primary me-1"
                        onClick={() => openEditModal(cat)}
                      >
                        <i className="fas fa-edit"></i>
                      </button>
                      <button 
                        className="btn btn-sm btn-outline-danger"
                        onClick={() => handleDelete(cat)}
                      >
                        <i className="fas fa-trash"></i>
                      </button>
                    </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>

      {/* Modal */}
      {showModal && (
        <div className="modal show d-block" style={{ backgroundColor: 'rgba(0,0,0,0.5)' }}>
          <div className="modal-dialog">
            <div className="modal-content">
              <div className="modal-header">
                <h5 className="modal-title">
                  {editingCategory ? 'Edit Category' : 'Add Category'}
                </h5>
                <button type="button" className="btn-close" onClick={() => setShowModal(false)}></button>
              </div>
              <form onSubmit={handleSubmit}>
                <div className="modal-body">
                  <div className="mb-3">
                    <label className="form-label">Name *</label>
                    <input 
                      type="text" 
                      className="form-control"
                      value={formData.name}
                      onChange={e => setFormData({...formData, name: e.target.value})}
                      required 
                      maxLength={100}
                    />
                  </div>
                  <div className="mb-3">
                    <label className="form-label">Description</label>
                    <textarea 
                      className="form-control"
                      value={formData.description}
                      onChange={e => setFormData({...formData, description: e.target.value})}
                      rows={2}
                      maxLength={255}
                    />
                  </div>
                  <div className="row">
                    <div className="col-md-6 mb-3">
                      <label className="form-label">Icon</label>
                      <select 
                        className="form-select"
                        value={formData.icon}
                        onChange={e => setFormData({...formData, icon: e.target.value})}
                      >
                        {ICON_OPTIONS.map(opt => (
                          <option key={opt.value} value={opt.value}>{opt.label}</option>
                        ))}
                      </select>
                    </div>
                    <div className="col-md-6 mb-3">
                      <label className="form-label">Color</label>
                      <input 
                        type="color" 
                        className="form-control form-control-color w-100"
                        value={formData.color}
                        onChange={e => setFormData({...formData, color: e.target.value})}
                      />
                    </div>
                  </div>
                </div>
                <div className="modal-footer">
                  <button type="button" className="btn btn-secondary" onClick={() => setShowModal(false)}>
                    Cancel
                  </button>
                  <button type="submit" className="btn btn-primary">
                    <i className="fas fa-save me-1"></i>Save
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default Categories;
```

---

## 📝 Step 6: Create Expenses Page (8 minutes)

### 💰 Expense Management

**Expected file**: `src/pages/Expenses.jsx`

```jsx
import { useState, useEffect } from 'react';
import { expenseService, categoryService } from '../services/api';

function Expenses() {
  const [expenses, setExpenses] = useState([]);
  const [categories, setCategories] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showModal, setShowModal] = useState(false);
  const [editingExpense, setEditingExpense] = useState(null);
  const [filterCategory, setFilterCategory] = useState('');
  const [formData, setFormData] = useState({
    description: '', amount: '', expenseDate: new Date().toISOString().split('T')[0], categoryId: ''
  });
  const [message, setMessage] = useState(null);

  useEffect(() => {
    loadData();
  }, []);

  useEffect(() => {
    loadExpenses();
  }, [filterCategory]);

  const loadData = async () => {
    try {
      const cats = await categoryService.getAll();
      setCategories(cats);
      await loadExpenses();
    } catch (err) {
      showMessage('Error loading data', 'danger');
    }
  };

  const loadExpenses = async () => {
    try {
      setLoading(true);
      let data;
      if (filterCategory) {
        data = await expenseService.getByCategory(filterCategory);
      } else {
        data = await expenseService.getAll();
      }
      setExpenses(data.content || data);
    } catch (err) {
      showMessage('Error loading expenses', 'danger');
    } finally {
      setLoading(false);
    }
  };

  const showMessage = (text, type) => {
    setMessage({ text, type });
    setTimeout(() => setMessage(null), 5000);
  };

  const openAddModal = () => {
    setEditingExpense(null);
    setFormData({
      description: '', amount: '', 
      expenseDate: new Date().toISOString().split('T')[0], 
      categoryId: categories[0]?.id || ''
    });
    setShowModal(true);
  };

  const openEditModal = (expense) => {
    setEditingExpense(expense);
    setFormData({
      description: expense.description,
      amount: expense.amount,
      expenseDate: expense.expenseDate,
      categoryId: expense.categoryId
    });
    setShowModal(true);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = { ...formData, amount: parseFloat(formData.amount), categoryId: parseInt(formData.categoryId) };
    
    try {
      if (editingExpense) {
        await expenseService.update(editingExpense.id, data);
        showMessage('Expense updated successfully', 'success');
      } else {
        await expenseService.create(data);
        showMessage('Expense created successfully', 'success');
      }
      setShowModal(false);
      loadExpenses();
    } catch (err) {
      showMessage(err.response?.data?.message || 'Error saving expense', 'danger');
    }
  };

  const handleDelete = async (expense) => {
    if (!window.confirm('Delete this expense?')) return;
    
    try {
      await expenseService.delete(expense.id);
      showMessage('Expense deleted successfully', 'success');
      loadExpenses();
    } catch (err) {
      showMessage('Error deleting expense', 'danger');
    }
  };

  return (
    <div>
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h1><i className="fas fa-receipt me-2"></i>Expenses</h1>
        <button className="btn btn-primary" onClick={openAddModal}>
          <i className="fas fa-plus me-1"></i>Add Expense
        </button>
      </div>

      {message && (
        <div className={`alert alert-${message.type} alert-dismissible fade show`}>
          {message.text}
          <button type="button" className="btn-close" onClick={() => setMessage(null)}></button>
        </div>
      )}

      {/* Filter */}
      <div className="card mb-4">
        <div className="card-body">
          <div className="row align-items-end">
            <div className="col-md-4">
              <label className="form-label">Filter by Category</label>
              <select 
                className="form-select"
                value={filterCategory}
                onChange={e => setFilterCategory(e.target.value)}
              >
                <option value="">All Categories</option>
                {categories.map(cat => (
                  <option key={cat.id} value={cat.id}>{cat.name}</option>
                ))}
              </select>
            </div>
            <div className="col-md-4">
              <button className="btn btn-secondary" onClick={() => setFilterCategory('')}>
                Clear Filter
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* Table */}
      <div className="card">
        <div className="table-responsive">
          <table className="table table-hover mb-0">
            <thead className="table-light">
              <tr>
                <th>Date</th>
                <th>Description</th>
                <th>Category</th>
                <th>Amount</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {loading ? (
                <tr><td colSpan="5" className="text-center py-4"><div className="spinner-border text-primary"></div></td></tr>
              ) : expenses.length === 0 ? (
                <tr><td colSpan="5" className="text-center py-4 text-muted">No expenses found</td></tr>
              ) : (
                expenses.map(exp => (
                  <tr key={exp.id}>
                    <td>{new Date(exp.expenseDate).toLocaleDateString()}</td>
                    <td>{exp.description}</td>
                    <td>
                      <span className="badge" style={{ backgroundColor: exp.categoryColor || '#6c757d' }}>
                        {exp.categoryName}
                      </span>
                    </td>
                    <td className="fw-bold text-success">${exp.amount.toFixed(2)}</td>
                    <td>
                      <button className="btn btn-sm btn-outline-primary me-1" onClick={() => openEditModal(exp)}>
                        <i className="fas fa-edit"></i>
                      </button>
                      <button className="btn btn-sm btn-outline-danger" onClick={() => handleDelete(exp)}>
                        <i className="fas fa-trash"></i>
                      </button>
                    </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>

      {/* Modal */}
      {showModal && (
        <div className="modal show d-block" style={{ backgroundColor: 'rgba(0,0,0,0.5)' }}>
          <div className="modal-dialog">
            <div className="modal-content">
              <div className="modal-header">
                <h5 className="modal-title">{editingExpense ? 'Edit Expense' : 'Add Expense'}</h5>
                <button type="button" className="btn-close" onClick={() => setShowModal(false)}></button>
              </div>
              <form onSubmit={handleSubmit}>
                <div className="modal-body">
                  <div className="mb-3">
                    <label className="form-label">Description *</label>
                    <input type="text" className="form-control" value={formData.description}
                      onChange={e => setFormData({...formData, description: e.target.value})} required />
                  </div>
                  <div className="row">
                    <div className="col-md-6 mb-3">
                      <label className="form-label">Amount *</label>
                      <div className="input-group">
                        <span className="input-group-text">$</span>
                        <input type="number" step="0.01" min="0.01" className="form-control" value={formData.amount}
                          onChange={e => setFormData({...formData, amount: e.target.value})} required />
                      </div>
                    </div>
                    <div className="col-md-6 mb-3">
                      <label className="form-label">Date *</label>
                      <input type="date" className="form-control" value={formData.expenseDate}
                        onChange={e => setFormData({...formData, expenseDate: e.target.value})} required />
                    </div>
                  </div>
                  <div className="mb-3">
                    <label className="form-label">Category *</label>
                    <select className="form-select" value={formData.categoryId}
                      onChange={e => setFormData({...formData, categoryId: e.target.value})} required>
                      <option value="">Select category</option>
                      {categories.map(cat => <option key={cat.id} value={cat.id}>{cat.name}</option>)}
                    </select>
                  </div>
                </div>
                <div className="modal-footer">
                  <button type="button" className="btn btn-secondary" onClick={() => setShowModal(false)}>Cancel</button>
                  <button type="submit" className="btn btn-primary"><i className="fas fa-save me-1"></i>Save</button>
                </div>
              </form>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default Expenses;
```

---

## 📝 Step 7: Setup App Routing (2 minutes)

**Expected file**: `src/App.jsx`

```jsx
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import Layout from './components/Layout';
import Dashboard from './pages/Dashboard';
import Categories from './pages/Categories';
import Expenses from './pages/Expenses';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Dashboard />} />
          <Route path="categories" element={<Categories />} />
          <Route path="expenses" element={<Expenses />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
```

**Update** `src/main.jsx`:

```jsx
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
```

---

## 📝 Step 8: Run & Test (5 minutes)

### ✅ Start Both Applications

```bash
# Terminal 1: Start Spring Boot backend
cd backend
./mvnw spring-boot:run

# Terminal 2: Start React frontend
cd frontend
npm run dev
```

### 🔍 Test at http://localhost:3000

- [ ] Dashboard loads with charts
- [ ] Categories CRUD works
- [ ] Expenses CRUD works
- [ ] Filter by category works

---

## 🎉 Session 4c Deliverables

### ✅ What You've Accomplished

- **✅ Modern SPA** - React with hooks and functional components
- **✅ API Integration** - Axios service layer
- **✅ Component Architecture** - Reusable React components
- **✅ Routing** - React Router for navigation
- **✅ Charts** - Chart.js integration

### 🆚 Comparison

| Aspect | Thymeleaf | React |
|--------|-----------|-------|
| Rendering | Server-side | Client-side |
| Learning | HTML + Thymeleaf | JavaScript/React |
| State | Server sessions | React state |
| SEO | Better by default | Needs SSR |
| Development | Single project | Two projects |

---

## 💡 GitHub Copilot Tips for React

### 🎯 Effective Prompts

```text
/generate Create a React component with useState and useEffect that [description]
"Add form validation to this React component"
"Convert this class component to functional with hooks"
```

### 🤖 Recommended Model

**Claude 3.5 Sonnet** or **GPT-4o** for:
- React component generation
- Hook patterns
- State management
- JSX templates

---

## 🎊 Alternative Complete!

You now have a React SPA that:
- ✅ Consumes your existing REST APIs
- ✅ Uses modern React patterns (hooks)
- ✅ Provides professional UI with Bootstrap
- ✅ Includes data visualization with Chart.js
