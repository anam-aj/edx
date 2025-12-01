"""def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product"""

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
