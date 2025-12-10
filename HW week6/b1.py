lst = list(map(int, input().split()))
m = {}
a = []
for i in lst:
    if i in m:
        continue
    else:
        a.append(i)
        m[i] = 1
print(a)