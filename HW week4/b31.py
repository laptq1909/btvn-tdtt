a = str(input("Ex31: "))
num = 0
for i in range(0, len(a)):
    if a[i].isnumeric():
        num += int(a[i])
print(num)