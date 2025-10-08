a = str(input("Ex30: "))
num = 0
cap = 0
low = 0
for i in range(len(a)):
    if a[i].isnumeric():
        num += 1
    elif a[i].isupper():
        cap += 1
    elif a[i].islower():
        low += 1
print(cap, low, num)