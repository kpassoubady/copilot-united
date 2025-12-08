# 🔍 EDA Detective

## 🎯 Objective

Use GitHub Copilot to perform Exploratory Data Analysis and uncover hidden insights in a mystery dataset.

## 🎮 Game Format

You're a data detective! Given a dataset with no documentation, use Copilot to:
1. Understand the data structure
2. Identify patterns and anomalies
3. Generate hypotheses about relationships
4. Present your findings

## 🕵️ Investigation Phases

### Phase 1: First Impressions (10 minutes)

**Goal**: Understand what you're working with

**Tasks**:
```python
# Ask Copilot to help you:
# 1. Load and display basic info about the dataset
# 2. Check data types and missing values
# 3. Get summary statistics
# 4. Identify the likely purpose of each column
```

**Sample Prompts**:
- "Write a function that provides a comprehensive overview of a DataFrame including shape, dtypes, nulls, and unique values per column"
- "Generate a data profiling report for this DataFrame"

---

### Phase 2: Statistical Deep Dive (15 minutes)

**Goal**: Find numerical patterns

**Tasks**:
- Distribution analysis for each numeric column
- Correlation analysis
- Identify statistical outliers
- Compare groups if categorical columns exist

**Detective Questions**:
1. Which columns have the most variance?
2. Are there any highly correlated features?
3. Do any distributions suggest data quality issues?

---

### Phase 3: Pattern Recognition (15 minutes)

**Goal**: Discover relationships and trends

**Tasks**:
```python
# Use Copilot to:
# 1. Create scatter plots for potentially related variables
# 2. Generate grouped statistics
# 3. Identify temporal patterns (if date columns exist)
# 4. Find categorical variable relationships
```

---

### Phase 4: Case Report (10 minutes)

**Goal**: Summarize findings

**Deliverable**: A markdown report with:
- Dataset overview
- Key findings (3-5 insights)
- Visualizations supporting findings
- Recommended next steps

## 🏆 Scoring

| Discovery Type | Points |
|----------------|--------|
| Basic insight (obvious pattern) | 5 |
| Intermediate insight (requires analysis) | 10 |
| Advanced insight (hidden relationship) | 20 |
| Novel visualization technique | 10 |
| Actionable recommendation | 15 |

## 💡 EDA Copilot Prompts

### Data Overview
```
"Create a comprehensive EDA function that takes a DataFrame and returns:
1. Basic statistics (shape, dtypes, memory usage)
2. Missing value analysis with percentages
3. Unique value counts for each column
4. Top correlations between numeric columns"
```

### Distribution Analysis
```
"Generate code to visualize the distribution of all numeric columns
in a grid layout, with histograms and box plots side by side,
highlighting potential outliers"
```

### Correlation Investigation
```
"Create an interactive correlation analysis that:
1. Shows a heatmap of correlations
2. Lists the top 10 most correlated pairs
3. Generates scatter plots for the strongest relationships"
```

## 📊 EDA Checklist

- [ ] Dataset dimensions and memory usage
- [ ] Data types for each column
- [ ] Missing value counts and patterns
- [ ] Duplicate row check
- [ ] Summary statistics (mean, median, std, etc.)
- [ ] Distribution plots for numeric columns
- [ ] Value counts for categorical columns
- [ ] Correlation matrix
- [ ] Outlier detection
- [ ] Time-based patterns (if applicable)

## 🧪 Mystery Datasets

Use these from `project4/data-pipeline/data/`:
1. Start with a simple CSV
2. Try to discover what the data represents
3. Document your detective process

## 🎬 Example Detective Report

```markdown
# EDA Report: Mystery Dataset

## Overview
- **Rows**: 10,000
- **Columns**: 15
- **Time Period**: 2020-2023

## Key Findings

### Finding 1: Seasonal Pattern
The `value` column shows clear quarterly spikes...

### Finding 2: Strong Correlation
Columns A and B have r=0.87 correlation...

### Finding 3: Data Quality Issue
Column C has 23% missing values, concentrated in...

## Recommendations
1. Investigate the seasonal pattern cause
2. Consider feature engineering with A*B
3. Impute missing values using...
```
