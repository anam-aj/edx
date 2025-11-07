def lcs3(first_sequence, second_sequence, third_sequence):

    m, n, r = len(first_sequence), len(second_sequence), len(third_sequence)

    lcs = []
    for i in range(m + 1):
        lcs.append([])
        for j in range(n + 1):
            lcs[i].append([])
            for k in range(r + 1):
                lcs[i][j].append(0)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            for k in range(1, r + 1):

                if (first_sequence[i - 1] == second_sequence[j - 1] and
                    first_sequence[i - 1] == second_sequence[j - 1]):
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
