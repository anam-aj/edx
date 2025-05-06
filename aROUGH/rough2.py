import pandas as pd

# Load the dataset (replace 'your_dataset.csv' with the file path)
file_path = 'sample_dataset.csv'
data = pd.read_csv(file_path)

# Print all the columns (features) of the dataset
print("Features (Columns) in the dataset:")
print(data.columns)

# Compute and display descriptive statistics for numeric columns
print("\nDescriptive Statistics:")
numeric_columns = data.select_dtypes(include=['number'])  # Select numeric columns

for column in numeric_columns.columns:
    print(f"\nFeature: {column}")
    print(f"Maximum: {numeric_columns[column].max()}")
    print(f"Minimum: {numeric_columns[column].min()}")
    print(f"Mean: {numeric_columns[column].mean()}")
    print(f"Median: {numeric_columns[column].median()}")
    print(f"Count: {numeric_columns[column].count()}")
    print(f"Variance: {numeric_columns[column].var()}")
    print(f"Standard Deviation: {numeric_columns[column].std()}")
