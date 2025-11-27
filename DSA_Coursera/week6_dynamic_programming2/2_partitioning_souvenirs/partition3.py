from sys import stdin


def partition3(values):
    if values.sum() % 3 != 0:
        return False
    target = values.sum() / 3

if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
