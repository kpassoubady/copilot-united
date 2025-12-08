# Project 4: Data Analysis Pipeline with Python and Pandas

Duration: 3 hours 30 mins (with 20 mins break)

## Quick Start

```bash
# Navigate to the data pipeline project
cd project4/data-pipeline

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run a sample script
python src/intro_pandas.py

# Or open a notebook
jupyter notebook notebooks/intro_python.ipynb
```

## Project Structure

```
project4/
├── install/                        # Installation guides
│   ├── proj4-install-mac.md
│   └── proj4-install-win.md
├── data-pipeline/                  # Main project
│   ├── data/                       # Datasets
│   ├── notebooks/                  # Jupyter notebooks
│   │   ├── digits_classification.ipynb
│   │   ├── intro_python.ipynb
│   │   ├── read_airport.ipynb
│   │   └── temp-seattle.ipynb
│   ├── src/                        # Python scripts
│   │   ├── data_loading.py
│   │   ├── intro_pandas.py
│   │   ├── user_engagement.py
│   │   └── ...
│   ├── output/                     # Analysis results
│   └── requirements.txt
└── Readme.md
```

## Related Resources

- **Breakout Exercises**: [python-data-analysis-exercise/](../python-data-analysis-exercise/)
- **Installation Guide**: [macOS](./install/proj4-install-mac.md) | [Windows](./install/proj4-install-win.md)

## Tasks

### 1. Data Loading and Preprocessing

* Load a large dataset using Pandas.
* Handle missing values and perform data cleaning.
* Transform data as needed (e.g., normalization, encoding).
* Use Copilot to assist in writing functions for data cleaning (handling missing values,removing duplicates)

### 2. Exploratory Data Analysis (EDA)

* Perform descriptive statistics.
* Generate visualizations to uncover insights (e.g., histograms, scatter plots).

### 3. Visualization

* Use Matplotlib or Seaborn to create visualizations.
* Plot relationships between variables and highlight key findings.

### 4. Advanced Analysis

* Perform time series analysis or cohort analysis
* Use Copilot to help write complex data aggregation and transformation operations

### 5. Summary Report

* Generate a summary report of the analysis.
* Use Jupyter Notebook to present the findings (optional).

## 1. Target Audience

* Junior and Intermediate Data Analysts: Professionals who have some experience with data analysis but are looking to  improve their efficiency and productivity using GitHub Copilot.
* Software Engineers or Developers: Those who want to integrate data analysis capabilities into their projects.
* Data Science Enthusiasts: Beginners or intermediate learners looking to build their skills in data wrangling, visualization, and analysis, while leveraging AI tools like GitHub Copilot..

## 2. Summary of Agenda and Benefits

### Data Loading and Preprocessing (40 minutes)

* Introduction to using Pandas for loading large datasets and preprocessing (missing values, encoding).
* How GitHub Copilot assists in creating efficient data-cleaning functions, saving time in mundane tasks.
* Benefits: Increased productivity in cleaning and preparing data by automating repetitive tasks like removing duplicates, filling missing values, etc.

### Exploratory Data Analysis (EDA) (50 minutes)

* Conducting descriptive statistics to uncover trends, distributions, and anomalies.
* Use GitHub Copilot to generate quick insights and visualizations like histograms, scatter plots, etc.
* Benefits: Reduces the manual effort required for generating visualizations, enabling faster iteration and discovery of patterns in data.

### Visualization (45 minutes)

* Utilizing Matplotlib or Seaborn for creating clear and insightful data visualizations.
* Copilot helps write plotting functions quickly, especially when dealing with multiple variables.
* Benefits: Users will experience how Copilot can suggest optimized code for visualizations and improve workflow by reducing time spent on repetitive plotting tasks.

### Advanced Analysis (50 minutes)

* Performing advanced data aggregation techniques, time series analysis, and cohort analysis.
* GitHub Copilot can assist with complex data operations such as pivoting tables,
performing rolling statistics, etc.
* Benefits: Learn how Copilot can streamline writing complex operations and handle
advanced analysis with less manual coding effort.

### Summary Report (25 minutes)

* Generate a final report of the findings using Pandas and Jupyter Notebook.
* Copilot assists in the creation of markdown summaries or sections of the analysis, especially useful for preparing presentations or reports.
* Benefits: Automates the creation of structured reports, ensuring that the time spent on
documentation is minimized.

## 3. Participation Requirements

* Basic Knowledge of Python programming (understanding of variables, loops, and functions).
* Familiarity with Pandas: Participants should have used Pandas before, at least for basic data loading and manipulation.
* Basic Understanding of Data Analysis: Should have some experience in handling datasets,
performing descriptive statistics, and creating visualizations.
* Environment Setup: Participants should have Python installed along with Jupyter Notebook and libraries like Pandas, Matplotlib, and Seaborn.
* GitHub Copilot Access: Participants should have GitHub Copilot enabled in their IDE (such as VSCode) to follow along with the session.
