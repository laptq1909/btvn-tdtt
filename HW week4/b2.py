n = int(input("Ex2: "))
count = 0
for i in range(2,n+1):
    if n % i == 0:
        count = count + 1
if n == 1:
    print("False")
if count > 1 and n != 1:
    print("False")
elif n!=1:
    print("True")