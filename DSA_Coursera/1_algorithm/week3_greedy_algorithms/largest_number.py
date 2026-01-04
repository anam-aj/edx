from itertools import permutations


def largest_number_naive(numbers):
    sorted_numbers = sorted(numbers, key=lambda n: str(n) * 5, reverse=True)
    largest = "".join(str(n) for n in sorted_numbers)

    return largest


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))
