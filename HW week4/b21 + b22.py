n = str(int(input("Ex21: ")))
lst = []
a,b = 0, 0
for i in n:
    lst.append(int(i))
    if int(i) % 2 == 0:
        a += 1
    else:
        b += 1
print(sum(lst))
print(f"Even: {a}, Odd: {b}")