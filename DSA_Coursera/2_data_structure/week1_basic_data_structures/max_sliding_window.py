# python3


def max_sliding_window_naive(sequence, m):
    maximums = []

    if len(sequence) == 1:
        return sequence

    if sequence[0] > sequence[1]:
        maximum = sequence[0]
        second_maximum = sequence[1]
        maximum_count = 1
        second_maximum_count = 1
    elif sequence[0] == sequence[1]:
        maximum = sequence[0]
        second_maximum = float('inf')
        maximum_count = 2
        second_maximum_count = 0
    else:
        maximum = sequence[1]
        second_maximum = sequence[0]
        maximum_count = 1
        second_maximum_count = 1


    for i in range(2, m):
        if sequence[i] > maximum:
            second_maximum = maximum
            second_maximum_count = maximum_count
            maximum = sequence[i]
            maximum_count = 1
        elif sequence[i] == maximum:
            maximum_count += 1
        elif sequence[i] > second_maximum:
            second_maximum = sequence[i]
            second_maximum_count = 1
        elif sequence[i] == maximum:
            second_maximum_count += 1

    maximums.append(maximum)

    for i in range(m, len(sequence)):
        first_element = sequence[i - m]
        if first_element == maximum:
            


    return maximums


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))
