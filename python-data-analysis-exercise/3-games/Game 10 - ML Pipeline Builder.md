# 🤖 ML Pipeline Builder

## 🎯 Objective

Build end-to-end machine learning pipelines using GitHub Copilot, from data preparation to model evaluation.

## 🎮 Game Format

Construct ML pipelines of increasing complexity, learning to leverage Copilot for each step.

## 🔧 Pipeline Stages

### Stage 1: Data Preparation (15 minutes)

**Challenge 1.1**: Train-Test Split
```python
# Split data with:
# - 80% train, 20% test
# - Stratified by target (for classification)
# - Random state for reproducibility
```

**Challenge 1.2**: Feature Engineering
```python
# Use Copilot to:
# - Create polynomial features
# - One-hot encode categoricals
# - Scale numeric features
# - Handle datetime features
```

**Challenge 1.3**: Pipeline with Preprocessing
```python
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

# Create a preprocessing pipeline that:
# - Scales numeric columns
# - One-hot encodes categorical columns
# - Imputes missing values appropriately
```

---

### Stage 2: Model Selection (15 minutes)

**Challenge 2.1**: Classification Pipeline
```python
# Build a pipeline for binary classification:
# - Preprocessing
# - Feature selection
# - Logistic Regression or Random Forest
```

**Challenge 2.2**: Regression Pipeline
```python
# Build a pipeline for regression:
# - StandardScaler
# - Linear Regression / Ridge / Lasso
```

**Challenge 2.3**: Model Comparison
```python
# Compare multiple models:
# - Use cross-validation
# - Track metrics for each
# - Select best performer
```

---

### Stage 3: Evaluation (15 minutes)

**Challenge 3.1**: Classification Metrics
```python
# Generate:
# - Confusion matrix visualization
# - Precision, recall, F1 score
# - ROC curve and AUC
# - Classification report
```

**Challenge 3.2**: Regression Metrics
```python
# Calculate and visualize:
# - RMSE, MAE, R²
# - Residual plot
# - Predicted vs Actual scatter
```

**Challenge 3.3**: Cross-Validation Report
```python
# Create a comprehensive CV report with:
# - Mean and std of scores
# - Fold-by-fold breakdown
# - Learning curves
```

---

### Stage 4: Complete Pipeline (20 minutes)

**The Ultimate Challenge**: Build a full ML pipeline class

```python
class AutoMLPipeline:
    """
    Automated ML Pipeline using scikit-learn.
    
    Use Copilot to implement:
    - fit(): Preprocess, select features, train model
    - predict(): Apply same transformations, generate predictions
    - evaluate(): Return comprehensive metrics
    - explain(): Feature importances and SHAP values
    """
    
    def __init__(self, task='classification'):
        self.task = task
        self.pipeline = None
        self.metrics = {}
    
    # Let Copilot build the rest!
```

## 🏆 Scoring

| Component | Points |
|-----------|--------|
| Proper train-test split | 10 |
| Preprocessing pipeline | 20 |
| Model training | 20 |
| Evaluation metrics | 20 |
| Cross-validation | 15 |
| Complete pipeline class | 30 |

## 💡 Copilot Prompts for ML

### Preprocessing
```
"Create a scikit-learn ColumnTransformer that:
1. Scales numeric columns: ['age', 'income', 'score']
2. One-hot encodes categorical columns: ['category', 'region']  
3. Passes through binary columns unchanged: ['is_premium']
Use Pipeline to chain with an imputer for missing values"
```

### Model Building
```
"Create a classification pipeline with:
1. StandardScaler for numeric features
2. OneHotEncoder for categorical features
3. SelectKBest for feature selection (k=10)
4. RandomForestClassifier with 100 estimators
Wrap everything in a Pipeline for easy fit/predict"
```

### Evaluation
```
"Write a function that takes y_true and y_pred for classification and returns:
1. Accuracy, precision, recall, F1 (as dict)
2. Confusion matrix as a styled heatmap
3. ROC curve plot with AUC in legend
4. Classification report as formatted string"
```

### Hyperparameter Tuning
```
"Create a GridSearchCV setup for RandomForestClassifier:
- n_estimators: [50, 100, 200]
- max_depth: [5, 10, 20, None]
- min_samples_split: [2, 5, 10]
Use 5-fold cross-validation and F1 as scoring metric
Return best parameters and best score"
```

## 📊 Code Templates

### Basic Pipeline
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Simple pipeline
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression())
])

pipe.fit(X_train, y_train)
predictions = pipe.predict(X_test)
```

### Column Transformer
```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

numeric_features = ['age', 'income']
categorical_features = ['category', 'region']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(drop='first'), categorical_features)
    ]
)
```

### Complete Pipeline with Preprocessing
```python
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

full_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Fit and evaluate
full_pipeline.fit(X_train, y_train)
y_pred = full_pipeline.predict(X_test)
```

### Evaluation Function
```python
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

def evaluate_classifier(y_true, y_pred, y_prob=None):
    """Comprehensive classification evaluation."""
    # Use Copilot to:
    # 1. Print classification report
    # 2. Plot confusion matrix
    # 3. Plot ROC curve if probabilities provided
    # 4. Return metrics dict
    pass
```

## 🎯 Bonus Challenge: Pipeline Serialization

```python
import joblib

def save_pipeline(pipeline, filepath: str):
    """Save trained pipeline to disk."""
    # Copilot: implement with joblib
    pass

def load_pipeline(filepath: str):
    """Load pipeline from disk."""
    # Copilot: implement loading
    pass

def pipeline_to_api(pipeline):
    """
    Copilot challenge: Create a FastAPI endpoint 
    that serves predictions from this pipeline.
    """
    pass
```

## 📚 Resources

- [Scikit-learn Pipeline Guide](https://scikit-learn.org/stable/modules/compose.html)
- [Column Transformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html)
- [Model Selection Guide](https://scikit-learn.org/stable/model_selection.html)
