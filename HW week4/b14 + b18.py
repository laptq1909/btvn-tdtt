num1 = int(input("Ex14 num1: "))
num2 = int(input("Ex14 num2: "))
lst1 = []
lst2 = []
lst3 = []
for i in range(1, num1):
    if num1 % i == 0:
        lst1.append(i)
for j in range(1, num2):
    if num2 % j == 0:
        lst2.append(j)
for k in lst1:
    if k in lst2:
        lst3.append(k)
print(f"GCD of {num1} and {num2} is {max(lst3)}")