import csv

# Define the data to be written into the CSV file
data = [
    ["Name", "Age", "Salary", "Gender", "Department"],
    ["Alice", 25, 50000, "F", "HR"],
    ["Bob", 30, 60000, "M", "IT"],
    ["Charlie", 22, 40000, "M", "Finance"],
    ["Diana", 28, 55000, "F", "Marketing"],
    ["Eve", 35, 70000, "F", "IT"],
]

# Specify the file name
file_name = "sample_dataset.csv"

# Write the data to a CSV file
with open(file_name, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"Sample CSV file '{file_name}' created successfully!")
