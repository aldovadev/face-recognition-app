import json
import os

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


# Step 2: Clear all files inside the "Samples" folder
folder_samples = "Samples"
for file_sample in os.listdir(folder_samples):
    file_path_sample = os.path.join(folder_samples, file_sample)
    try:
        if os.path.isfile(file_path_sample):
            os.unlink(file_path_sample)
    except Exception as e:
        print(f"Error deleting {file_path_sample}: {e}")

print(f"Files in '{folder_samples}' cleared.")
