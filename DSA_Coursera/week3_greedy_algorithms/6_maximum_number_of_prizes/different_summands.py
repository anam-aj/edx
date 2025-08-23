def optimal_summands(n):

    summands = []
    sum_summands = 0
    last_summand = 0

    for i in range(1, n):
        sum_summands += i
        if sum_summands <= n:
            summands.append(i)
        else:
            last_summand = i
            break

    if n == 1:
        summands.append(n)
    else:
        gap = n - (sum_summands - last_summand)
        last_term = summands[-1] + gap
        summands[-1] = last_term

    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
