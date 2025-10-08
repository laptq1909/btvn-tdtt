n = str(int(input("Ex8: ")))
i = 0
while str(n) != str(n)[::-1]:
    n = str(int(n) + int(str(n)[::-1]))
    i = i + 1
print(f"{i} times")
print(f"{n}")