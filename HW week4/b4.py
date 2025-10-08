n = int(input("Ex4: : "))
a = 1
if n<=0:
    n = -n
while n/10 > 1:
    a += 1
    n = n/10
    if n / 10 == 1:
        a += 1
        break
print(a)