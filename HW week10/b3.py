n = str(input())
lst = []
for i in n:
    lst.append(i)
for i in range(len(lst), 0, -1):
    if lst[i-1] == '0':
        lst[0] = 0
        lst[i-1] = lst[0]
    