from sys import stdin


def maximum_gold(capacity, weights):

    dp_value = []

    for m in range(len(weights) + 1):
        dp_value.append([0])
        for n in range(capacity):
            dp_value[m].append(0)

    for item in range(1, len(weights) + 1):
        weight_i = weights[item - 1]
        for current_capacity in range(1, capacity + 1):
            dp_value[item][current_capacity] = dp_value[item - 1][current_capacity]
            if weight_i <= current_capacity:
                val = dp_value[item - 1][current_capacity - weight_i] + weight_i
                if dp_value[item][current_capacity] < val:
                    dp_value[item][current_capacity] = val

    return dp_value[len(weights)][capacity]


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
