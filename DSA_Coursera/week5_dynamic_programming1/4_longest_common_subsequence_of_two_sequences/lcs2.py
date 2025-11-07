def lcs2(first_sequence, second_sequence):

    m, n = len(first_sequence), len(second_sequence)

    lcs = []

    # Create empty matrix for edit distances
    for i in range(m + 1):
        lcs.append([])
        for _ in range(n + 1):
            lcs[i].append(0)

    # Compute edit distances for all i and j positions
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            insertion = lcs[i][j - 1]
            deletion  = lcs[i -1][j]
            mis_match = lcs[i - 1][j - 1]
            match = lcs[i - 1][j - 1] + 1

            if first_sequence[i - 1] == second_sequence[j - 1]:
                lcs[i][j] = max(insertion, deletion, match)
            else:
                lcs[i][j] = max(insertion, deletion, mis_match)

    return lcs[m][n]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
