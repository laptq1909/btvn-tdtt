a = map(int, input().split())
k = int(input())
lst = []
a = sorted(a)
for i in range(0, len(a)):
    for j in range(i + 1, len(a)):
        if a[i] + a[j] == k:
            if (a[i], a[j]) not in lst:
                lst.append((a[i], a[j]))
print(lst)