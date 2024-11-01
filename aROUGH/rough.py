from tabulate import tabulate

data = [['Ghost', 100], ['Zombie', 200]]
print(tabulate(data, headers=['Name', 'Age']))
