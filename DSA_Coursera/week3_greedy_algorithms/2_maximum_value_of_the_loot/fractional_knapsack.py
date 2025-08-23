from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0.0

    sorted_indices = sorted(range(len(weights)), key=lambda i: values[i]/weights[i], reverse=True)

    for i in sorted_indices:
        if capacity <= 0:
            return value
        else:
            weight = weights[i]

            if weight <= capacity:
                value += (values[i])
            else:
                value += ((capacity/weight) * values[i])

            capacity -= weight

    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
