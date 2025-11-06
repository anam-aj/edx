def lcs2(first_sequence, second_sequence):
    edit_dist = edit_distance(first_sequence)
    return 0


def edit_distance(first_string, second_string):

    m, n = len(first_string), len(second_string)

    edit_distances = []

    # Create empty matrix for edit distances
    for i in range(m + 1):
        edit_distances.append([])
        for _ in range(n + 1):
            edit_distances[i].append(0)

    # Fill in edit distance for first row and first column
    for i in range(m + 1):
        edit_distances[i][0] = i
    for i in range(n + 1):
        edit_distances[0][i] = i

    # Compute edit distances for all i and j positions
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            insertion = edit_distances[i][j - 1] + 1
            deletion  = edit_distances[i -1][j] + 1
            mis_match = edit_distances[i - 1][j - 1] + 1
            match = edit_distances[i - 1][j - 1]

            if first_string[i - 1] == second_string[j - 1]:
                edit_distances[i][j] = min(insertion, deletion, match)
            else:
                edit_distances[i][j] = min(insertion, deletion, mis_match)

    return edit_distances[m][n]

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
