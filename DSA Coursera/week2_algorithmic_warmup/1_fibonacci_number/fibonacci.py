def fibonacci_number(n):
    first_number = 0
    second_number = 1

    if n == 1:
        return first_number
    elif n == 2:
        return second_number
    elif n > 2:
        for number in range(2, n):
             next_number = first_number + second_numbr




if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
