b = int(input())
n = list(map(str, input().split()))
lst = []
for i in range(len(n)):
    if n[i] == "7":
        lst.append(i)
print(*lst if len(lst) > 0 else "Not found")