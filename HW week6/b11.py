a = map(int, input().split())
lst1 = []
lst2 = []
for i in a:
    if i % 2 == 0:
        lst1.append(i)
    else:
        lst2.append(i)
print(tuple(lst1))
print(tuple(lst2))