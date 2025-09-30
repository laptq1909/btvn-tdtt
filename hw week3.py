import math

#1
n = int(input("EX1 "))
revN = int(str(n)[::-1])
print(revN)
#2
a = int(input("EX2 a = "))
b = int(input("EX2 b = "))
a = a^b
b = a^b
a = a^b
print(f"a: {a}, b: {b}")
#3
n = int(input("EX3 "))
if n > 0 and n & (n-1) == 0:
    print(f"True")
else:
    print(f"False")
#4 & 5
m = int(input("EX4 "))
n = int(input("EX5 "))
print(m//n)
print(m//n +1)
#6
a = int(input("EX6 "))
if a % 2 == 0:
    print(f"Even")
else:
    print(f"Odd")
#7
a = int(input("EX7 "))
b = int(input("EX7 "))
if a < 0 and b < 0:
    print(f"Yes")
else:
    print(f"No")
#8
a = str(input("EX8 "))
b = str(input("EX8 "))
if len(a) > len(b):
    print(f"True")
else:
    print(f"False")
#9 & 11
a,b,c = map(int,input("EX9&11 ").split())
if a < 0 or b < 0 or c < 0:
    print(f"Invalid input")
    breakpoint()
if a + b > c and a + c > b and b + c > a:
    print("Yes")
    if a == b == c:
        print(f"Tam giac deu")
    elif b == c or b == a or c == a:
        print(f"Tam giac can")
    else:
        print(f"Tam giac")
else:
    print("No")
#10
a,b,c,d = map(int,input("EX10 ").split())
print(max(a,b,c,d))
#12
n = int(input("EX12 "))
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print(f"Yes")
else:
    print(f"No")
#13
KWH = int(input("EX13 "))
if 0 < KWH < 50:
    print(f"{KWH*1500} VND ")
elif 50 < KWH < 100:
    print(f"{50*1500 + KWH*2000} VND ")
elif 100 < KWH:
    print(f"{KWH*3000 + 50*1500 + 50*2000} VND ")
else:
    print(f"invalid input")
#14
a,b = map(int,input("Enter a, b to put in the equation ax + b = 0, EX14: ").split())
if a == 0 and b == 0:
    print(f"Infinite solution")
elif a == 0:
    print(f"No solution")
else:
    print(f"Your solution is {-b/a}")
#15
a = int(input("EX15 "))
if a >= 8:
    print(f"Gioi")
elif a >= 6.5:
    print(f"Kha")
elif a>= 5:
    print(f"Trung binh")
else:
    print(f"Yeu")
#16
a = float(input("EX16 "))
print(f"{math.ceil(a)}, {math.floor(a)}, {math.trunc(a)}")
#17 = 11