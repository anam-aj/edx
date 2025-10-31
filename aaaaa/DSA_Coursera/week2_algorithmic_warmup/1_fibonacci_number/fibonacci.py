def fibonacci_number(n):
    first_number = 0
    second_number = 1

    if n == 0:
        return first_number
    elif n > 0:
        for _ in range(1, n):
            next_number = first_number + second_number
            first_number = second_number
            second_number = next_number

        return second_number


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
