# 📊 Visualization Battle

## 🎯 Objective

Compete to create the most insightful and visually appealing charts using GitHub Copilot.

## 🎮 Game Format

Teams compete to create the best visualization for given datasets. Judged on clarity, aesthetics, and insight delivered.

## 📋 Challenges

### Challenge 1: Sales Dashboard (15 minutes)

**Dataset**: Monthly sales data with categories, regions, and products

**Requirements**:
- Create a multi-panel dashboard (2x2 grid)
- Include: bar chart, line chart, pie chart, heatmap
- Use consistent color scheme
- Add proper titles and labels

**Prompt Starting Point**:
```
Create a sales dashboard with 4 subplots using matplotlib and seaborn:
- Top-left: Monthly sales trend (line chart)
- Top-right: Sales by category (bar chart)
- Bottom-left: Regional distribution (pie chart)
- Bottom-right: Category vs Region heatmap

Use a professional color palette and include:
- Figure size 14x10
- Proper titles for each subplot
- Legend where appropriate
```

---

### Challenge 2: Distribution Analysis (15 minutes)

**Dataset**: Customer demographics or sensor readings

**Requirements**:
- Show distribution of a numeric variable
- Compare distributions across categories
- Highlight outliers and statistics

**Techniques to use**:
- Histogram with KDE
- Box plots / Violin plots
- Statistical annotations

---

### Challenge 3: Correlation Explorer (15 minutes)

**Dataset**: Multi-variable dataset (e.g., housing prices, stock data)

**Requirements**:
- Correlation heatmap with annotations
- Scatter plot matrix for top correlations
- Regression line with confidence interval

## 🏆 Scoring Rubric

| Category | Points | Description |
|----------|--------|-------------|
| **Clarity** | 25 | Easy to understand at a glance |
| **Aesthetics** | 25 | Professional, polished appearance |
| **Insight** | 25 | Reveals meaningful patterns in data |
| **Code Quality** | 15 | Clean, reusable, well-documented |
| **Creativity** | 10 | Novel approaches or enhancements |

## 💡 Copilot Tips for Visualization

```python
# Tip 1: Set style at the start
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="whitegrid", palette="husl")
plt.rcParams['figure.figsize'] = [12, 8]

# Tip 2: Ask Copilot for specific chart types
# "Create a grouped bar chart comparing X across Y categories"

# Tip 3: Request annotations
# "Add value labels on top of each bar"
# "Include a trend line with equation"

# Tip 4: Ask for color guidance
# "Use a colorblind-friendly palette"
# "Apply a sequential colormap for the heatmap"
```

## 🎨 Visualization Checklist

- [ ] Clear, descriptive title
- [ ] Labeled axes with units
- [ ] Legend (if multiple series)
- [ ] Appropriate chart type for data
- [ ] No chartjunk (unnecessary elements)
- [ ] Color-blind friendly colors
- [ ] Readable font sizes
- [ ] Source citation (if applicable)

## 📦 Quick Setup

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load sample data
df = pd.read_csv('../project4/data-pipeline/data/your_dataset.csv')

# Quick exploration
print(df.info())
print(df.describe())
```

## 🔗 Resources

- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
- [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)
- [ColorBrewer Palettes](https://colorbrewer2.org/)
