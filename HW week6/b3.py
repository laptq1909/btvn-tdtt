tup = tuple(map(int, input().split()))
k = int(input())
k = k % len(tup)
tup = tup[k:] + tup[:k]
print(tup)