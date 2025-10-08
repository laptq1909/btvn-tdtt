a = int(input("Ex6 start: "))
b = int(input("Ex6 end: "))
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
total = 0
for num in range(a, b + 1):
    if is_prime(num):
        total += num
print("Sum: ", total)