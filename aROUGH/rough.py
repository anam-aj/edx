m, n = 3, 4
dist_matrix = []

for i in range(m + 1):
    dist_matrix.append([])
    for j in range(n + 1):
        dist_matrix[i].append(0)

print(dist_matrix)

'''
for i in range(m + 1):
    dist_matrix[i][0] = i
for i in range(n + 1):
    dist_matrix[0][i] = i

print(dist_matrix)
'''

