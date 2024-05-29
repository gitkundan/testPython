import orjson
from pathlib import Path

# Define the directory containing the .bin files
data_dir = Path('C:/data')

# Use pathlib to find all .bin files in the directory
bin_files = data_dir.glob('*.bin')

# Initialize an empty master list to hold all dictionaries
final = []

# Iterate over each .bin file
for bin_file in bin_files:
    # Read the binary content of the file
    with bin_file.open('rb') as f:
        bin_data = f.read()
    
    # Convert the binary data to JSON
    try:
        json_data = orjson.loads(bin_data)
        if isinstance(json_data, list):  # Ensure the data is a list
            final.extend(json_data)  # Append dictionaries to the master list
        else:
            print(f"File {bin_file} does not contain a list of dictionaries. Skipping.")
    except orjson.JSONDecodeError as e:
        print(f"Error decoding JSON from file {bin_file}: {e}")

# Now final contains all the dictionaries from all files
print(f"Total dictionaries collected: {len(final)}")
