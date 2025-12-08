# Data Analysis Pipeline with Python and Pandas

## Objective

To build a data analysis pipeline using the `cars.json` dataset, practicing data cleaning, exploratory data analysis (EDA), and visualization while leveraging GitHub Copilot to enhance productivity.

## Task 1: Data Loading and Preprocessing

**Instructions:**

* Load the dataset `cars.json` using Pandas.
* Display the first five rows to understand the structure of the data.
* Remove duplicate rows, if any.
* Handle missing values:
  * Replace missing `Miles_per_Gallon` with the median value.
  * For `Horsepower`, replace missing values with the mean.
  * For `Origin`, replace missing values with 'Unknown'
* Add a new column `Power-to-Weight Ratio` calculated as `Horsepower / Weight_in_lbs`.
  * For `Power-to-Weight Ratio` with NaN values replace with 0

**Expected Output:**

Save the cleaned dataset with no missing values and the new column added as cars_processed.csv in result directory

## Task 2: Exploratory Data Analysis (EDA)

**Instructions:**

* Generate descriptive statistics for the dataset (mean, median, standard deviation, etc.).
* Group cars by `Origin` and calculate the average `Miles_per_Gallon` for each group.
* Identify the car with the highest `Power-to-Weight Ratio`.
* Write a function to return the top 5 cars with the highest `Miles_per_Gallon`.

**Expected Output:**

Insights about the dataset, such as average MPG by region and high-performance cars.

## Task 3: Visualization

**Instructions:**

* Create a bar chart showing the average `Miles_per_Gallon` for each `Origin`.
* Plot a scatter plot comparing `Horsepower` and `Miles_per_Gallon`.
* Save the scatter plat as `horsepower_vs_miles_per_gallon.jpeg` a JPEG file in the result directory
* Generate a histogram for `Weight_in_lbs` to analyze the distribution.
* Save the histogram as a PNG file named `Weight_in_lbs_histogram.png` in the result directory

**Expected Output:**

* Informative visualizations illustrating key dataset features.
* Saved scatter and histogram figures in the result directory.

## Task 4: Advanced Analysis

**Instructions:**

* Perform a cohort analysis: Group cars by `Year` and calculate the average `Miles_per_Gallon` per year.
* Write a function to filter cars with `Power-to-Weight Ratio` above a threshold.
* Display min and max value of `Power-to-Weight Ratio`
* Filter the cars with `Power-to-Weight Ratio` above 0.03
* Use GitHub Copilot to assist with writing complex Pandas operations, such as pivoting and aggregating data.
  * Pivot the data to create a pivot table with `Year` as the index and `Origin` as the columns, and `Miles_per_Gallon` as the values.
  * Aggregate the data with median to create a pivot table with `Year` as the index and `Origin` as the columns, and `Miles_per_Gallon` as the values.

**Expected Output:**

Detailed analysis on trends over time and high-performance car categories.

## Task 5: Summary Report

**Instructions:**

* Compile all findings and visualizations into a well-structured Jupyter Notebook report.
* Write markdown cells summarizing:
  * Dataset cleaning and preparation.
  * Key insights from EDA and visualizations.
  * Advanced analysis results.

**Expected Output:**

A comprehensive and well-documented Jupyter Notebook ready for presentation.

## Bonus

* Experiment with GitHub Copilot's suggestions for customizing visualizations.
* Use Copilot to create a function that identifies outliers in the dataset based on `Miles_per_Gallon`.
