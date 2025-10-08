n1 = int(input("Ex13 num1: "))
n2 = int(input("Ex13 num2: "))
lst1 = []
lst2 = []
for i in range(1,n1):
    if n1 % i == 0:
        lst1.append(i)
for j in range(1,n2):
    if n2 % j == 0:
        lst2.append(j)
total1 = sum(lst1)
total2 = sum(lst2)
if total1 == n2 and total2 == n1:
    print("True")
else:
    print("False")