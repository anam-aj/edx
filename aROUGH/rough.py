import csv

# Open CSV file
with open ("shopping.csv") as file:
    rows = csv.reader(file)
    count = 0
    for row in rows:
        if count < 5:
            print(row)
            count += 1
