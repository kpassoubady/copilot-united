import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates


def load_data(file_path):
    data = pd.read_csv(file_path)
    return data


#   load project1/data/user_engagement.csv
file_path = "./data/user_engagement.csv"
data = load_data(file_path)
print(data.head())

# Perform cohort analysis
# Convert the 'date' column to datetime format
data["login_date"] = pd.to_datetime(data["login_date"])
print(data["login_date"])
data["year"] = data["login_date"].dt.year
data["month"] = data["login_date"].dt.month
data["day"] = data["login_date"].dt.day


# Create a cohort based on the year and month of the first login
if "login_date" in data.columns:
    # Calculate the cohort based on the first login date
    data["cohort"] = pd.to_datetime(
        data.groupby("user_id")["login_date"].transform("min")
    )
    # Extract the year and month from the cohort
    data["cohort_year"] = data["cohort"].dt.year
    data["cohort_month"] = data["cohort"].dt.month

    # Calculate the cohort index
    data["cohort_index"] = (
        (data["year"] - data["cohort_year"]) * 12
        + (data["month"] - data["cohort_month"])
        + 1
    )

    # Calculate the number of unique users in each cohort
    cohort_data = (
        data.groupby(["cohort", "cohort_index"])["user_id"].nunique().reset_index()
    )

    # Plot the cohort analysis
    plt.figure(figsize=(12, 8))
    plt.title("Cohort Analysis")
    sns.heatmap(
        cohort_data.pivot(index="cohort", columns="cohort_index", values="user_id"),
        annot=True,
        fmt=".0f",
        cmap="YlGnBu",
    )
    plt.xlabel("Cohort Index")
    plt.ylabel("Cohort")
    plt.xticks(rotation=45)

    # Format the x-axis tick labels to display only the date component
    plt.gca().yaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))

    # plt.show()

# Calculate the retention rate
# Calculate the total number of users in each cohort
cohort_size = data.groupby("cohort")["user_id"].nunique()
print(cohort_size)

# Generate a summary report of the analysis
summary = cohort_data.pivot(
    index="cohort", columns="cohort_index", values="user_id"
).divide(cohort_size, axis=0)
print(summary)


# Save the summary report to a CSV file
summary.to_csv("./result/cohort_summary.csv")
print("Summary report saved to ./result/cohort_summary.csv")

