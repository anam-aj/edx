from itertools import permutations


def max_dot_product(first_sequence, second_sequence):
    max_product = 0
    sorted_1st = sorted(first_sequence)
    sorted_2nd = sorted(second_sequence)
    for i in range(len(sorted_1st)):
        current_product = sorted_1st[i] * sorted_2nd[i]
        max_product += current_product
        
    return max_product


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))

