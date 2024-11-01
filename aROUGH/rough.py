from tabulate import tabulate
from termcolor import colored

data = [
    ["Red", "Apple"],
    ["Green", "Lime"],
    ["Blue", "Berry"]
]

table = tabulate(data, headers=["Color", "Fruit"])
colored_table = colored(table, 'blue')  # This will color the table blue

print(table)
print(colored_table)
