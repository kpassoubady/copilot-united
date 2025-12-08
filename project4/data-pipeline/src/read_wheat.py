import pandas as pd
import matplotlib.pyplot as plt


# Load the dataset
def load_json(file_path):
    data = pd.read_json(file_path)
    return data


# load airport.csv file
file_path = "./data/wheat.json"
data = load_json(file_path)
print("First 5 rows of the dataset")
print(data.head())
print("Display the entire dataset")
print(data.to_string())

data.info()

data.plot(kind="hist", x="year", y="wages")
plt.show()

data.plot(kind="scatter", x="year", y="wheat")
plt.show()
