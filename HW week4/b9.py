import math
n = int(input("Ex9: "))
for i in range(1, int(math.isqrt(n)) + 1):
    if i**2 <= n:
        print(i**2, end=' ')