import json
import os

files_path = os.environ["INPUT_PATH"]
files_json = os.environ["INPUT_JSON"]
find = os.environ["INPUT_FIND"]
output_file = os.environ["GITHUB_OUTPUT"]

# Load JSON into a dictionary
files_dict = json.loads(files_json)

#  Loop through the dictionary
for object in files_dict["files"]:
    full_path = f"{files_path}/{object['file']}"

    # Read in the file
    with open(full_path, "r") as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace(find, object["replace"])

    # Write the file out again
    with open(full_path, "w") as file:
        file.write(filedata)

# Set output to use in Github Action
modified_count = len(files_dict["files"])
with open(output_file, "a") as file:
    output = f"count={modified_count}"
    file.write(output)
