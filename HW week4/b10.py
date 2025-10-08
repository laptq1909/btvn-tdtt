n = int(input("Ex10: "))
a = 1
lst = []
for x in range(1, n + 1):
    while x != 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1
        a += 1
    lst.append(a)
    a = 1
print(lst.index(max(lst)) + 1)
print(max(lst))