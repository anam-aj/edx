def gcd(a, b):

    if a > b:
        big = a
        small = b
    else:
        big = b
        small = a

    remainder = big % small

    while remainder != 0:
        big = small
        small = remainder
        remainder = big % small

    return small


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
