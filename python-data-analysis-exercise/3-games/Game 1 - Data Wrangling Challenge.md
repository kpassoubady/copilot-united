# 🧹 Data Wrangling Challenge

## 🎯 Objective

Write the best prompt to get GitHub Copilot to clean a messy dataset using Pandas.

## 📋 The Challenge

You have a messy CSV file with the following issues:
- Missing values in multiple columns
- Inconsistent date formats (MM/DD/YYYY, YYYY-MM-DD, DD-MM-YYYY)
- Duplicate rows
- Mixed case in string columns
- Numeric columns stored as strings with currency symbols ($1,234.56)
- Outliers in numeric data

## 🎮 Game Rules

### Round 1: Basic Cleaning (10 minutes)
Write a prompt to generate code that:
1. Loads the CSV file
2. Removes duplicate rows
3. Handles missing values appropriately
4. Standardizes column names (lowercase, underscores)

### Round 2: Type Conversion (10 minutes)
Write a prompt to:
1. Convert date strings to datetime objects
2. Clean currency strings to float values
3. Convert categorical columns to appropriate types

### Round 3: Data Validation (10 minutes)
Write a prompt to:
1. Identify and handle outliers
2. Validate data ranges (e.g., age between 0-120)
3. Create a data quality report

## 📝 Sample Prompt Template

```
I have a CSV file with messy data. Please write a Python function using Pandas that:
1. [Specific cleaning task]
2. [Another task]

The data has these columns: [column names]
Known issues include: [list issues]

Please include:
- Error handling for edge cases
- Logging of changes made
- A summary of rows affected
```

## 🏆 Scoring Criteria

| Criteria | Points |
|----------|--------|
| Code correctness | 30 |
| Handles edge cases | 20 |
| Clean, readable code | 20 |
| Efficient operations | 15 |
| Good documentation | 15 |

## 💡 Copilot Tips

- Use `#file` to reference your CSV structure
- Be specific about data types expected
- Mention the Pandas version (e.g., pandas 2.0+)
- Ask for method chaining for cleaner code

## 🎬 Example Solution Approach

```python
import pandas as pd

def clean_dataset(filepath: str) -> pd.DataFrame:
    """
    Clean a messy dataset by handling common data quality issues.
    
    Args:
        filepath: Path to the CSV file
        
    Returns:
        Cleaned DataFrame
    """
    # Load data
    df = pd.read_csv(filepath)
    
    # Chain cleaning operations
    df_clean = (df
        .drop_duplicates()
        .pipe(standardize_columns)
        .pipe(handle_missing_values)
        .pipe(convert_data_types)
        .pipe(remove_outliers)
    )
    
    return df_clean
```

## 🔗 Related Datasets

Use files from `project4/data-pipeline/data/` for practice.
