# what is pandas library in python?
# Pandas is a Python library that provides data structures and data analysis tools. It is built on top of the NumPy library and provides easy-to-use data structures like Series and DataFrame for working with structured data. Pandas is widely used for data manipulation, cleaning, and analysis in Python.

# who created pandas library?
# Pandas was created by Wes McKinney in 2008 while working at AQR Capital Management. It was developed to address the need for a powerful data analysis tool in Python that could handle structured data effectively.

# what are the main data structures in pandas?
# The main data structures in Pandas are:
# Series: A one-dimensional labeled array capable of holding any data type.
# DataFrame: A two-dimensional labeled data structure with columns of potentially different types.
# These data structures are used to represent and work with structured data in Pandas.

# what the name "Pandas" stands for?
# The name "Pandas" is derived from the term "panel data," which refers to multidimensional structured data sets commonly used in statistics and econometrics. The name reflects the library's focus on handling structured data effectively.

import pandas as pd

# create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# print pandas version
print("Pandas version:", pd.__version__)

# check the data type of each column
print("Data types of each column:")
print(df.dtypes)    

# check the shape of the DataFrame
print("Shape of the DataFrame:", df.shape)

# check the number of rows in the DataFrame
print("Number of rows in the DataFrame:", len(df))

# check the column names
print("Column names:")
print(df.columns)

# check the index of the DataFrame
print("Index of the DataFrame:")    
print(df.index)

# check the summary statistics of the DataFrame
print("Summary statistics:")
print(df.describe())

# check the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head())

# check the last few rows of the DataFrame
print("Last few rows of the DataFrame:")
print(df.tail())

# check the values in a specific column
print("Values in the 'Name' column:")
print(df['Name'])

# check the unique values in a specific column
print("Unique values in the 'City' column:")
print(df['City'].unique())

# check the frequency of each value in a specific column
print("Value counts in the 'City' column:")
print(df['City'].value_counts())

# check the values in a specific row
print("Values in the first row:")
print(df.iloc[0])

# check the values in a specific location
print("Value at row 1, column 'Name':")
print(df.at[1, 'Name'])


# check the values in a specific row and column
print("Value at row 2, column 'Age':")
print(df.at[2, 'Age'])

# create a sample series with a single column
s = pd.Series([1, 2, 3, 4, 5])
print("Sample Series:")
print(s)

# create a sample series with mixed data types
s = pd.Series([1, 'Alice', 3.5, True])
print("Mixed Data Types Series:")
print(s)

# create a sample DataFrame with mixed data types
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [85.5, 90.0, 88.5],
    'Passed': [True, False, True]
}

df = pd.DataFrame(data)
print("Mixed Data Types DataFrame:")
print(df)
print(df.info())
