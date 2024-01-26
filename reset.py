import json
import shutil

filename = "names.json"

# Step 1: Read existing JSON data from the file
try:
    with open(filename, "r") as file:
        json_array = json.load(file)
except FileNotFoundError:
    print(f"File '{filename}' not found.")
    json_array = []

# Step 2: Clear the JSON array (set it to an empty list)
json_array = []

# Step 3: Write the updated JSON data back to the file
with open(filename, "w") as file:
    json.dump(json_array, file, indent=2)

print(f"Data in '{filename}' cleared.")


folder_samples = "Samples"

try:
    shutil.rmtree(folder_samples)
except Exception as e:
    print(f"Error deleting {folder_samples}: {e}")

print(f"Folder '{folder_samples}' deleted.")
