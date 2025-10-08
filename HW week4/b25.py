n = 0
a = 0
lst = []
while n != -1 or a < 2:
    n = int(input("Ex25 (-1 to stop): "))
    a = a + 1
    if n != -1:
        lst.append(n)
    elif n == -1 and a >= 2:
        print(max(lst), min(lst))
        break