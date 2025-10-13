def compute_operations(n):

    min_steps = [0]
    steps = [[], [1], ]

    for num in range(2, n + 1):
        steps.append([])
        if num - 1 > 0:
            ...
        if num % 2 == 0:
            ...
        if num % 3 == 0:
            ...




    for

    return []


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
