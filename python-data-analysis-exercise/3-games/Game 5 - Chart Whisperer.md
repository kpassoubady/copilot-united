# 🎨 Chart Whisperer

## 🎯 Objective

Reverse-engineer visualizations! Given a chart image, write a prompt that makes Copilot generate code to recreate it exactly.

## 🎮 Game Format

1. See a target visualization
2. Write a prompt describing it precisely
3. Generate code with Copilot
4. Compare output to target
5. Score based on accuracy

## 🖼️ Challenges

### Challenge 1: The Bar Chart

**Target Description**: A horizontal bar chart showing top 5 countries by GDP, with:
- Blue bars with gradient effect
- Value labels at end of each bar
- Title: "Top 5 Economies 2023"
- Y-axis: Country names
- X-axis: GDP in trillions (formatted with $)

**Your Prompt**: Write the most precise prompt to recreate this chart.

---

### Challenge 2: The Time Series

**Target Description**: A line chart with:
- Two lines (actual vs predicted)
- Shaded confidence interval around predicted
- Legend in upper left
- Date range on x-axis (Jan-Dec)
- Grid lines (light gray, dashed)

---

### Challenge 3: The Scatter Matrix

**Target Description**: A 3x3 scatter plot matrix with:
- Diagonal: histograms
- Off-diagonal: scatter plots with regression lines
- Color-coded by category
- Shared axes

---

### Challenge 4: The Heatmap

**Target Description**: A correlation heatmap with:
- Diverging colormap (red-white-blue)
- Annotations showing correlation values
- Dendrograms on both axes (clustered)
- Mask for upper triangle

---

### Challenge 5: The Dashboard

**Target Description**: A 2x2 subplot figure with:
- Top-left: Pie chart with exploded slice
- Top-right: Stacked bar chart
- Bottom-left: Box plots by category
- Bottom-right: Line chart with markers
- Shared title: "Q4 Performance Summary"

## 🏆 Scoring

| Accuracy Level | Points |
|----------------|--------|
| Exact match | 100 |
| Minor differences (colors, fonts) | 80 |
| Correct chart type, different style | 60 |
| Similar but missing elements | 40 |
| Wrong chart type | 10 |

## 💡 Prompt Engineering Tips

### Be Specific About:

**1. Chart Type**
```
"Create a horizontal bar chart" (not just "bar chart")
"Create a scatter plot with regression line" (not just "scatter plot")
```

**2. Styling**
```
"Use the 'viridis' colormap"
"Set figure size to 10x6 inches"
"Use 'seaborn-whitegrid' style"
```

**3. Annotations**
```
"Add value labels on each bar, formatted as currency"
"Include a text box with R² value in upper right"
```

**4. Axes**
```
"X-axis: dates from Jan 2023 to Dec 2023, monthly ticks"
"Y-axis: values from 0 to 100, labeled as percentages"
```

## 📝 Prompt Template

```
Create a [CHART TYPE] visualization with matplotlib/seaborn that shows:

Data:
- X-axis: [description]
- Y-axis: [description]
- Categories/Groups: [if applicable]

Styling:
- Color scheme: [specific colors or palette]
- Figure size: [width x height]
- Style: [matplotlib style]

Elements:
- Title: "[exact title]"
- Legend: [position and format]
- Annotations: [specific labels or markers]
- Grid: [yes/no, style]

Additional:
- [Any special requirements]
```

## 🎬 Example Round

**Target**: A donut chart showing market share

**Winning Prompt**:
```
Create a donut chart (pie chart with hole) using matplotlib showing
market share of 5 companies:
- Data: [40, 25, 15, 12, 8] with labels ['Company A', 'B', 'C', 'D', 'Other']
- Colors: use 'Set2' colormap
- Center hole: 40% of radius
- Add percentage labels on each slice (formatted as "XX%")
- Add center text showing "Total: $50B"
- Title: "Market Share 2023"
- Add a subtle shadow effect
- Figure size: 8x8
- Explode the largest slice slightly (0.05)
```

## 🔗 Practice Resources

Look at charts from:
- [Our World in Data](https://ourworldindata.org/)
- [FiveThirtyEight](https://fivethirtyeight.com/)
- [Seaborn Gallery](https://seaborn.pydata.org/examples/)
