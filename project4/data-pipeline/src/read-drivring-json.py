import json
import os

# Load the JSON file
file_path = os.path.join(os.path.dirname(__file__), 'data', 'driving.json')
with open(file_path, 'r') as file:
    data = json.load(file)

# Print the number of objects in the array
print("Number of objects in the array:", len(data))