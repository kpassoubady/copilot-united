# Data Loading and Preprocessing
# Load a large dataset using Pandas.
# Handle missing values and perform data cleaning.
# Transform data as needed (e.g., normalization, encoding).
# Use Copilot to assist in writing functions for data cleaning
# (handling missing values,removing duplicates)

import pandas as pd


# Load the dataset
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data


# load random_names.csv file
file_path = "./data/random_names.csv"
data = load_data(file_path)
print(data.head())


# Handle missing values
def handle_missing_values(data):
    # Check for missing values
    missing_values = data.isnull().sum()
    print(missing_values)
    # Drop rows with missing values
    data = data.dropna()
    return data


# Handle missing values in the dataset
data = handle_missing_values(data)
print(data.head())


# remove duplicates
def remove_duplicates(data):
    # Check for duplicates
    duplicates = data.duplicated().sum()
    print(duplicates)
    # Remove duplicates
    data = data.drop_duplicates()
    return data


## Remove duplicates in the dataset
data = remove_duplicates(data)
print(data.head())
