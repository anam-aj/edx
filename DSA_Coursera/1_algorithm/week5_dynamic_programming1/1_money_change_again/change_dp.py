def change(money):
    # List to store min_number_of_coins values
    min_coin_list = [0]

    coins = [1, 3, 4]

    for amount in range(1, money + 1):
        min_coin_list.append(float('inf'))
        for coin in coins:
            if amount >= coin:
                num_of_coins = min_coin_list[amount - coin] + 1
                if num_of_coins < min_coin_list[amount]:
                    min_coin_list[amount] = num_of_coins

    return min_coin_list[money]


if __name__ == '__main__':
    m = int(input())
    print(change(m))
