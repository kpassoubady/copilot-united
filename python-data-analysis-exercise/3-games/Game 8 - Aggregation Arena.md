# 🏟️ Aggregation Arena

## 🎯 Objective

Master Pandas GroupBy, pivot tables, and aggregation operations using GitHub Copilot.

## 🎮 Game Format

Battle through increasingly complex aggregation challenges. Each round tests different aspects of data aggregation.

## ⚔️ Battle Rounds

### Round 1: GroupBy Basics (10 minutes)

**Dataset**: Sales transactions with `[date, product, category, region, sales, quantity]`

**Challenges**:

1. **Single Group**: Total sales by category
```python
# Target output: DataFrame with category and total_sales
```

2. **Multiple Groups**: Average sales by category AND region
```python
# Target output: DataFrame with category, region, avg_sales
```

3. **Multiple Aggregations**: Sum of sales, count of transactions, average quantity by product
```python
# Use .agg() with multiple functions
```

---

### Round 2: Transform vs Aggregate (15 minutes)

**Concept**: Understand when to use `transform()` vs `agg()`

**Challenge 1**: Add a column showing each row's percentage of its category total
```python
# transform() keeps the original shape
df['pct_of_category'] = df.groupby('category')['sales'].transform(
    lambda x: x / x.sum() * 100
)
```

**Challenge 2**: Flag rows above category average
```python
# Create 'above_avg' column using transform
```

**Challenge 3**: Rank within groups
```python
# Rank each product's sales within its category
```

---

### Round 3: Pivot Table Power (15 minutes)

**Challenge 1**: Basic Pivot
```python
# Rows: Region
# Columns: Category  
# Values: Sum of Sales
```

**Challenge 2**: Multi-Index Pivot
```python
# Rows: [Region, Store]
# Columns: [Category, Product]
# Values: Sales (sum), Quantity (mean)
```

**Challenge 3**: Pivot with Margins
```python
# Add row and column totals
```

---

### Round 4: Advanced Aggregation (20 minutes)

**Challenge 1**: Custom Aggregation Function
```python
def sales_range(x):
    """Return the range (max - min) of sales."""
    return x.max() - x.min()

# Apply to groupby
```

**Challenge 2**: Named Aggregation (Pandas 0.25+)
```python
df.groupby('category').agg(
    total_sales=('sales', 'sum'),
    avg_quantity=('quantity', 'mean'),
    unique_products=('product', 'nunique')
)
```

**Challenge 3**: Window Functions
```python
# Rolling 7-day average sales by category
# Cumulative sum within groups
# Lag/Lead values
```

## 🏆 Scoring

| Challenge Completed | Points |
|---------------------|--------|
| Basic GroupBy | 10 |
| Multiple Aggregations | 15 |
| Transform correctly | 20 |
| Pivot Table | 15 |
| Multi-Index Pivot | 20 |
| Custom Aggregation | 25 |
| Window Functions | 30 |

## 💡 Copilot Prompts for Aggregation

### GroupBy Prompts
```
"Group this sales DataFrame by category and calculate:
- Total sales (sum)
- Number of transactions (count)
- Average order value (mean)
- Best selling product (mode)
Return as a clean DataFrame with descriptive column names"
```

### Pivot Table Prompts
```
"Create a pivot table from this DataFrame:
- Index: region and store_type (hierarchical)
- Columns: quarter
- Values: revenue (sum) and units (sum)
- Include margins (totals)
- Format numbers with commas"
```

### Transform Prompts
```
"Add these calculated columns to the DataFrame:
1. 'pct_of_group': Each row's percentage of its group total
2. 'vs_group_avg': Difference from group average
3. 'group_rank': Rank within group (1 = highest)
Group by 'category' column"
```

## 📊 Quick Reference

### GroupBy Methods
```python
# Basic aggregations
df.groupby('col').sum()
df.groupby('col').mean()
df.groupby('col').count()
df.groupby('col').nunique()  # unique count
df.groupby('col').first()    # first value
df.groupby('col').last()     # last value

# Multiple columns
df.groupby(['col1', 'col2']).agg({'val1': 'sum', 'val2': 'mean'})

# Named aggregation
df.groupby('col').agg(
    new_name=('old_col', 'function')
)
```

### Pivot Tables
```python
pd.pivot_table(
    df,
    values='sales',
    index=['region'],
    columns=['category'],
    aggfunc='sum',
    margins=True,
    fill_value=0
)
```

### Transform vs Apply
```python
# transform: returns same-shaped output
df.groupby('cat')['val'].transform('mean')

# apply: flexible output shape
df.groupby('cat').apply(lambda x: x.nlargest(3, 'val'))
```

## 🎯 Final Boss: Complex Report

Create a comprehensive sales report function:

```python
def generate_sales_report(df: pd.DataFrame) -> dict:
    """
    Generate a complete sales analysis report.
    
    Use Copilot to implement:
    1. Summary by category (totals, averages)
    2. Top 10 products by revenue
    3. Regional performance comparison
    4. Month-over-month growth
    5. Product category pivot table
    
    Returns dict with DataFrames for each analysis.
    """
    pass
```

## 📚 Resources

- [Pandas GroupBy Guide](https://pandas.pydata.org/docs/user_guide/groupby.html)
- [Pivot Table Documentation](https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html)
