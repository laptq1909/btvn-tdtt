a = map(str, input().split())
lst = []
for i in a:
    lst.append(i)
key = []
value = []
for j in range(len(lst)):
    if j % 2 == 0:
        key.append(lst[j])
    else:
        value.append(lst[j])
print(dict(zip(value, key)))