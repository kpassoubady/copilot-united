# Perform time series analysis or cohort analysis on the dataset
# Time series analysis
# Time series analysis is a statistical technique used to analyze
# time-ordered data.
# It is often used to forecast future values based on past observations.
# Time series analysis can help identify trends, seasonality,
# and other patterns in the data.

# Cohort analysis
# Cohort analysis is a technique used to group data into cohorts
# based on shared characteristics.

# Cohort analysis can help identify patterns and trends
# within specific groups of users or customers.
# It is often used in marketing and customer analytics
# to track customer behavior over time.
# Cohort analysis can provide insights into customer
# retention, acquisition, and engagement.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the dataset
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data


# load project1/data/us-employment.csv
file_path = "./data/us-employment.csv"
data = load_data(file_path)
print(data.head())

# Perform time series analysis
# Convert the 'date' column to datetime format
data["month"] = pd.to_datetime(data["month"])
print(data["month"])
df = pd.DataFrame(data)

# find mean, median, and mode of the 'private' column
mean = data["private"].mean()
print("Mean:", mean)
