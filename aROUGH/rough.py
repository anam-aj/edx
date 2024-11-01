from tabulate import tabulate

data = [
    ["\033[91mRed\033[0m", "Apple"],
    ["\033[92mGreen\033[0m", "Lime"],
    ["\033[94mBlue\033[0m", "Berry"]
]

print(tabulate(data, headers=["Color", "Fruit"]))
