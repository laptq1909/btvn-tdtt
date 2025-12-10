a = list(map(int, input().split()))
b = list(map(int, input().split()))
lst = []
for i in a:
    if i in b and i not in lst:
        lst.append(i)
print(lst)