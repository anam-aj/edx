def change(money):
    change = (money // 10) + ((money % 10) // 5) + (money % 5)

    return change


if __name__ == '__main__':
    m = int(input())
    print(change(m))
