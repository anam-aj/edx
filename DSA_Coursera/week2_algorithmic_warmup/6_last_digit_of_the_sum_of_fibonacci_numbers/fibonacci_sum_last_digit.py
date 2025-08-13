def fibonacci_sum(n):
    if n < 1:
        return 0

    previous, current, _sum = 0, 1, 1
    modulo_of_pre_cur_sum = [(0, 1, 1)]
    repeat_after = 1

    if n < (10 ** 3):
        small = n
    else:
        small = 10 ** 3

    for _ in range(1, small):
        previous, current = current, previous + current
        _sum = _sum + current
        previous %= 10
        current %= 10
        _sum %= 10
        current_modulo_of_pre_cur_sum = (previous, current, _sum)
        if current_modulo_of_pre_cur_sum == (0, 1, 1):
            break
        else:
            modulo_of_pre_cur_sum.append(current_modulo_of_pre_cur_sum)
            repeat_after += 1

    index = n % repeat_after
    return modulo_of_pre_cur_sum[index - 1][2]


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))
