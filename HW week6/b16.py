m, n = map(int, input().split())
mat = []
for _ in range(m):
    mat.append(list(map(int, input().split())))
width = 4
for row in mat:
    print(" ".join(f"{x:>{width}}" for x in row))