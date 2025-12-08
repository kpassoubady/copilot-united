# 📖 Data Storyteller

## 🎯 Objective

Use GitHub Copilot to transform raw data analysis into compelling narratives and reports.

## 🎮 Game Format

Given analysis results, compete to create the most engaging and insightful data story.

## 📋 Challenges

### Challenge 1: Executive Summary (15 minutes)

**Scenario**: You've analyzed quarterly sales data. Generate an executive summary.

**Input Data**:
```python
results = {
    'q4_revenue': 2_450_000,
    'q4_growth': 0.23,
    'top_product': 'Widget Pro',
    'top_region': 'West',
    'customer_churn': 0.08,
    'new_customers': 1250
}
```

**Task**: Use Copilot to generate:
1. A 3-paragraph executive summary
2. Key metrics highlighted
3. Recommendations section

**Prompt Example**:
```
Generate an executive summary for quarterly business review based on:
- Revenue: $2.45M (23% growth)
- Top performer: Widget Pro in West region
- Customer churn: 8%, new customers: 1,250

Include tone: professional but accessible
Format: 3 paragraphs with bullet points for key metrics
End with: 2-3 actionable recommendations
```

---

### Challenge 2: Data Blog Post (20 minutes)

**Scenario**: Transform EDA findings into a blog-style article.

**Requirements**:
- Engaging title
- Hook in first paragraph
- Data-driven insights with visualizations
- Conclusion with takeaways

---

### Challenge 3: Automated Report (20 minutes)

**Scenario**: Create a reusable report generator.

**Task**: Use Copilot to create a function that:
```python
def generate_report(df: pd.DataFrame, title: str) -> str:
    """
    Generate a markdown report from a DataFrame.
    
    Includes:
    - Data overview
    - Key statistics
    - Auto-generated insights
    - Embedded visualization references
    """
    pass
```

---

### Challenge 4: Presentation Slides (15 minutes)

**Scenario**: Generate slide content from analysis.

**Output Format**:
```markdown
# Slide 1: Title
## Key Finding: [Main Insight]

# Slide 2: The Data
- Dataset: [description]
- Time period: [range]
- Key metrics: [list]

# Slide 3: Visualization
[Chart description + key callout]

# Slide 4: Recommendations
1. [Action item]
2. [Action item]
3. [Action item]
```

## 🏆 Scoring

| Criteria | Points |
|----------|--------|
| Clarity of message | 25 |
| Accuracy of insights | 25 |
| Engaging narrative | 20 |
| Actionable recommendations | 15 |
| Professional formatting | 15 |

## 💡 Storytelling Prompts

### For Summaries
```
"Summarize this DataFrame analysis in 3 sentences for a non-technical audience,
highlighting the most surprising finding and its business implication"
```

### For Insights
```
"Based on these statistics, generate 5 bullet-point insights,
ordered by potential business impact, with specific numbers cited"
```

### For Recommendations
```
"Given these findings about customer behavior, generate 3 actionable
recommendations with expected impact and implementation difficulty"
```

### For Narratives
```
"Write an opening paragraph for a data story about [topic] that:
- Hooks the reader with a surprising statistic
- Provides context for why this matters
- Previews the key findings to come"
```

## 📝 Report Templates

### Quick Stats Block
```python
def format_stats_block(df):
    """Generate a formatted statistics block."""
    prompt = f"""
    Create a markdown stats block from:
    - Rows: {len(df)}
    - Columns: {list(df.columns)}
    - Date range: {df['date'].min()} to {df['date'].max()}
    - Key numeric summary: {df.describe().to_dict()}
    
    Format as a clean markdown table with emoji indicators for trends.
    """
    # Use Copilot to generate
```

### Insight Generator
```python
def generate_insights(analysis_results: dict) -> list[str]:
    """
    Generate natural language insights from analysis results.
    
    Prompt Copilot with:
    "Convert these statistical findings into plain English insights:
    - Correlation between X and Y: 0.85
    - Average value increased by 23%
    - Outliers detected in column Z
    
    Format each insight as a complete sentence explaining
    the 'so what' for a business user."
    """
    pass
```

## 🎯 Copilot Chat Commands

Use these in Copilot Chat for storytelling:

```
/doc Generate documentation for this analysis function

"Explain this correlation matrix to a marketing manager"

"What story does this time series tell about customer behavior?"

"Generate a tweet-length summary of this DataFrame's key insight"
```

## 📊 Output Examples

### Good Data Story Opening
> "Last quarter, something unexpected happened in the West region: while overall sales dipped 5%, customer satisfaction scores hit an all-time high of 94%. This paradox reveals a fundamental shift in how our customers define value..."

### Good Insight Format
> "📈 **Revenue Growth**: Q4 revenue reached $2.45M, a 23% increase YoY. This growth was primarily driven by Widget Pro sales in the West region, which alone contributed 40% of total revenue."

### Good Recommendation
> "**Recommendation #1: Expand Widget Pro Distribution** 
> *Impact*: Potential 15% revenue increase
> *Effort*: Medium (3-month rollout)
> *Rationale*: West region success suggests untapped demand in similar markets (Southwest, Pacific Northwest)"
