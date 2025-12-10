m, n, k = map(int, input().split())
matrix = []
for i in range(m):
    matrix.append(list(map(int, input().split())))
col_sum = 0
for j in range(m):
    col_sum += matrix[j][k-1]
print(col_sum)