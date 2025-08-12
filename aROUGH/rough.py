a = [1, 2, 3]
a, b, c = a

print(a, b, c)
def max_pairwise_product(numbers):
    n = len(numbers)

    if numbers[0] > numbers[1]:
        highest = numbers[0]
        second_highest = numbers[1]
    else:
        highest = numbers[1]
        second_highest = numbers[0]

    for index in range(2, n):
        if numbers[index] > highest:
            second_highest = highest
            highest = numbers[index]
        elif numbers[index] > second_highest:
            second_highest = numbers[index]

    return (highest * second_highest)

if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
