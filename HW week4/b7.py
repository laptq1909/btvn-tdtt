n = int(input("Ex7: "))
max_prime = 1
while n % 2 == 0:
    max_prime = 2
    n = n//2
i = 3
import math
limit = int(math.isqrt(n)) + 1
while i <= limit and n > 1:
    while n % i == 0:
        max_prime = i
        n = n // i
        limit = int(math.isqrt(n)) + 1 # update limit
    i += 2
if n > 1:
    max_prime = n
print(max_prime)