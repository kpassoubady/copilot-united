import DataLoader as dl

file_path = "./data/random_names.csv"
data = dl.DataLoader.read_csv(file_path)
if data is not None:
    print(data.head())
