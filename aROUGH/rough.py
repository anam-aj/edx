weights = [1, 3, 4, 4, 5]
capacity = 3

dp_value = []

for m in range(len(weights) + 1):
    dp_value.append([0])
    for n in range(capacity):
        dp_value[m].append(0)

print(dp_value)
