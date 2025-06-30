import csv

# Open CSV file
with open ("shopping.csv") as file:
    rows = csv.reader(file)
    count = 0
    header = next(rows)
    print (header)

