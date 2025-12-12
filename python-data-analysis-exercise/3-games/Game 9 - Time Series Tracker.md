# ⏰ Time Series Tracker

## 🎯 Objective

Master time series analysis with Pandas using GitHub Copilot for date manipulation, resampling, and temporal pattern detection.

## 🎮 Game Format

Track through time-based challenges, from basic datetime handling to advanced temporal analysis.

## 📅 Challenges

### Level 1: DateTime Fundamentals (10 minutes)

**Challenge 1.1**: Convert string dates to datetime
```python
# Input: '2023-01-15', '01/15/2023', 'Jan 15, 2023', '15-Jan-2023'
# All should become proper datetime objects
```

**Challenge 1.2**: Extract components
```python
# From a datetime column, create:
# - year, month, day columns
# - day_of_week (Monday=0)
# - is_weekend boolean
# - quarter
```

**Challenge 1.3**: Date arithmetic
```python
# Calculate:
# - Days since first purchase
# - Days until next month
# - Business days between two dates
```

---

### Level 2: Resampling & Rolling (15 minutes)

**Challenge 2.1**: Downsampling
```python
# Convert daily data to:
# - Weekly (sum of values)
# - Monthly (mean of values)
# - Quarterly (last value)
```

**Challenge 2.2**: Upsampling
```python
# Convert monthly data to daily:
# - Forward fill
# - Linear interpolation
# - Distribute value evenly
```

**Challenge 2.3**: Rolling Windows
```python
# Calculate:
# - 7-day rolling average
# - 30-day rolling sum
# - Rolling standard deviation
# - Expanding mean (cumulative)
```

---

### Level 3: Temporal Patterns (20 minutes)

**Challenge 3.1**: Seasonality Detection
```python
# Identify patterns:
# - Day of week effect
# - Monthly seasonality
# - Year-over-year comparison
```

**Challenge 3.2**: Trend Analysis
```python
# Calculate:
# - Moving average trend line
# - Period-over-period growth
# - Cumulative growth
```

**Challenge 3.3**: Anomaly Detection
```python
# Flag anomalies:
# - Values outside 3 standard deviations
# - Unusual day-of-week values
# - Missing expected dates
```

---

### Level 4: Advanced Time Series (20 minutes)

**Challenge 4.1**: Lag Features
```python
# Create:
# - Previous day value (lag 1)
# - Same day last week (lag 7)
# - Same day last month
# - Same day last year
```

**Challenge 4.2**: Lead Features
```python
# Create:
# - Next day value
# - Value 7 days ahead
# - Forward-looking rolling average
```

**Challenge 4.3**: Time-Based Joins
```python
# Join two time series:
# - Align by nearest date
# - Forward fill missing matches
# - As-of join (last known value)
```

## 🏆 Scoring

| Challenge | Points |
|-----------|--------|
| DateTime conversion | 10 |
| Component extraction | 15 |
| Resampling | 20 |
| Rolling calculations | 20 |
| Seasonality analysis | 25 |
| Lag/Lead features | 25 |
| Time-based joins | 30 |

## 💡 Copilot Prompts for Time Series

### DateTime Handling
```
"Parse these date formats into pandas datetime:
- '2023-01-15' (ISO)
- '01/15/2023' (US)
- '15/01/2023' (European)
- 'January 15, 2023' (Long)
Handle errors gracefully and return NaT for invalid dates"
```

### Resampling
```
"Resample this daily time series DataFrame:
1. Weekly totals (week ending Sunday)
2. Monthly averages
3. Quarterly last values
Preserve the datetime index and handle missing periods"
```

### Pattern Detection
```
"Analyze this time series for patterns:
1. Calculate day-of-week averages and identify best/worst days
2. Compute month-over-month growth rates
3. Detect if there's a significant trend (simple regression)
4. Flag any values more than 2 std devs from rolling mean
Return a summary DataFrame with findings"
```

## 📊 Time Series Code Snippets

### DateTime Basics
```python
import pandas as pd

# Parse dates
df['date'] = pd.to_datetime(df['date_str'], format='%Y-%m-%d')

# Set as index
df = df.set_index('date')

# Extract components
df['year'] = df.index.year
df['month'] = df.index.month
df['day_of_week'] = df.index.dayofweek
df['is_weekend'] = df.index.dayofweek >= 5
```

### Resampling
```python
# Downsample
daily_to_weekly = df.resample('W').sum()
daily_to_monthly = df.resample('M').mean()

# Upsample
monthly_to_daily = df.resample('D').ffill()

# Custom periods
df.resample('2W').agg({'col1': 'sum', 'col2': 'mean'})
```

### Rolling & Expanding
```python
# Rolling calculations
df['rolling_7d'] = df['value'].rolling(window=7).mean()
df['rolling_30d_sum'] = df['value'].rolling(window=30).sum()

# Expanding (cumulative)
df['cumsum'] = df['value'].expanding().sum()
df['cummax'] = df['value'].expanding().max()

# Exponential weighted
df['ewm'] = df['value'].ewm(span=7).mean()
```

### Lag/Lead Features
```python
# Lag features
df['lag_1'] = df['value'].shift(1)
df['lag_7'] = df['value'].shift(7)

# Lead features
df['lead_1'] = df['value'].shift(-1)

# Percent change
df['pct_change'] = df['value'].pct_change()
df['pct_change_7d'] = df['value'].pct_change(periods=7)
```

## 🎯 Final Challenge: Time Series Dashboard

```python
def create_time_series_dashboard(df: pd.DataFrame, date_col: str, value_col: str):
    """
    Create a comprehensive time series analysis.
    
    Use Copilot to generate:
    1. Trend line plot with confidence interval
    2. Seasonality decomposition
    3. Day-of-week box plots
    4. Month-over-month comparison
    5. Anomaly highlights
    6. Summary statistics by period
    
    Return: matplotlib figure with 2x3 subplots
    """
    pass
```

## 📚 Resources

- [Pandas Time Series Guide](https://pandas.pydata.org/docs/user_guide/timeseries.html)
- [Resampling Documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.resample.html)
