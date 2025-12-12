import pandas as pd
import matplotlib.pyplot as plt


# Load the dataset
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data


# load airport.csv file
file_path = "./data/airports.csv"
data = load_data(file_path)
print(data.head())


# Handle missing values
def handle_missing_values(data):
    """
    Handle missing values in the given DataFrame.

    This function checks for missing values in the DataFrame, prints the count of missing values for each column,
    and then drops all rows that contain any missing values.

    Parameters:
    data (pandas.DataFrame): The input DataFrame to process.

    Returns:
    pandas.DataFrame: The DataFrame with rows containing missing values removed.
    """
    # Check for missing values
    missing_values = data.isnull().sum()
    print(missing_values)
    # Drop rows with missing values
    data = data.dropna()
    return data


# Handle missing values in the dataset
data = handle_missing_values(data)
print(data.head())

# find the mean, median, and mode of the 'elevation_ft' column
mean = data["longitude"].mean()
median = data["longitude"].median()
mode = data["longitude"].mode()
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)


# find duplicates
def find_duplicates(data):
    # Check for duplicates
    duplicates = data.duplicated().sum()
    print(duplicates)
    return duplicates


# Find duplicates in the dataset
duplicates = find_duplicates(data)
print("Number of duplicates:", duplicates)


# remove duplicates
def remove_duplicates(data):
    # Check for duplicates
    duplicates = data.duplicated()
    print("Duplicate set")
    print(duplicates)
    # Remove duplicates
    data = data.drop_duplicates()
    return data


# Remove duplicates in the dataset
data = remove_duplicates(data)
print("Duplicate set removed")
print(data.head())

# find the correlation between 'latitude' and 'longitude' columns
correlation = data["latitude"].corr(data["longitude"])
print("Correlation between latitude and longitude:", correlation)
data.plot(x="latitude", y="longitude", kind="scatter")
plt.title("Scatter plot of latitude vs longitude")
plt.show()
