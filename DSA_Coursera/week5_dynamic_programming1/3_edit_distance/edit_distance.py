def edit_distance(first_string, second_string):

    m, n = len(first_string), len(second_string)

    dist_matrix = [[]]

    for i in range(m + 1):
        dist_matrix[i][0] = i
    for i in range(n + 1):
        dist_matrix[0][i] = i


    return 0


if __name__ == "__main__":
    print(edit_distance(input(), input()))
