    # Empty dictionary to hold each list as a key-value pair
    # key = columnname, value = list of correspondig values from all rows
    data = {}

    # Open CSV file
    with open (filename) as file:
        rows = csv.DictReader(file)

        # Add column names to 'data' as keys
        columns = rows.keys()
        for name in columns:
            data[name] = []

        # Populate the columns(keys) in 'data' with values
        for row in rows:
            for col, val in row.items:
                data[col].append(val)
