# 🔎 Missing Data Mystery

## 🎯 Objective

Master the art of handling missing data using GitHub Copilot. Detect patterns, choose appropriate strategies, and implement robust solutions.

## 🎮 Game Format

Investigate datasets with various missing data patterns and implement the best handling strategy.

## 🕵️ Mystery Cases

### Case 1: The Random Gaps (10 minutes)

**Scenario**: Sales data with randomly missing values

**Investigation Tasks**:
1. Identify missing value patterns
2. Determine if missing completely at random (MCAR)
3. Implement appropriate imputation

**Copilot Prompt**:
```
Analyze missing data patterns in this DataFrame:
1. Show missing count and percentage per column
2. Visualize missing data pattern (use missingno library if available)
3. Test if data is MCAR using Little's test concept
4. Recommend imputation strategy based on findings
```

---

### Case 2: The Systematic Absence (15 minutes)

**Scenario**: Survey data where certain demographics skipped questions

**Pattern**: Missing Not at Random (MNAR)

**Tasks**:
- Identify which groups have missing data
- Determine if missingness correlates with other variables
- Implement conditional imputation

---

### Case 3: The Time Gap (15 minutes)

**Scenario**: Time series with missing timestamps

**Challenges**:
- Missing entire rows (gaps in time)
- Forward fill vs backward fill decisions
- Interpolation methods

**Code Template**:
```python
def handle_time_series_gaps(df: pd.DataFrame, date_col: str, value_cols: list) -> pd.DataFrame:
    """
    Handle missing values in time series data.
    
    Steps:
    1. Create complete date range
    2. Reindex to fill gaps
    3. Apply appropriate interpolation
    4. Handle edge cases
    """
    # Use Copilot to implement
    pass
```

---

### Case 4: The Multi-Column Puzzle (20 minutes)

**Scenario**: Dataset where missing values in one column relate to another

**Example**: Income missing when employment_status = "Student"

**Advanced Tasks**:
- Detect correlated missingness
- Implement conditional imputation
- Validate imputation quality

## 🛠️ Imputation Strategies Reference

| Strategy | When to Use | Copilot Prompt |
|----------|-------------|----------------|
| Drop rows | < 5% missing, MCAR | `"Remove rows with any missing values"` |
| Mean/Median | Numeric, normal/skewed | `"Fill missing with column median"` |
| Mode | Categorical data | `"Fill missing with most frequent value"` |
| Forward Fill | Time series | `"Forward fill missing values in time order"` |
| Interpolation | Continuous time series | `"Linearly interpolate missing values"` |
| KNN Impute | Complex patterns | `"Use KNN imputation with 5 neighbors"` |
| Regression | Predictable from other cols | `"Predict missing values using linear regression"` |

## 🏆 Scoring

| Achievement | Points |
|-------------|--------|
| Correctly identify missing pattern | 20 |
| Choose appropriate strategy | 25 |
| Implement correctly | 25 |
| Validate imputation quality | 15 |
| Document reasoning | 15 |

## 💡 Copilot Prompts for Missing Data

### Analysis Prompts
```
"Create a missing data analysis report that shows:
1. Missing count per column as bar chart
2. Missing percentage with color coding (green <5%, yellow 5-20%, red >20%)
3. Correlation matrix of missingness indicators
4. Recommendations based on patterns found"
```

### Implementation Prompts
```
"Write a flexible imputation function that:
- Accepts strategy parameter ('mean', 'median', 'mode', 'knn', 'interpolate')
- Handles numeric and categorical columns differently
- Returns imputed DataFrame and a report of changes made
- Includes option to create 'was_missing' indicator columns"
```

### Validation Prompts
```
"Create a function to validate imputation quality:
1. Compare distributions before/after (KS test)
2. Check if imputed values are within reasonable range
3. Verify no new missing values introduced
4. Generate visualization comparing original vs imputed"
```

## 📊 Missing Data Visualization Code

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_missing(df: pd.DataFrame):
    """Visualize missing data patterns."""
    # Ask Copilot to:
    # 1. Create a heatmap of missing values
    # 2. Show bar chart of missing percentages
    # 3. Create a matrix showing missing patterns
    pass

# Quick missing data summary
def missing_summary(df):
    """Generate missing data summary."""
    missing = df.isnull().sum()
    percent = 100 * missing / len(df)
    return pd.DataFrame({
        'Missing': missing,
        'Percent': percent,
        'Type': df.dtypes
    }).sort_values('Percent', ascending=False)
```

## 🎯 Challenge: The Ultimate Imputer

Create a class that handles all missing data scenarios:

```python
class SmartImputer:
    """
    Intelligent missing data handler.
    
    Use Copilot to implement:
    - fit(): Analyze patterns and choose strategies
    - transform(): Apply imputation
    - fit_transform(): Both in one call
    - get_report(): Return imputation summary
    """
    
    def __init__(self, strategy='auto'):
        self.strategy = strategy
        self.column_strategies_ = {}
        self.imputation_values_ = {}
    
    # Let Copilot implement the rest!
```

## 📚 Resources

- [Pandas Missing Data Docs](https://pandas.pydata.org/docs/user_guide/missing_data.html)
- [Scikit-learn Imputation](https://scikit-learn.org/stable/modules/impute.html)
- [missingno Library](https://github.com/ResidentMario/missingno)
