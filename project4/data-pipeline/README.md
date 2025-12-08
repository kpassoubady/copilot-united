# Data Analysis Pipeline

A data analysis project demonstrating Python, Pandas, and data visualization techniques with GitHub Copilot assistance.

## Directory Structure

```
data-pipeline/
├── data/                   # Input datasets (CSV, JSON, etc.)
├── notebooks/              # Jupyter notebooks for interactive analysis
│   ├── digits_classification.ipynb
│   ├── intro_python.ipynb
│   ├── read_airport.ipynb
│   └── temp-seattle.ipynb
├── src/                    # Python scripts and modules
│   ├── data_loading.py     # Data loading utilities
│   ├── intro_pandas.py     # Pandas introduction
│   ├── user_engagement.py  # User engagement analysis
│   └── ...
├── output/                 # Analysis results and generated files
├── requirements.txt        # Python dependencies
└── README.md
```

## Setup

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Running Notebooks

```bash
# Start Jupyter
jupyter notebook notebooks/

# Or use JupyterLab
jupyter lab
```

## Running Scripts

```bash
# Run a specific analysis script
python src/intro_pandas.py

# Run data loading example
python src/data_loading.py
```

## Technology Stack

- **Python**: 3.9+
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **Machine Learning**: Scikit-learn (for classification examples)
- **Notebooks**: Jupyter

## GitHub Copilot Learning Objectives

Use this project to practice:
1. **Data Loading**: Generate file reading functions
2. **Data Cleaning**: Create preprocessing pipelines
3. **EDA**: Generate descriptive statistics code
4. **Visualization**: Create plots and charts
5. **Analysis**: Write aggregation and transformation code
