n = int(input("Ex20: "))
k = 0
if n % 2 != 0 or n <= 0:
    print("Not a power of 2")
while n % 2 == 0:
    n = n//2
    k += 1
if n == 1:
    print(f"Yes a power of 2")
else:
    print("Not a power of 2")