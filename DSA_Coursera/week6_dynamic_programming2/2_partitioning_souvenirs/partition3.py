from sys import stdin


def partition3(values):
    if values.sum() % 3 != 0:
        return False
    target = values.sum() // 3

    for value in values:
        if value > target:
            return False

    dp_table = [[False] * (target + 1) for _ in range(target + 1)]
    dp_table[0][0] = True

    for value in values:
        new_dp = 

    for s1 in range(target + 1):
        for s2 in range(target + 1):


if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
