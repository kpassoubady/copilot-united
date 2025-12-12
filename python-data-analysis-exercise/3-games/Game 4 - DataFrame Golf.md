# ⛳ DataFrame Golf

## 🎯 Objective

Solve data manipulation challenges using the **fewest characters** of code possible with Pandas method chaining.

## 🎮 Game Rules

- Each challenge has a target output
- Write the shortest Pandas code to achieve it
- Must use proper Pandas methods (no exec/eval hacks)
- Method chaining is encouraged
- Lowest character count wins!

## 🏌️ Challenges

### Hole 1: Filter and Sort (Par 60 chars)

**Input DataFrame**:
```python
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 30, 35, 28],
    'salary': [50000, 60000, 70000, 55000]
})
```

**Goal**: Get names of people over 27, sorted by salary descending

**Expected Output**: `['Charlie', 'Bob', 'David']`

**Hints**: Try `query()`, `sort_values()`, `tolist()`

---

### Hole 2: Aggregate Attack (Par 80 chars)

**Input**: Sales DataFrame with columns `['product', 'region', 'sales', 'quantity']`

**Goal**: Get total sales and average quantity per product

**Expected**: DataFrame with product as index, sum of sales, mean of quantity

---

### Hole 3: Pivot Pro (Par 100 chars)

**Input**: Long-format data with `['date', 'category', 'value']`

**Goal**: Pivot to wide format with dates as rows, categories as columns

---

### Hole 4: String Slinger (Par 70 chars)

**Input**: DataFrame with messy text column

**Goal**: Clean column: lowercase, strip whitespace, replace spaces with underscores

---

### Hole 5: DateTime Dash (Par 90 chars)

**Input**: DataFrame with string date column `'date_str'`

**Goal**: Convert to datetime, extract year and month as new columns

---

### Hole 6: Join Journey (Par 120 chars)

**Input**: Two DataFrames to merge

**Goal**: Left join, fill NaN with 0, keep only rows where joined value > 100

## 🏆 Scoring

| Strokes Under Par | Points |
|-------------------|--------|
| 20+ under | 50 |
| 10-19 under | 40 |
| 1-9 under | 30 |
| Par | 20 |
| Over par | 10 |

## 💡 Golf Tips

### Method Chaining Magic
```python
# Instead of:
df2 = df[df['age'] > 25]
df3 = df2.sort_values('salary')
result = df3['name'].tolist()

# Golf style:
df.query('age>25').sort_values('salary').name.tolist()
```

### Short Aliases
```python
# Use .loc sparingly - often query() is shorter
df.query('a>5&b<10')  # vs df.loc[(df.a>5)&(df.b<10)]

# Use .pipe() for custom functions
df.pipe(lambda x: x[x.a>5])
```

### One-Liners
```python
# Assign multiple columns
df.assign(year=df.date.dt.year, month=df.date.dt.month)

# Agg multiple functions
df.groupby('cat').agg({'val':['sum','mean']})
```

## 🎯 Copilot Challenge

Ask Copilot: "What's the shortest Pandas code to [task]?"

Then try to beat Copilot's suggestion!

## 📊 Leaderboard Template

| Hole | Par | Your Score | Copilot Score |
|------|-----|------------|---------------|
| 1 | 60 | | |
| 2 | 80 | | |
| 3 | 100 | | |
| 4 | 70 | | |
| 5 | 90 | | |
| 6 | 120 | | |
| **Total** | **520** | | |
