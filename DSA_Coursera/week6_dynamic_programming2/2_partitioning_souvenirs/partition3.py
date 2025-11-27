from sys import stdin
import copy


def partition3(values):
    if sum(values) % 3 != 0:
        return False
    target = sum(values) // 3

    for value in values:
        if value > target:
            return False

    dp_table = [[False] * (target + 1) for _ in range(target + 1)]
    dp_table[0][0] = True

    for value in values:
        new_dp = [row[:] for row in dp_table]

        for s1 in range(target + 1):
            for s2 in range(target + 1):

                if dp_table[s1][s2]:
                    if s1 + value <= target:
                        new_dp[s1 + value][s2] = True
                    if s2 + value <= target:
                        new_dp[s1][s2 + value] = True

        dp_table = new_dp

    return dp_table[target][target]


if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
