# 1. Write a Python script to read a CSV file with missing values and replace the missing values with a default value (e.g., "Unknown" or 0).Sample Data (missing_data.csv):

import csv
import json

def fill_missing_values(input_file, output_file, default_values):
    # Read CSV file
    with open(input_file, mode='r', newline='') as infile:
        reader = csv.reader(infile)
        header = next(reader)  # Read the header
        rows = []
        
        for row in reader:
            filled_row = [row[i] if row[i].strip() else default_values.get(header[i], "Unknown") for i in range(len(row))]
            rows.append(filled_row)
    
    # Write cleaned data to new CSV file
    with open(output_file, mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)
        writer.writerows(rows)
    
    print(f"Missing values replaced. Cleaned data saved to {output_file}")

# Define default values for missing data
default_values = {"Name": "Unknown", "Age": "0", "City": "Unknown"}

# Process the CSV file
fill_missing_values("D:/Python course/Questions LAB/Lab question/missing_data.csv", "D:/Python course/Questions LAB/Lab question/cleaned_data.csv", default_values)


# ------------------------------------------------>

# 2 Write a Python script to validate JSON data by checking if it contains required fields and if the data types are correct (e.g., integers for IDs, strings for names). Sample Data (data.json):

def validate_json(file_path, required_fields):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    errors = []
    for i, item in enumerate(data):
        for field, field_type in required_fields.items():
            if field not in item:
                errors.append(f"Missing field '{field}' in item {i}")
            elif not isinstance(item[field], field_type):
                errors.append(f"Incorrect type for '{field}' in item {i}. Expected {field_type.__name__}, got {type(item[field]).__name__}")
    
    if errors:
        print("Validation errors:")
        for error in errors:
            print(error)
    else:
        print("JSON data is valid.")

# Define required fields and their expected data types
required_fields = {
    "Product ID": int,
    "Name": str,
    "Price": float
}

# Validate the JSON file
validate_json("D:/Python course/Questions LAB/Lab question/data.json", required_fields)
