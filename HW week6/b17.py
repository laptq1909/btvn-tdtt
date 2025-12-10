m, n = 2, 2
mat = []
for i in range(m):
    mat.append(list(map(int, input().split())))
for x in range(m):
    print(mat[x][x], end=" ")
print()
for x in range(n):
    print(mat[x][n - x - 1], end=" ")
print()