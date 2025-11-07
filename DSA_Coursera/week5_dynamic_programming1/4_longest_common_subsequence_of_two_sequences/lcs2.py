def lcs2(first_sequence, second_sequence):

    m, n = len(first_sequence), len(second_sequence)

    lcs = []
    count = 0

    # Create empty matrix for edit distances
    for i in range(m + 1):
        lcs.append([])
        for _ in range(n + 1):
            lcs[i].append(0)
    '''
    # Fill in edit distance for first row and first column
    for i in range(m + 1):
        edit_distances[i][0] = i
    for i in range(n + 1):
        edit_distances[0][i] = i
    '''

    # Compute edit distances for all i and j positions
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            insertion = edit_distances[i][j - 1] + 1
            deletion  = edit_distances[i -1][j] + 1
            mis_match = edit_distances[i - 1][j - 1] + 1
            match = edit_distances[i - 1][j - 1]

            if first_sequence[i - 1] == second_sequence[j - 1]:
                edit_distances[i][j] = min(insertion, deletion, match)
                if min(insertion, deletion, match) == deletion:
                    count += 1
            else:
                edit_distances[i][j] = min(insertion, deletion, mis_match)
                if min(insertion, deletion, mis_match) == deletion or min(insertion, deletion, mis_match) == mis_match:
                    count += 1
    los = m - count

    return los


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
