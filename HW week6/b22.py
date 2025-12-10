a = map(int, input().split())
lst = []
for i in a:
    lst.append(i)
print(lst.index(max(lst)) + 1)