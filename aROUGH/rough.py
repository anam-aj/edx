import csv

# Empty dictionary to hold each list as a key-value pair
# key = columnname, value = list of correspondig values from all rows
data = {}
rows = {}

# Open CSV file
with open ("shopping.csv") as file:
    rows = list(csv.DictReader(file))

# Add column names to 'data' as keys
columns = rows[0].keys()
for name in columns:
    data[name] = []

# Populate the columns(keys) in 'data' with values
for row in rows:
    for col, val in row.items():
        data[col].append(val)

count = 0
for key, value in data.items():
    print(key)
    print(data[key][0:4])


