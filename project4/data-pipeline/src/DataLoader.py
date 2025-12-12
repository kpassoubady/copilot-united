import pandas as pd


class DataLoader:
    @staticmethod
    def read_csv(file_path):
        try:
            return pd.read_csv(file_path)
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
        except pd.errors.EmptyDataError:
            print(f"Error: The file {file_path} is empty.")
        except pd.errors.ParserError:
            print(f"Error: The file {file_path} could not be parsed.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    @staticmethod
    def read_json(file_path):
        try:
            return pd.read_json(file_path)
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
        except ValueError:
            print(f"Error: The file {file_path} could not be parsed.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


# Usage in data_loading.py
file_path = "./data/random_names2.csv"
data = DataLoader.read_csv(file_path)
if data is not None:
    print(data.head())

# Usage in read_wheat.py
# file_path = "./data/some_json_file.json"
# data = DataLoader.read_json(file_path)
# if data is not None:
#     print(data.head())
