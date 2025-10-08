a = 0
b = 1
A = int(input("Enter a number: "))
lst = [1]
while a + b < A:
    a = b + a
    b = a + b
    lst.append(a)
    lst.append(b)
for i in lst:
    if i > A:
        lst.remove(i)
print(max(lst))