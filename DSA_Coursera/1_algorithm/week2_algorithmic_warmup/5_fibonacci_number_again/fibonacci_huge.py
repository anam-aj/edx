def fibonacci_huge_naive(n, m):

    if n < 1:
        return n

    previous = 0
    current = 1
    repeat_after = 1

    if n < (m * m):
        small = n
    else:
        small = m * m

    modulo = [(0, 1)]

    for _ in range(1, small):
        previous, current = current, previous + current
        previous %= m
        current %= m
        current_modulo_pair = (previous, current)
        if current_modulo_pair == (0, 1):
            break
        else:
            modulo.append(current_modulo_pair)
            repeat_after += 1

    index = n % repeat_after
    return modulo[index - 1][1]


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))
