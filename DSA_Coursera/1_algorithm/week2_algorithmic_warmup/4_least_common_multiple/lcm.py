def lcm(a, b):
    if a > b:
        big = a
        small = b
    else:
        big = b
        small = a

    current = big
    while True:
        remainder = current % small
        if remainder == 0:
            return current
        else:
            current += big


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

